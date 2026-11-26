# UX/UI product design skill

Agent skill UX/UI és product design munkához: meglévő felület áttervezéséhez és nulláról induló weboldalhoz vagy apphoz. Nem kivitelez (nem ír Figma-fájlt vagy frontend kódot), hanem a döntéseket adja: milyen sorrendben gondolkodjon az AI, mi kerüljön a képernyőre és mi ne, hogyan épüljön a szín-, szöveg-, betű- és ikonrendszer, és mit ellenőrizzen átadás előtt. Ha mellette eszközhöz kötött skill is fut, az a kivitelezést adja, ez a döntéseket.

Az [Agent Skills](https://agentskills.io) nyílt szabványt követi, ezért a **Claude** (Claude Code, Claude.ai, Claude Agent SDK) és az **OpenAI Codex** (CLI, IDE-bővítmény, ChatGPT asztali app) is ugyanazt a mappát használja.

## Mit csinál

- **Javaslattal kezd, nem kérdőívvel:** 3–7 pontos megoldás, rögtön egy minta, a kihagyott elemek listája és legfeljebb három kérdés, mindegyikhez javasolt válasszal. Indoklást csak kérésre ad.
- **Munkamenet:** a flow szöveges bejárása rajz előtt, tartalmi szűrés (kötelező, szükséges, feltételes, fölösleges, tisztázandó), vizuális irány, struktúra, tokenek, képernyő, állapotok, ellenőrzés.
- **Nulláról induló weboldal és app:** alapozó döntések és kötelező listák (Core Web Vitals, kereshetőség, jogi elemek, platformkonvenciók, engedélykérés, offline működés).
- **Rendszerek mérhető küszöbökkel:** elrendezés és gombhierarchia, színrendszer OKLCH-ban, betűválasztás, szöveghierarchia, ikonok, űrlapok, akadálymentesség.
- **19 próba átadás előtt**, például: fordított bejárás, hunyorítási próba, akcentusszámlálás, kontraszt, paletta-audit, renderelés.

## Felépítés

```
skills/ux-ui-product-design/
├── SKILL.md             # a skill: munkamenet, szabályok, ellenőrzés
├── scripts/palette.py   # palettaszámolás, kontraszt, színaudit (Python 3, függőség nélkül)
└── agents/openai.yaml   # Codex/ChatGPT megjelenítési adatok (nem kötelező)
```

## Telepítés

Töltsd le a repót:

```bash
git clone https://github.com/Hello-agency-hun/ux-ui-product-design.git
```

**Claude Code** (minden projektben):

```bash
cp -R ux-ui-product-design/skills/ux-ui-product-design ~/.claude/skills/
```

Csak egy projektben: másold a projekt `.claude/skills/` mappájába.

**Codex** (minden projektben):

```bash
cp -R ux-ui-product-design/skills/ux-ui-product-design ~/.agents/skills/
```

Csak egy repóban: másold a repó `.agents/skills/` mappájába. Codexben a `$skill-installer` is fel tudja telepíteni a repó címéből.

**Claude.ai:** a `skills/ux-ui-product-design` mappát tömörítsd zipbe, és töltsd fel a beállítások Skills részén.

A skill magától bekapcsol, ha felületet, appot, weboldalt, flow-t, űrlapot vagy dashboardot kell tervezni, áttervezni vagy átnézni. Kézzel is hívható: Claude Code-ban `/ux-ui-product-design`, Codexben `$ux-ui-product-design`.

## Palettaszkript

A skill színszabályait (12 lépcsős semleges skála az akcentushoz hangolva, akcentusskála, jelentésszínek, kategóriaszínek, kontrasztküszöbök) a `scripts/palette.py` számolja ki. Csak Python 3.8+ kell hozzá.

```bash
cd skills/ux-ui-product-design
python3 scripts/palette.py generate --accent "#4F46E5"                    # táblázat + kontrasztjelentés
python3 scripts/palette.py generate --accent "#4F46E5" --format css       # CSS-változók
python3 scripts/palette.py generate --accent "#4F46E5" --format json > palette.json
python3 scripts/palette.py contrast "#575667" "#F0EFF8"                   # egy pár ellenőrzése
python3 scripts/palette.py audit --palette palette.json ../../src         # palettán kívüli színek keresése
```

A `generate` és az `audit` hibakóddal (1) lép ki, ha egy kontrasztpár nem éri el a küszöböt, vagy ha palettán kívüli szín maradt. Így CI-ban is használható. A szkript világos témát számol.

## English

An agent skill for UX/UI and product design decisions (flow walkthroughs, content triage, color system, typography, icons, pre-handoff checks), compatible with Claude and OpenAI Codex via the open Agent Skills format. The skill text is written in Hungarian; the agent answers in the user's language. Install by copying `skills/ux-ui-product-design` into `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (Codex). `scripts/palette.py` (Python 3, no dependencies) generates an OKLCH-based palette with WCAG contrast checks and audits files for off-palette colors.

## Licenc

MIT, lásd [LICENSE](LICENSE).
