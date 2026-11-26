#!/usr/bin/env python3
"""Felületi paletta számolása OKLCH-ból, kontrasztellenőrzés és színaudit.

Csak a Python standard könyvtárát használja (3.8+), telepíteni semmit nem kell.

Parancsok:
  generate  Egy akcentusszínből kiszámolja a teljes világos témájú palettát:
            12 lépcsős semleges skála, 12 lépcsős akcentusskála, jelentésszínek
            (siker, figyelmeztetés, hiba, információ) és kérésre kategóriaszínek.
            A végén kontrasztjelentést ad a fontos szöveg-háttér párokról.
  contrast  Két szín WCAG-kontrasztaránya és a küszöbök.
  audit     Megkeresi a fájlokban azokat a színkódokat, amelyek nincsenek a palettán.

Példák:
  python3 palette.py generate --accent "#4F46E5"
  python3 palette.py generate --accent "#4F46E5" --categories 4 --format css > tokens.css
  python3 palette.py generate --accent "#4F46E5" --format json > palette.json
  python3 palette.py contrast "#5B5B70" "#F0F0F8"
  python3 palette.py audit --palette palette.json src/ index.html
"""

import argparse
import json
import math
import os
import re
import sys

# ---------------------------------------------------------------------------
# Színtér-átváltások (Björn Ottosson Oklab-képletei, sRGB D65)
# ---------------------------------------------------------------------------


def _srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _linear_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def _cbrt(x):
    return math.copysign(abs(x) ** (1 / 3), x)


def linear_rgb_to_oklab(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = _cbrt(l), _cbrt(m), _cbrt(s)
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_linear_rgb(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def oklch_to_linear_rgb(L, C, H):
    h = math.radians(H)
    return oklab_to_linear_rgb(L, C * math.cos(h), C * math.sin(h))


def in_gamut(rgb, eps=1e-6):
    return all(-eps <= c <= 1 + eps for c in rgb)


def max_chroma(L, H):
    """A legnagyobb C, ami adott L és H mellett még sRGB-ben ábrázolható."""
    lo, hi = 0.0, 0.4
    for _ in range(40):
        mid = (lo + hi) / 2
        if in_gamut(oklch_to_linear_rgb(L, mid, H)):
            lo = mid
        else:
            hi = mid
    return lo


class Color:
    """OKLCH-ban megadott szín; ha kilógna az sRGB-ből, a telítettséget csökkenti."""

    def __init__(self, L, C, H):
        L = min(max(L, 0.0), 1.0)
        C = max(C, 0.0)
        self.L, self.C, self.H = L, min(C, max_chroma(L, H)), H % 360
        lin = oklch_to_linear_rgb(self.L, self.C, self.H)
        self.lin = tuple(min(max(c, 0.0), 1.0) for c in lin)

    @classmethod
    def from_hex(cls, value):
        lin = hex_to_linear(value)
        L, a, b = linear_rgb_to_oklab(*lin)
        C = math.hypot(a, b)
        H = math.degrees(math.atan2(b, a)) % 360 if C > 1e-6 else 0.0
        obj = cls.__new__(cls)
        obj.L, obj.C, obj.H, obj.lin = L, C, H, lin
        return obj

    @property
    def hex(self):
        return "#" + "".join(
            "{:02X}".format(int(round(min(max(_linear_to_srgb(c), 0.0), 1.0) * 255))) for c in self.lin
        )

    @property
    def oklch(self):
        return "oklch({:.3f} {:.3f} {:.1f})".format(self.L, self.C, self.H)

    @property
    def luminance(self):
        # A WCAG-luminanciát a kerekített hexből számoljuk, mert az kerül a kódba.
        r, g, b = hex_to_linear(self.hex)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b


# ---------------------------------------------------------------------------
# Segédfüggvények
# ---------------------------------------------------------------------------

HEX_RE = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
OKLCH_RE = re.compile(r"^oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)(?:deg)?\s*(?:/\s*[\d.%]+\s*)?\)$", re.I)


def normalize_hex(value):
    m = HEX_RE.match(value.strip())
    if not m:
        raise ValueError("Érvénytelen hexkód: {}".format(value))
    h = m.group(1)
    if len(h) in (3, 4):
        h = "".join(ch * 2 for ch in h[:3])
    return "#" + h[:6].upper()


def hex_to_linear(value):
    h = normalize_hex(value)[1:]
    return tuple(_srgb_to_linear(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))


def parse_color(value):
    value = value.strip()
    m = OKLCH_RE.match(value)
    if m:
        L = float(m.group(1)) / (100 if m.group(2) else 1)
        return Color(L, float(m.group(3)), float(m.group(4)))
    return Color.from_hex(value)


def contrast(c1, c2):
    a, b = c1.luminance, c2.luminance
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def hue_distance(h1, h2):
    d = abs(h1 - h2) % 360
    return min(d, 360 - d)


def oklab_distance(c1, c2):
    a = linear_rgb_to_oklab(*c1.lin)
    b = linear_rgb_to_oklab(*c2.lin)
    return 100 * math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def darken_until(L, C, H, backgrounds, target, floor=0.2):
    """Addig sötétít, amíg a szín minden háttéren eléri a kontrasztküszöböt."""
    color = Color(L, C, H)
    while L > floor and min(contrast(color, bg) for bg in backgrounds) < target:
        L -= 0.005
        color = Color(L, C, H)
    return color


# ---------------------------------------------------------------------------
# Palettaszámolás (világos téma)
# ---------------------------------------------------------------------------

# Semleges skála: (L, a telítettség aránya a --neutral-chroma értékhez), lépcsőnként.
NEUTRAL_STEPS = [
    (0.993, 0.25),  # 1  alkalmazás háttere
    (0.975, 0.35),  # 2  halk háttér (oldalsáv, sávozott sor)
    (0.955, 0.40),  # 3  komponens háttere, halvány panel
    (0.930, 0.45),  # 4  hover
    (0.905, 0.50),  # 5  lenyomott, kiválasztott
    (0.880, 0.55),  # 6  halk elválasztó
    (0.835, 0.60),  # 7  interaktív elem kerete
    (0.760, 0.65),  # 8  erős keret, fókuszgyűrű
    (0.560, 0.80),  # 9  tömör háttér
    (0.510, 0.85),  # 10 tömör háttér hovere
    (0.460, 0.90),  # 11 másodlagos szöveg
    (0.220, 1.00),  # 12 elsődleges szöveg
]

NEUTRAL_ROLES = [
    "alkalmazás háttere", "halk háttér", "komponens háttere, halvány panel", "hover",
    "lenyomott, kiválasztott", "halk elválasztó", "interaktív elem kerete",
    "erős keret, fókuszgyűrű", "tömör háttér", "tömör háttér hovere",
    "másodlagos szöveg", "elsődleges szöveg",
]

# Akcentusskála: (L, C) a világos lépcsőkhöz; a 9. lépcső maga a megadott akcentus.
ACCENT_LIGHT_STEPS = [
    (0.985, 0.012), (0.965, 0.025), (0.935, 0.045), (0.905, 0.060),
    (0.870, 0.080), (0.830, 0.100), (0.770, 0.130), (0.700, 0.160),
]

ACCENT_ROLES = [
    "legfinomabb háttér", "finom háttér", "kiválasztott háttér", "hover a kiválasztotton",
    "halvány akcentus-felület, másodlagos gomb", "halvány keret", "keret", "erős keret, fókusz",
    "tömör: a fő művelet", "a fő művelet hovere", "akcentusszínű szöveg, link", "legsötétebb akcentus",
]

# Jelentésszínek bevett színezete (OKLCH H). A figyelmeztetés ikonja narancs felé hajlik.
SEMANTIC_HUES = {"success": 150, "warning": 75, "danger": 27, "info": 245}
SEMANTIC_ICON_HUE = {"warning": 55}
SEMANTIC_LABELS = {"success": "siker", "warning": "figyelmeztetés", "danger": "hiba, rombolás", "info": "információ"}


def auto_light_shift(hue):
    """Kék-lila akcentusnál a világos lépcsők a lila felé fordulnak (kb. 12 fok)."""
    return 12.0 if 255 <= hue <= 295 else 0.0


def build_palette(accent, neutral_chroma, light_shift, categories):
    tokens = []  # (név, Color, szerep)
    warnings = []
    white = Color(1.0, 0.0, 0.0)

    if accent.C < 0.06:
        warnings.append("Az akcentus telítettsége alacsony (C {:.3f}): alig fog elválni a szürkéktől.".format(accent.C))
    for key, hue in SEMANTIC_HUES.items():
        if key != "info" and hue_distance(accent.H, hue) < 30:
            warnings.append("Az akcentus színezete közel esik a(z) {} jelentésszínhez ({:.0f}°): válassz olyan árnyalatot, aminek nincs státuszjelentése.".format(SEMANTIC_LABELS[key], hue_distance(accent.H, hue)))

    light_hue = accent.H + light_shift
    chroma_scale = min(1.0, accent.C / 0.20)

    tokens.append(("white", white, "fehér munkafelület"))

    # Semleges skála a halvány akcentus-lépcső színezetéhez hangolva.
    for i, (L, k) in enumerate(NEUTRAL_STEPS, start=1):
        tokens.append(("neutral-{}".format(i), Color(L, neutral_chroma * k, light_hue), NEUTRAL_ROLES[i - 1]))
    neutral = {n: c for n, c, _ in tokens}
    text_backgrounds = [white, neutral["neutral-1"], neutral["neutral-2"], neutral["neutral-3"]]

    # A másodlagos szöveg a halvány paneleken is legyen olvasható (4,5:1),
    # az erős keret és a fókuszgyűrű fehéren nem szöveges elemként is látsszon (3:1).
    for name, backgrounds, target in (("neutral-11", text_backgrounds, 4.5), ("neutral-8", [white], 3.0)):
        old = neutral[name]
        fixed = darken_until(old.L, old.C, old.H, backgrounds, target)
        idx = [t[0] for t in tokens].index(name)
        tokens[idx] = (name, fixed, tokens[idx][2])
        neutral[name] = fixed

    # Akcentusskála.
    for i, (L, C) in enumerate(ACCENT_LIGHT_STEPS, start=1):
        hue = light_hue if L > 0.85 else accent.H
        color = Color(L, C * chroma_scale, hue)
        if i == 8:
            # Az erős keret és a fókuszjelző fehéren legalább 3:1.
            color = darken_until(L, C * chroma_scale, hue, [white], 3.0)
        tokens.append(("accent-{}".format(i), color, ACCENT_ROLES[i - 1]))
    tokens.append(("accent-9", accent, ACCENT_ROLES[8]))
    tokens.append(("accent-10", Color(accent.L - 0.05, accent.C, accent.H), ACCENT_ROLES[9]))
    accent_text = darken_until(min(accent.L - 0.08, 0.45), accent.C, accent.H, text_backgrounds, 4.5)
    tokens.append(("accent-11", accent_text, ACCENT_ROLES[10]))
    tokens.append(("accent-12", Color(min(accent_text.L - 0.12, 0.32), accent.C * 0.7, accent.H), ACCENT_ROLES[11]))

    # A fő művelet felirata: fehér, ha elég a kontraszt, különben a legsötétebb szöveg.
    if contrast(white, accent) >= 4.5:
        tokens.append(("on-accent", white, "felirat a tömör akcentuson"))
    else:
        dark = [c for n, c, _ in tokens if n == "neutral-12"][0]
        tokens.append(("on-accent", dark, "felirat a tömör akcentuson"))
        warnings.append("Fehér szöveg a tömör akcentuson csak {:.2f}:1, ezért a felirata sötét.".format(contrast(white, accent)))

    # Jelentésszínek: halvány háttér, keret, ikon (nem szöveges elem, 3:1) és sötét szöveg (4,5:1).
    for key, hue in SEMANTIC_HUES.items():
        bg = Color(0.960, 0.030, hue)
        border = Color(0.820, 0.090, hue)
        icon_hue = SEMANTIC_ICON_HUE.get(key, hue)
        icon = darken_until(0.680, 0.170, icon_hue, [white, bg], 3.0)
        text = darken_until(0.520, 0.150, hue, [white, bg, neutral["neutral-1"]], 4.5)
        label = SEMANTIC_LABELS[key]
        tokens += [
            ("{}-bg".format(key), bg, "{}: halvány háttér".format(label)),
            ("{}-border".format(key), border, "{}: keret".format(label)),
            ("{}-icon".format(key), icon, "{}: ikon, pötty, vékony él".format(label)),
            ("{}-text".format(key), text, "{}: szöveg".format(label)),
        ]

    # Kategóriaszínek: azonos szerepben azonos L és C, csak a színezet tér el.
    if categories:
        hues = pick_category_hues(categories, accent.H)
        spacing = min(hue_distance(a, b) for i, a in enumerate(hues) for b in hues[i + 1:]) if len(hues) > 1 else 360
        if spacing < 40:
            warnings.append("A kategóriaszínek legkisebb távolsága {:.0f}° (cél: legalább 40°). Vonj össze kategóriákat, vagy jelöld őket formával és felirattal.".format(spacing))
        for h in hues:
            near = [SEMANTIC_LABELS[k] for k, sh in SEMANTIC_HUES.items() if hue_distance(h, sh) < 20]
            if near:
                warnings.append("A {:.0f}°-os kategóriaszín közel esik ehhez: {}. Ne adj neki státuszjelentést.".format(h, ", ".join(near)))
        roles = {"bg": (0.935, 0.045), "edge": (0.630, 0.130), "text": (0.450, 0.110)}
        for role, (L, C) in roles.items():
            # Az összes színezeten ábrázolható közös telítettség.
            common_c = min([C] + [max_chroma(L, h) for h in hues])
            roles[role] = (L, common_c)
        for i, h in enumerate(hues, start=1):
            for role, (L, C) in roles.items():
                tokens.append(("cat-{}-{}".format(i, role), Color(L, C, h), "{}. kategória: {}".format(i, {"bg": "halvány háttér", "edge": "sáv, él", "text": "szöveg"}[role])))

    tokens = order_tokens(tokens)
    return tokens, warnings


def pick_category_hues(n, accent_hue):
    """Mohó maximin-választás: az akcentustól legalább 30°, a jelentésszínektől minél messzebb."""
    candidates = [float(h) for h in range(0, 360, 5) if hue_distance(h, accent_hue) >= 30]
    chosen = []
    for _ in range(min(n, 6)):
        best, best_score = None, -1.0
        for h in candidates:
            if h in chosen:
                continue
            d_main = min([hue_distance(h, c) for c in chosen + [accent_hue]])
            d_sem = min(hue_distance(h, s) for s in SEMANTIC_HUES.values())
            score = min(d_main, 2 * d_sem)
            if score > best_score:
                best, best_score = h, score
        chosen.append(best)
    return sorted(chosen)


def order_tokens(tokens):
    def key(item):
        name = item[0]
        m = re.match(r"^(neutral|accent)-(\d+)$", name)
        group_order = {"white": 0, "neutral": 1, "accent": 2, "on-accent": 3}
        if m:
            return (group_order[m.group(1)], int(m.group(2)))
        if name in group_order:
            return (group_order[name], 0)
        return (4, 0)

    # Stabil rendezés: a jelentés- és kategóriaszínek megtartják a felvétel sorrendjét.
    return sorted(tokens, key=key)


def contrast_report(tokens):
    t = {n: c for n, c, _ in tokens}
    pairs = [
        ("neutral-12", "white", 4.5, "elsődleges szöveg fehéren"),
        ("neutral-12", "neutral-3", 4.5, "elsődleges szöveg halvány panelen"),
        ("neutral-11", "white", 4.5, "másodlagos szöveg fehéren"),
        ("neutral-11", "neutral-3", 4.5, "másodlagos szöveg halvány panelen"),
        ("neutral-8", "white", 3.0, "erős keret, fókuszgyűrű fehéren"),
        ("accent-8", "white", 3.0, "akcentusszínű fókuszjelző fehéren"),
        ("accent-11", "white", 4.5, "link, akcentusszöveg fehéren"),
        ("accent-11", "neutral-3", 4.5, "link halvány panelen"),
        ("accent-11", "accent-5", 4.5, "akcentusszöveg halvány akcentus-felületen"),
        ("on-accent", "accent-9", 4.5, "fő művelet felirata"),
        ("accent-9", "white", 3.0, "fő művelet gombja fehéren (nem szöveges)"),
    ]
    for key in SEMANTIC_HUES:
        pairs += [
            ("{}-text".format(key), "{}-bg".format(key), 4.5, "{} szöveg a saját hátterén".format(SEMANTIC_LABELS[key])),
            ("{}-text".format(key), "white", 4.5, "{} szöveg fehéren".format(SEMANTIC_LABELS[key])),
            ("{}-icon".format(key), "white", 3.0, "{} ikon fehéren (nem szöveges)".format(SEMANTIC_LABELS[key])),
        ]
    i = 1
    while "cat-{}-text".format(i) in t:
        pairs += [
            ("cat-{}-text".format(i), "cat-{}-bg".format(i), 4.5, "{}. kategória szövege a hátterén".format(i)),
            ("cat-{}-edge".format(i), "white", 3.0, "{}. kategória sávja fehéren (nem szöveges)".format(i)),
        ]
        i += 1
    rows = []
    for fg, bg, target, label in pairs:
        ratio = contrast(t[fg], t[bg])
        rows.append({"fg": fg, "bg": bg, "ratio": round(ratio, 2), "target": target, "pass": ratio >= target, "label": label})
    return rows


# ---------------------------------------------------------------------------
# Kimenetek
# ---------------------------------------------------------------------------


def print_table(tokens, report, warnings, accent, light_shift):
    print("# Paletta")
    print()
    print("Akcentus: {} ({}), a világos lépcsők színezet-eltolása: {:+.0f}°".format(accent.hex, accent.oklch, light_shift))
    print()
    print("| Token | Hex | OKLCH | Szerep |")
    print("|---|---|---|---|")
    for name, color, role in tokens:
        print("| {} | {} | {} | {} |".format(name, color.hex, color.oklch, role))
    print()
    print_report(report)
    if warnings:
        print()
        print("## Figyelmeztetések")
        print()
        for w in warnings:
            print("- " + w)


def print_report(report, stream=sys.stdout):
    print("## Kontraszt", file=stream)
    print(file=stream)
    print("| Pár | Arány | Küszöb | Eredmény |", file=stream)
    print("|---|---|---|---|", file=stream)
    for r in report:
        print("| {} ({} / {}) | {:.2f}:1 | {}:1 | {} |".format(
            r["label"], r["fg"], r["bg"], r["ratio"], r["target"], "OK" if r["pass"] else "HIBA"), file=stream)


def print_css(tokens):
    print(":root {")
    for name, color, role in tokens:
        print("  --{}: {}; /* {} | {} */".format(name, color.hex, color.oklch, role))
    print("}")


def to_json(tokens, report, warnings, accent, light_shift):
    return {
        "accent": accent.hex,
        "lightHueShift": light_shift,
        "tokens": {n: {"hex": c.hex, "oklch": c.oklch, "role": r} for n, c, r in tokens},
        "contrast": report,
        "warnings": warnings,
    }


# ---------------------------------------------------------------------------
# Audit: a palettán kívüli színkódok megkeresése
# ---------------------------------------------------------------------------

SCAN_EXTENSIONS = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".js", ".jsx", ".ts", ".tsx",
                   ".vue", ".svelte", ".svg", ".json", ".md", ".mdx", ".astro", ".php", ".twig", ".liquid"}
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", ".nuxt", "vendor", "__pycache__"}
COLOR_IN_TEXT = re.compile(
    r"(?<![\w&])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![\w-])"
    r"|rgba?\(\s*\d{1,3}\s*[, ]\s*\d{1,3}\s*[, ]\s*\d{1,3}[^)]*\)"
    r"|oklch\([^)]*\)",
    re.I,
)


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    if os.path.splitext(f)[1].lower() in SCAN_EXTENSIONS:
                        yield os.path.join(root, f)
        else:
            print("Nem található: {}".format(p), file=sys.stderr)


def color_from_match(text):
    t = text.strip()
    if t.startswith("#"):
        return Color.from_hex(t)
    if t.lower().startswith("rgb"):
        nums = [int(x) for x in re.findall(r"\d{1,3}", t)[:3]]
        return Color.from_hex("#" + "".join("{:02X}".format(min(n, 255)) for n in nums))
    return parse_color(t)


def run_audit(palette, paths):
    allowed = {}
    for name, color in palette.items():
        allowed.setdefault(color.hex, name)
    off, near, black = [], [], []
    for path in iter_files(paths):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
        except OSError as exc:
            print("Nem olvasható: {} ({})".format(path, exc), file=sys.stderr)
            continue
        for no, line in enumerate(lines, start=1):
            for m in COLOR_IN_TEXT.finditer(line):
                try:
                    color = color_from_match(m.group(0))
                except ValueError:
                    continue
                if color.hex in allowed:
                    continue
                where = "{}:{}".format(path, no)
                if color.hex == "#000000":
                    black.append((where, m.group(0)))
                    continue
                best = min(palette.items(), key=lambda kv: oklab_distance(color, kv[1]))
                dist = oklab_distance(color, best[1])
                if dist < 0.25:
                    # Kerekítési zaj (például háromtizedes oklch()): ugyanaz a token.
                    continue
                entry = (where, m.group(0), best[0], best[1].hex, dist)
                (near if dist < 1.0 else off).append(entry)
    print("# Színaudit")
    print()
    if not (off or near or black):
        print("Minden talált színkód a palettáról való.")
        return 0
    if black:
        print("## Tiszta fekete (cseréld a semleges skála sötét lépcsőjére)")
        print()
        for where, raw in black:
            print("- {} `{}`".format(where, raw))
        print()
    if off:
        print("## Palettán kívüli színek")
        print()
        for where, raw, name, hexv, dist in off:
            print("- {} `{}` → legközelebbi: {} {} (eltérés {:.1f})".format(where, raw, name, hexv, dist))
        print()
    if near:
        print("## Szinte egyező színek (valószínűleg kerekítés, cseréld a pontos tokenre)")
        print()
        for where, raw, name, hexv, dist in near:
            print("- {} `{}` → {} {}".format(where, raw, name, hexv))
    return 1


def load_palette(args):
    if args.palette:
        with open(args.palette, encoding="utf-8") as fh:
            data = json.load(fh)
        tokens = data.get("tokens", data)
        palette = {}
        for name, value in tokens.items():
            raw = value["hex"] if isinstance(value, dict) else value
            palette[name] = Color.from_hex(raw)
        return palette
    accent = parse_color(args.accent)
    shift = auto_light_shift(accent.H) if args.light_shift is None else args.light_shift
    tokens, _ = build_palette(accent, args.neutral_chroma, shift, args.categories)
    return {n: c for n, c, _ in tokens}


# ---------------------------------------------------------------------------
# Parancssor
# ---------------------------------------------------------------------------


def add_generation_args(p):
    p.add_argument("--accent", help='Akcentusszín: hex ("#4F46E5") vagy oklch ("oklch(0.51 0.23 277)").')
    p.add_argument("--neutral-chroma", type=float, default=0.03,
                   help="A semleges skála legnagyobb telítettsége (0,005–0,04; alap: 0,03).")
    p.add_argument("--light-shift", type=float, default=None,
                   help="A világos lépcsők színezet-eltolása fokban (alap: kék-lila akcentusnál +12, máskor 0).")
    p.add_argument("--categories", type=int, default=0, help="Kategóriaszínek száma (0–6).")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command")

    gen = sub.add_parser("generate", help="Paletta számolása egy akcentusszínből.")
    add_generation_args(gen)
    gen.add_argument("--format", choices=["table", "css", "json"], default="table")

    con = sub.add_parser("contrast", help="Két szín kontrasztaránya.")
    con.add_argument("foreground")
    con.add_argument("background")

    aud = sub.add_parser("audit", help="Palettán kívüli színkódok keresése fájlokban.")
    aud.add_argument("paths", nargs="+", help="Fájlok vagy mappák.")
    aud.add_argument("--palette", help="A generate --format json kimenete.")
    add_generation_args(aud)

    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 2

    if args.command == "contrast":
        fg, bg = parse_color(args.foreground), parse_color(args.background)
        ratio = contrast(fg, bg)
        print("{} / {}: {:.2f}:1".format(fg.hex, bg.hex, ratio))
        for target, label in ((4.5, "törzsszöveg"), (3.0, "nagy szöveg, nem szöveges elem")):
            print("  {} ({}:1): {}".format(label, target, "OK" if ratio >= target else "HIBA"))
        return 0 if ratio >= 4.5 else 1

    if args.command == "audit":
        if not args.palette and not args.accent:
            parser.error("az audithoz --palette vagy --accent kell")
        return run_audit(load_palette(args), args.paths)

    if not args.accent:
        parser.error("a generate parancshoz --accent kell")
    if not 0 <= args.categories <= 6:
        parser.error("a kategóriaszínek száma 0 és 6 között lehet")
    accent = parse_color(args.accent)
    shift = auto_light_shift(accent.H) if args.light_shift is None else args.light_shift
    tokens, warnings = build_palette(accent, args.neutral_chroma, shift, args.categories)
    report = contrast_report(tokens)
    failed = [r for r in report if not r["pass"]]
    if failed:
        warnings.append("{} kontrasztpár nem éri el a küszöböt (lásd a táblázatban: HIBA).".format(len(failed)))

    if args.format == "table":
        print_table(tokens, report, warnings, accent, shift)
    elif args.format == "css":
        print_css(tokens)
        if failed:
            print_report(failed, stream=sys.stderr)
    else:
        json.dump(to_json(tokens, report, warnings, accent, shift), sys.stdout, ensure_ascii=False, indent=2)
        print()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
