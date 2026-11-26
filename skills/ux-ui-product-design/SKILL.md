---
name: "ux-ui-product-design"
description: "Kutatásra épülő UX/UI és product design meglévő felülethez és nulláról induló weboldalhoz, apphoz: javaslat és minta az elején, tartalmi szűrés, flow-bejárás, színrendszer, felirat-hierarchia, betűtípus, ikonok. Használd mindig, ha felületet, appot, weboldalt, flow-t, űrlapot, dashboardot kell tervezni, áttervezni vagy átnézni."
---

# UX/UI product design

Ez a skill azt írja le, hogyan hozz tervezési döntéseket, akár meglévő felületet tervezel át, akár nulláról indul egy weboldal vagy app. Gondolkodási sorrendet, tartalmi szűrőt, szín-, szöveg-, betű- és ikonrendszert, valamint mérhető küszöböket ad. Ha van eszközhöz kötött skill is (Figma, frontend kód, design vászon), az a kivitelezést adja, ez pedig a döntéseket: előbb ezt alkalmazd, utána azt.

A felhasználó nyelvén válaszolj. A szakszavak (primary action, empty state) maradhatnak angolul.

## Alapállás

A felhasználó nem a felületet akarja használni, hanem el akar érni valamit. Minden elem, ami nem viszi közelebb a céljához, elvonja a figyelmét attól, ami igen. A jó terv mércéje, hogy egy új ember 5 másodperc alatt megmondja: hol vagyok, mit tehetek itt, mi a következő lépés.

Öt tipikus hiba, amit ez a skill megfordít:

1. Rögtön képernyő készül, a flow tisztázása nélkül.
2. A meglévő vagy kért tartalom kérdés nélkül átkerül a tervbe: szépen elrendezve, de továbbra is fölöslegesen vagy érthetetlenül.
3. Minden elem egyforma súlyt kap, ezért semmi sem vezet.
4. Csak az ideális állapot van megtervezve.
5. A színek, szövegstílusok, betűk és ikonok menet közben, egyenként születnek, rendszer nélkül.

## Hogyan válaszolj: javaslat előre, indoklás kérésre

A megrendelő megoldást vár, nem kérdőívet és nem előadást. Miután értelmezted a kérést és fejben végigmentél a munkamenet első három lépésén, a válaszod így épül fel:

1. **Így oldanám meg.** 3-7 rövid, konkrét pont: mi kerül a képernyőre és hová, mi a fő művelet és mi a felirata, mit vonnál össze, mit tennél mélyebbre, mit hagynál ki. Kijelentő módban, döntésként.
2. **Minta.** Rögtön mutasd is meg: egy első képernyő, egy gyors vázlat vagy a kulcsrészlet kidolgozva. Inkább gyors és konkrét legyen, mint tökéletes. Nagy kérésnél (több képernyő, teljes oldal vagy app) a szerkezet vázlata és a legfontosabb képernyő az első minta.
3. **Amit kihagynék vagy áthelyeznék.** Egy sorban felsorolva, hogy semmi ne tűnjön el csendben.
4. **Kérdések, javasolt válasszal.** Legfeljebb három, csak ami tényleg befolyásolja a tervet. Mindegyikhez írd oda, mit feltételeztél a mintában.

**Az indoklást ne fejtsd ki kéretlenül.** A javaslat pontjai mellé nem jár magyarázat, kutatási hivatkozás vagy elvek felsorolása. A végén egy mondatban jelezd, hogy bármelyik döntést megindokolod, ha kérik. Ha rákérdeznek, adj rövid, konkrét indoklást arra az egy pontra. Kivétel, amikor egy félmondatnyi indoklás kéretlenül is jár: ha a javaslatod eltér attól, amit a megrendelő kifejezetten kért, ha kockázatot látsz, vagy ha valamit kihagynál.

A szöveges bejárást, a tartalmi leltárt és a tokeneket elkészíted, mert ezekből születik a javaslat, de alapértelmezésben az eredményüket mutatod meg. Kérésre bármelyiket megmutatod teljes terjedelmében.

Ha egy kérdés a terv gerincét érinti (nem tudod, kinek szól a képernyő, vagy mit csinál a fő művelet), akkor is hozz javaslatot és mintát a legvalószínűbb értelmezés alapján, de jelöld világosan, hogy feltevésre épül, és a válaszig ne dolgozd ki a további képernyőket.

## Munkamenet

Ebben a sorrendben haladj. Az első három lépés tisztán gondolati: amíg ezek nincsenek meg, ne rajzolj semmit. Nulláról induló munkánál előbb olvasd el a "Nulláról induló tervezés" fejezetet, mert az megelőzi ezt a sort.

### 1. Értsd meg a feladatot

- Ki használja, milyen szerepben és milyen helyzetben? Ha több szerep van, sorold fel külön.
- Mi az az egy dolog, amit el akar érni? Egy mondatban.
- Honnan érkezik erre a képernyőre, és hová megy tovább?
- Mi az a pillanat, amikor először értéket kap?
- Mit ismer már? Milyen más termékeket használ?
- Milyen platformra, milyen nyelven és melyik piacra készül?

Amit nem tudsz, arra tegyél feltevést, és vidd tovább a javaslatba kérdésként, javasolt válasszal.

### 2. Járd be a flow-t szövegben, terv nélkül

Mielőtt bármit rajzolnál, írd le magadnak a felhasználó útját lépésenként. Ez a száraz bejárás: a flow tesztje képernyők nélkül. Minden lépéshez:

- **Szándék**: mit akar itt a felhasználó?
- **Kérdés**: mit kell tudnia ahhoz, hogy dönteni vagy cselekedni tudjon?
- **Cselekvés**: mit tesz, és mi lesz annak az eredménye?
- **Visszajelzés**: miből tudja, hogy sikerült, és mi jön utána?

Szerepenként külön bejárást készíts, ha az útjuk eltér. A fő út után nézd meg a két-három leggyakoribb mellékutat (visszatérő felhasználó, hiba, megszakított folyamat).

A bejárás eredménye két lista: **milyen információra** és **milyen műveletre** van szükség, és melyik lépésnél. Ami egyik lépésben sem kerül elő, az gyanús.

Flow-szabályok:

- **Az első értékig vezető út legyen a legrövidebb.**
- **Az erőfeszítés számít, nem a lépésszám.** A mezők és döntések száma jobban rontja az élményt, mint a képernyők száma.
- **Egy képernyő, egy fő cél.**
- **Progressive disclosure.** Azt mutasd, ami most kell.
- **Okos alapértelmezések.** Amit a rendszer tud, azt ne kérdezd meg.
- **Mindig legyen kiút.** A visszavonás jobb, mint a megerősítő ablak.
- **Mutasd a haladást.** Ha egy elemnek életciklusa van, lássa a felhasználó, hol tart és mi a következő állomás.
- **Zárd le jól.** A siker pillanata legyen egyértelmű, és mondja meg a következő lépést.

### 3. Szűrd meg a tartalmat

Lásd a Tartalmi szűrés fejezetet. Ezután add a javaslatot és a mintát.

### 4. Döntsd el a vizuális irányt: arculat vagy új javaslat

Nem kell ragaszkodnod a meglévő anyag arculatához. Meglévő felület vagy brand esetén egyszer kérdezz rá:

- **Marad az arculat**: csak a hierarchia és az elrendezés javul.
- **Finomított arculat**: a felismerhető elemek maradnak, a színrendszert és a szövegstílusokat újraépíted köréjük.
- **Új javaslat**: saját vizuális irányt hozol. Ilyenkor is kérdezd meg, van-e elem, aminek maradnia kell (például a betűtípus vagy a logó).

Ez a kérdés a javaslat kérdései közé tartozik, javasolt válasszal. Ha a meglévő arculatban színjelentési ütközést látsz (például piros a fő cselekvés színe), jelezd egy mondatban. Ha a felhasználó már megmondta, melyiket kéri, ne kérdezd újra.

Saját javaslatnál az irány a témából jöjjön. Egy mondatban nevezd meg a karaktert, és minden későbbi döntés ehhez igazodjon.

### 5. Építsd fel a struktúrát

- A navigáció a felhasználó fejében élő felosztást kövesse, ne a szervezeti ábrát.
- Felső szinten 5-7 elemnél több ritkán indokolt.
- Használd a megszokott mintákat. Újítani ott érdemes, ahol az a termék lényege.
- A felhasználó mindig tudja, hol van.

### 6. Állítsd fel a rendszert, mielőtt rajzolsz

Rögzítsd a tokeneket: színszerepek, betűtípus és szövegstílusok, ikonkészlet, térközskála, lekerekítések, felületszintek. A színeket a `scripts/palette.py` számolja ki (lásd Színharmónia). A terv ezután kizárólag ezekből építkezik.

### 7. Tervezd meg a képernyőt

Rangsorold a szűrésen átment elemeket. A rangsor a bejárásból jön: ami a fő út legtöbb lépésében kell, az van elöl.

### 8. Tervezd meg az összes állapotot

Lásd az Állapotok fejezetet.

### 9. Ellenőrizd: fordított bejárás és vizuális próbák

Lásd a fájl végén.

## Nulláról induló tervezés

Ha nincs meglévő felület, a munkamenet elé négy alapozó döntés kerül. Ezekre is javaslatot hozol, nem kérdéssort: ha a megrendelő csak annyit mondott, "kell egy weboldal egy kávézónak", te mondod meg, milyen oldalak, milyen fő cél és milyen hang lenne jó, és ő javít rajta.

### Alapozás

1. **Cél és mérce.** Egy fő üzleti cél (ajánlatkérés, vásárlás, foglalás, regisztráció, napi használat) és egy-két mérőszám, amiből látszik, hogy működik. Minden későbbi döntés ezt szolgálja.
2. **Közönség és fő feladatok.** Kik jönnek, és mi az a 3-5 dolog, amiért jönnek. A látogatók többsége néhány fő feladatért érkezik: ezek kapják a legjobb helyet, a többi nem versenyezhet velük.
3. **Tartalom előbb, forma utána.** A terv valódi szövegre, kínálatra, árakra és képekre épüljön. Ha nincs tartalom, írj valószerű vázlatot és jelöld, mi a helyőrző (például [ÁR], [ÜGYFÉLVÉLEMÉNY]). Kitalált statisztika, ajánlás vagy ügyféllogó nem kerülhet a tervbe.
4. **Terjedelem.** Mi kell az első verzióba, és mi nem. Mondd ki, mit hagynál későbbre: a kisebb, kész termék jobb, mint a nagy, félkész.

Mindig nézd meg, mit szoktak meg a felhasználók a hasonló termékeknél (2-3 minta elég): a bevett mintáktól csak okkal térj el.

### Szerkezet

- **Weboldal**: oldaltérkép (melyik oldal mire való, oldalanként egy cél), navigáció, és oldalanként a szekciók sorrendje.
- **App**: a fő objektumok (amikkel a felhasználó dolgozik: feladat, rendelés, ügyfél), ezek kapcsolatai és a rajtuk végezhető műveletek. Ebből jön a képernyőlista (lista, adatlap, létrehozás, beállítás) és a navigáció. Ugyanaz az objektum mindenhol ugyanazzal a névvel és megjelenéssel szerepel.
- A 3-5 fő feladat mindegyikére készíts szöveges bejárást (Munkamenet 2. lépés).
- Építs kis komponenskészletet a tokenekből (gomb, mező, lista, kártya, navigáció, modál, értesítés, üres állapot), és minden képernyő ebből álljon össze. Így az első képernyő döntései az összes többire érvényesek.

### Weboldal: ami kötelező

- **Az első képernyő három kérdésre válaszol 5 másodperc alatt**: mi ez, kinek szól, mit tegyek. Egy világos értékajánlat a látogató szavaival, egy fő cselekvés.
- **A szekciók sorrendje a látogató kérdéseit követi**: mi ez → miért jó nekem → hogyan működik → miért higgyem el → mennyibe kerül → mit tegyek most. Ami egyik kérdésre sem válaszol, az kimarad.
- **Egy oldal, egy cél, egy fő cselekvés**, ami hosszabb oldalon többször is megjelenik, azonos felirattal.
- **Bizalmi elemek csak valódiak**: ügyfélvélemény névvel, konkrét eredmény, referencia, garancia, elérhetőség.
- **Az ár és a feltételek látszódjanak**, ahol a döntéshez kellenek. Rejtett költség nincs.
- **Navigáció**: kevés pont, a látogató szavaival; a logó a kezdőlapra visz; mobilon is elérhető a fő cselekvés. A láblécben elérhetőség és jogi oldalak.
- **Űrlap**: csak ami az első lépéshez kell, és utána egyértelmű visszaigazolás arról, mi történik ezután.
- **Reszponzív**: mobilról indulva tervezz, mert a látogatók nagy része telefonról jön. Add meg, mi történik az elrendezéssel telefonon, táblagépen és asztali gépen.
- **Sebesség** (Core Web Vitals): a legnagyobb tartalmi elem 2,5 mp-en belül jelenjen meg (LCP), az interakcióra adott válasz 200 ms alatt legyen (INP), az elrendezés ne ugráljon betöltéskor (CLS 0,1 alatt). Ez tervezési döntés is: méretezett képek, lefoglalt hely a később betöltő elemeknek, kevés betűfájl, nincs nehéz animáció az első képernyőn.
- **Kereshetőség**: oldalanként egy főcím (h1), logikus címsorszintek, beszédes oldalcím és leírás, beszédes linkszöveg (nem "kattints ide"), alternatív szöveg a képekhez.
- **Jogi és megfelelési elemek** (ezek "Kötelező" besorolásúak, de a megrendelővel erősítsd meg, melyik vonatkozik rá): az EU-ban sütihozzájárulás, ahol az elutasítás ugyanolyan könnyű, mint az elfogadás; adatkezelési tájékoztató; cégadatok; webshopnál általános szerződési feltételek és elállási tájékoztatás. Fogyasztóknak szóló szolgáltatásnál az akadálymentesség (WCAG 2.2 AA) az EU-ban jogi elvárás is lehet. Jogi szöveget ne te írj: jelöld a helyét.
- **Kiegészítő oldalak**: 404, üres keresési találat, űrlap sikeres elküldése, karbantartás.
- **Mérés**: a fő célhoz tartozó esemény (például elküldött ajánlatkérés) legyen mérhető.
- **Többnyelvűség**, ha kell: a szöveg más nyelven akár 30-40%-kal hosszabb lehet, a felület ezt bírja el.

### App: ami kötelező

- **Platformkonvenciók**: iOS-en és Androidon a rendszer navigációját, gesztusait, visszalépését és komponenseit kövesd. Webappnál az asztali szokásokat (billentyűzet, több ablak, jobb klikk).
- **Navigáció**: mobilon 3-5 fő terület alsó fülsávban, felirattal; asztali gépen oldalsáv. A leggyakoribb művelet egy érintéssel elérhető.
- **Első indítás**: érték előbb, fiók és beállítás utána. Hosszú bemutató helyett az első valódi feladat elvégzése a bevezetés. Üres állapotok mintaadattal vagy első lépéssel.
- **Engedélykérés** (értesítés, helyadat, kamera) abban a pillanatban, amikor a haszna nyilvánvaló, előtte egy mondat arról, mire kell.
- **Értesítések**: csak ami a felhasználónak fontos, típusonként kikapcsolható.
- **Hálózat és adat**: mi látszik offline, mi történik megszakadó kapcsolatnál, a beírt adat nem veszhet el (automatikus mentés vagy vázlat).
- **Eszközök és beállítások**: biztonságos zónák (kivágás, alsó sáv), sötét mód, a rendszer nagyított betűmérete, fekvő nézet és táblagép, ha releváns.
- **Gesztusok**: minden gesztusnak legyen látható alternatívája (húzás helyett gomb).
- **Fiók**: kijelentkezés, adatok exportálása és fiók törlése elérhető; a törlés ugyanolyan könnyű, mint a regisztráció.

### Mit mutass először nulláról induló munkánál

Az első válaszod: a fő cél egy mondatban, a szerkezet (oldaltérkép vagy képernyőlista) röviden, a vizuális irány egy mondatban, és mintaként a legfontosabb képernyő (weboldalnál a kezdőlap első képernyője és szekciósorrendje, appnál a fő feladat képernyője). A többi képernyőt akkor dolgozd ki, amikor az irányra rábólintottak.

## Tartalmi szűrés

A fölösleges információ nem ártalmatlan: minden elem, ami nem szolgál célt, elveszi a figyelmet attól, ami igen. Ezért a meglévő felület elemei és a megrendelő kérései sem kerülnek be automatikusan a tervbe. Mindegyiknek igazolnia kell a helyét. Ugyanez igaz arra is, amit te magad tennél hozzá.

### Tartalmi leltár

Vedd sorra a képernyő minden elemét: adatmező, felirat, gomb, link, szekció, segédszöveg. Minden elemre válaszolj:

1. **Melyik lépést szolgálja** a bejárásból?
2. **Kinek szól**, és milyen gyakran kell neki?
3. **Mi történne, ha nem lenne ott?** Ha senki nem venné észre, fölösleges.
4. **Érthető-e önmagában?** Egy új felhasználó tudná, mit jelent, és mi történik, ha rákattint?

### Besorolás

| Kategória | Mit jelent | Mi történik vele |
|---|---|---|
| **Kötelező** | Üzleti, jogi vagy folyamatbeli okból ott kell lennie, akkor is, ha a felhasználó fő útját nem szolgálja | Marad. Olyan helyre és súllyal, ami megfelel a valódi gyakoriságának. |
| **Szükséges** | A fő út valamelyik lépését szolgálja | Marad, a rangsor szerint elöl. |
| **Feltételes** | Csak bizonyos szerepnek, állapotban vagy esetben kell | Csak akkor és annak jelenik meg, vagy egy szinttel mélyebbre kerül. |
| **Fölösleges** | Egyik lépést sem szolgálja, ismétel valamit, vagy a rendszer belső ügye | Kimarad, és felsorolod a kihagyottak között. |
| **Tisztázandó** | Nem tudod eldönteni, mert nem ismered a folyamatot vagy az elem célját | Kérdés a megrendelőnek, javasolt válasszal. Addig halkan a helyén marad. |

- **A "Kötelező" címkét a megrendelő adja, nem te.** Te csak jelölheted, hogy valami valószínűleg kötelező. Ha a megrendelő azt mondja, hogy egy elemnek ott kell lennie bizonyos esetekben, az nem vita tárgya: a feladatod az, hogy jó helyre, jó feltétellel és érthető felirattal kerüljön.
- **A kötelező nem jelent kiemeltet.**
- **Ne törölj csendben.** Amit kihagynál vagy áthelyeznél, azt mindig sorold fel.
- **Ne találj ki jelentést.** Ha egy felirat vagy mező célja nem derül ki, ne írd át szebbre találgatás alapján.
- **Ne adj hozzá saját ötletből** olyan elemet, amit a bejárás nem indokol. Ha valami hiányzik a flow-ból, javasold külön, jelölve, hogy a te javaslatod.

### Tipikus fölösleges tartalom

- **Rendszer-belső információ**: honnan importálták az adatot, belső azonosító, technikai állapot.
- **Ismétlés**: ugyanaz az adat két helyen.
- **Üres váz**: 0 elemű szekciók, kitöltetlen mezők teljes méretben.
- **Soha nem változó érték.**
- **Magyarázó szöveg állandóan.**
- **"Hátha kell valakinek" funkció.**
- **Összesítő, amit senki nem olvas.**
- Weboldalon: általános üdvözlőszöveg, cégtörténet a kezdőlap tetején, képváltó több üzenettel, díszítő stockfotó, közösségi ikonok a fejlécben.

### Feliratok és műveletek érthetőségi próbája

Minden interaktív elemre tedd fel a négy kérdést:

1. A felhasználó ebben a lépésben egyáltalán ezt akarja-e elérni?
2. Észreveszi-e, hogy a művelet elérhető?
3. A feliratból tudja-e, hogy ez az, amit keres, és mi lesz a következménye?
4. A művelet után látja-e, hogy sikerült?

A gombfelirat mondja ki az eredményt, ne a szándékot vagy egy belső fogalmat ("Tovább" helyett "Foglalás elküldése"). Ha egy műveletnek mellékhatása van (értesítés megy valakinek, elindul egy előfizetés), az derüljön ki a feliratból vagy közvetlenül mellette. Ha te magad sem tudod megmondani, pontosan mi történik a kattintás után, az tisztázandó.

### Kérések felülvizsgálata

Amikor a megrendelő azt kéri, hogy valami kerüljön fel egy felületre, a kérést is vesd össze a bejárással:

- Ha a kérés egy lépést szolgál, tedd be a megfelelő súllyal.
- Ha nem illeszkedik egyik lépéshez sem, ne hagyd ki és ne is tedd be szó nélkül. Mondd el egy mondatban, miért nem látod a helyét, és rögtön hozz javaslatot (más képernyő, feltételes megjelenés, mélyebb szint).
- Ha a válasz az, hogy kötelező, fogadd el, és tervezd meg jól.
- Ha a kérés ellentmond egy korábbi döntésnek vagy önmagának, jelezd, mielőtt építesz rá.

### Önellenőrzés

A saját tervedre ugyanez a szűrő vonatkozik. Átadás előtt jelöld meg azokat az elemeket, amiket csak azért hagytál benne, mert az eredetiben ott voltak, vagy mert te találtad ki. Ezeket igazold a bejárással, vedd ki, vagy tedd a kérdések közé. Ha nem ismered a teljes rendszert, mondd ki, mely döntéseid feltevések.

## Elrendezés és hierarchia

- Ami a feladat közepe, az legyen fókuszban. Ami tájékozódást és navigációt szolgál, az húzódjon háttérbe.
- Képernyőnként egy primary action, és az a legfeltűnőbb elem.
- **Kiemelni halkítással lehet.** Ha a fontos elem nem ugrik ki, azt halkítsd, ami versenyez vele.
- Ami összetartozik, legyen közel. A csoporton belüli térköz legalább kétszer kisebb, mint a csoportok közötti.
- Előbb térközzel válassz szét, aztán háttérszínnel, és csak végül vonallal vagy kerettel.
- Egyetlen térközskála (például 4, 8, 12, 16, 24, 32, 48, 64). Igazíts közös élekre.
- Érintési célpont: a WCAG-minimum 24x24 CSS px, de asztali gépen 32-40 px a cél, érintőképernyőn 44-48 px. Romboló művelet nem kerül a leggyakoribb mellé.

**Felületek és mélység.**

- Legfeljebb három felületszint: alap, kiemelt, lebegő. A szintet háttérárnyalat VAGY árnyék VAGY keret jelzi.
- Kártyát csak akkor használj, ha a tartalom önálló egység.
- Egy lekerekítési rendszer (például 6 / 10 / 16). Beágyazott elem sugara = külső sugár mínusz a belső margó.
- A formák egy nyelvet beszéljenek: betű, ikonok, sarkok, vonalvastagságok.

**Gombhierarchia.** Négy szint, és egy nézetben a legmagasabb szintből csak egy lehet:

1. Tömör (akcentusszín): a képernyő fő művelete.
2. Lágy vagy keretes: fontos másodlagos művelet.
3. Szellem: gyakori, de nem kiemelt műveletek.
4. Link: szövegközi navigáció.

## Színrendszer

A szín a hierarchia és a flow eszköze, nem díszítés. Ne színeket válassz, hanem szerepeket tölts be: minden színnek egy feladata van, és egy feladathoz egy szín tartozik.

### A színek jelentése

| Szín | Bevett jelentés a felületen | Mire használd | Mire ne |
|---|---|---|---|
| Piros | hiba, veszély, megállás, visszafordíthatatlan művelet | hibaüzenet, törlés, lejárt határidő, kritikus riasztás | fő cselekvés, link, navigáció, díszítés, nagy felület |
| Narancs | komoly figyelmeztetés, javítható hiba | közelgő határidő, kockázat | siker, semleges információ |
| Sárga, borosztyán | figyelem, óvatosan | nem blokkoló figyelmeztetés, függőben | szöveg színeként világos alapon |
| Zöld | siker, kész, mehet | megerősítés, kész állapot, érvényes mező | romboló művelet, hiba |
| Kék | semleges információ, interakció, megbízhatóság | link, fő cselekvés, tájékoztató üzenet | veszély jelzése |
| Lila, indigó | nincs erős státuszjelentése | akcentus, márka, kiemelés | (szabadon használható) |
| Szürke | semleges, inaktív, másodlagos | letiltott állapot, vázlat, háttér | fontos, élő tartalom |

**A pirosról külön.**

- A piros gyorsan vonzza a tekintetet, de teljesítményhelyzetben a kudarc veszélyét idézi és elkerülő viselkedést vált ki. Munkaeszközben az állandóan jelen lévő piros feszültséget kelt és elkoptatja a valódi riasztások erejét.
- A piros ne legyen a "tovább", "mentés", "indítás" típusú fő cselekvés színe.
- **Piros márkaszín esetén** a márkapiros maradjon a logóban és a márkapillanatokban, kis felületen. A cselekvés színe legyen más, a hibáé pedig a márkapirostól láthatóan eltérő árnyalat, ikonnal és szöveggel megerősítve.
- **Nincs "legjobban konvertáló gombszín".** Az a gomb nyer, amelyik elüt a környezetétől.

**A jelentés a környezettől függ.** Kultúránként eltér (a piros nyugaton hiba és veszély, Kínában szerencse és öröm), szakterületenként is (pénzügyben a piros veszteség). Nemzetközi terméknél nézz utána a célpiacnak. Ugyanaz a szín a terméken belül egyet jelentsen.

### A paletta felépítése

**1. Semleges skála.** Készíts 10-12 lépcsős szürkeskálát, és minden lépcsőnek adj szerepet. Három-négy szürke mindig kevés.

| Lépcső | Szerep |
|---|---|
| 1 | alkalmazás háttere |
| 2 | halk háttér (oldalsáv, sávozott sor) |
| 3 | komponens háttere |
| 4 | hover |
| 5 | lenyomott, kiválasztott |
| 6 | halk elválasztó |
| 7 | interaktív elem kerete |
| 8 | erős keret, fókuszgyűrű |
| 9-10 | tömör háttér és annak hovere |
| 11 | másodlagos szöveg |
| 12 | elsődleges szöveg |

A szürkét színezd enyhén az akcentus felé (pontos szabály: Színharmónia). A legsötétebb szöveg ne legyen tiszta fekete. A skála sok lépcsője nem jelent sok színezett felületet: egy képernyőn általában egy halvány felületlépcső és egy-két keretlépcső dolgozik.

**2. Egy akcentusszín, ugyanilyen skálával.** A tömör lépcső a fő műveleté, a világos lépcsők a kiválasztott és aktív állapotoké, a sötét lépcső a színes szövegé. Olyan árnyalatot válassz, aminek nincs státuszjelentése a termékben.

**3. Jelentésszínek.** Siker, figyelmeztetés, hiba és rombolás, információ. Mindegyikből három lépcső: halvány háttér, keret, sötét szöveg.

**4. Kategóriaszínek, ha kellenek.** Legfeljebb 5-6, azonos világossággal és telítettséggel, egymástól legalább kb. 40 fokra. Ne essenek egybe a jelentésszínekkel és az akcentussal (attól legalább 30 fok). Ha több kellene, vonj össze kategóriákat, vagy jelöld forma és felirat segítségével.

### Számolás, arányok, szabályok

- A skálákat OKLCH-ban építsd: ott az azonos L érték különböző árnyalatoknál is azonos érzékelt világosságot ad.
- Minden szöveg-háttér pár kontrasztját számold ki. Törzsszöveg legalább 4,5:1, nagy szöveg és nem szöveges elem legalább 3:1.
- Nagyjából 60% alapfelület, 30% másodlagos felület és szöveg, legfeljebb 10% akcentus.
- A tömör akcentus egy nézetben egy elemen jelenik meg: a fő műveleten.
- A linknek aláhúzás vagy saját szín jár, a sima szöveg soha nem akcentusszínű.
- A szín soha ne egyedül hordozza a jelentést: adj mellé ikont, szöveget vagy formát.
- Színes háttéren a háttér színének sötét vagy világos változata legyen a szöveg, ne szürke.
- Sötét módban a felületek világosodással emelkednek, a telítettség csökken.

### Mit csinálnak a legjobb termékek a színnel

Linear, GitHub (Primer), Atlassian és Material 3 közös mintája:

- **A felület szinte színnélküli.** Szürkeárnyalatos keret, egy akcentus, és szín csak ott, ahol funkciója van. A Linear egyik felületfrissítése kifejezetten csökkentette az ikonokat és elhagyta a színes ikonháttereket.
- **A szín szerepet tölt be, nem árnyalatot választasz.** Primer: accent = interaktív szöveg és ikon; success, attention, danger = jelentés. Atlassian: díszítő színt ne használj ott, ahol a színnek jelentése van; próbaként kérdezd meg, lecserélhető-e a szín egy másikra anélkül, hogy a jelentés változna.
- **Hangsúlyszintek egy színen belül**: legfinomabb, finom, erős háttér; a szöveg és az ikon ugyanabból a színből jön, mint a háttere.
- **Állapotnak kategória szerint jár szín, nem egyenként.** A Jira három kategóriára (teendő, folyamatban, kész) szűkítette a státuszszíneket; a Linear kategóriákba sorolja az állapotokat, és alakkal jelöli őket.
- **Az élénk szín elviszi a tekintetet**, ezért az akcentus és a figyelmeztető színek mennyiségével takarékoskodni kell (Material 3).

### Állapot színezése listában, naptárban, táblán

- **Listában az állapotot alak és felirat mutatja, semleges színnel**: szaggatott kör = el sem kezdődött, részben kitöltött kör = halad, pipa = kész. Ez csak akkor működik, ha az állapotok sorrendben követik egymást; ha nem, maradjon a felirat.
- **Színt csak az kap, ami beavatkozást kér**: figyelmeztetés (beragadt, hamarosan lejár) és hiba (késik, blokkolt). Így egy pillantással kiderül, hol kell tenni valamit.
- **Naptárban és táblán**, ahol a sáv színe az egyetlen gyors jel, állapotkategóriánként egy árnyalat jár (legfeljebb 4-5), az akcentustól távol. Ugyanaz a kategória minden nézetben ugyanazt a színt kapja.
- **A csoportcím színezetlen.** Ha a sorokban már ott a piros dátum, a „Késésben” cím ne legyen piros is: egy jelentés, egy jel.
- **Soronként ismétlődő művelet semleges**, az akcentus csak rávitelkor jelenik meg. Tizenöt színes „Szerkesztés” gomb elnyomja a sorok tartalmát és elkoptatja az akcentust.
- **Új, olvasatlan elemek**: egy elválasztó jelöli, honnan kezdődik az újdonság („4 új üzenet”), mellette elemenként egy kis pötty. Nem kap minden elem színes keretet: négy rikító keret egymás alatt zajt csap, és nem mondja meg, hol a határ.
- **Említés (@név) akcentusszínű szöveg**, mert kattintható; nem színes doboz.

### Alapértelmezett vizuális nyelv: visszafogott, egy színnel

Ha a megrendelő nem kér mást, ebből indulj. A hangsúlyt a méret, a súly és a térköz adja.

- **Fehér munkafelület, egyetlen halvány semleges a másodlagos zónáknak** (oldalsáv, mellékpanel, műveletsáv). A halvány panelen a tartalom fehér kártyán ül, a fehér felületen nincs kártya, csak térköz és egy-egy hajszálvonal.
- **Az akcentus két formája, két szerep:** tömören a nézet egyetlen fő műveletén (a következő lépés); szövegszínként azon, ami kattintható szöveg (link, említés, „+ Érték megadása”). Halvány változata a másodlagos megerősítő gomb és a kiválasztott állapot háttere.
- **A fő művelet egy helyen, egy sávban:** az állapot, a haladás és a következő lépés gombja egy halvány sávban a cím alatt. A másodlagos gomb fehér, kerettel; a harmadlagos keret nélküli szöveg.
- **Rangsor szürkével:** a cím a legsötétebb és legnagyobb, az érték középerős, a címke és a metaadat kicsi és szürke, kis vonalas ikonnal.
- **Ami nem kattintható és nem jelez beavatkozást, az nem színes.** Kivétel a személy azonosítása: az avatar halvány pasztell, személyenként állandó, sötét betűvel, sosem tömör vagy fekete.
- **Üres mező nem doboz:** hiányzó értéknél akcentusszínű szöveges művelet áll, nem szaggatott keret és nem „–”.

### Színharmónia: a palettát számold, ne válogasd

A színek attól passzolnak, hogy közös szabályból születnek. Szemre válogatott hexkódokból nem lesz rendszer.

- **Előbb a paletta, utána a képernyő.** Az összes színt és a párok kontrasztját a skill mappájában lévő `scripts/palette.py` számolja OKLCH-ból (csak Python 3 kell, telepíteni semmit nem kell; a parancsokat a skill mappájából futtasd, vagy add meg a szkript teljes útvonalát):
  - `python3 scripts/palette.py generate --accent "#4F46E5"`: a teljes világos paletta szerepekkel és kontrasztjelentéssel. `--format css` CSS-változókat, `--format json` gépi formát ad, `--categories N` kategóriaszíneket is számol.
  - `python3 scripts/palette.py contrast "#575667" "#F0EFF8"`: egy szöveg-háttér pár ellenőrzése.
  - `python3 scripts/palette.py audit --palette palette.json <fájlok vagy mappák>`: a palettán kívüli színkódok és a tiszta fekete listája.

  Meglévő arculat akcentusával is futtasd. Ha a szkript figyelmeztet (például az akcentus túl közel esik egy jelentésszínhez, vagy a fehér felirat nem olvasható rajta), azt vidd a javaslatba. Ha a környezetben nem futtatható Python, ugyanezeket a szabályokat számold végig kézzel.
- **Az akcentus családja: a világos lépcsők fordulnak.** A szem a világos és a sötét változatot azonos számérték mellett nem azonos árnyalatnak látja. Kék-lila akcentusnál (OKLCH H 260-290) a halvány lépcsőket (L 0,85 fölött) fordítsd kb. 10-15 fokkal a lila felé, a sötét szövegszín maradjon az akcentus H-ján. Más akcentusnál is nézd meg egymás mellett a tömör, a halvány és a sötét változatot: egy családnak kell látszaniuk.
- **Egy semleges skála, a halvány akcentus-lépcsőhöz hangolva** (H = a halvány lépcső H-ja, C 0,005-0,04), csak a világosság változik. Hideg és meleg szürke együtt mindig idegenül hat.
- **Ami színes, az látsszon.** Kiinduló értékek fehér alapon: halvány panel L kb. 0,955 (C 0,01); halvány akcentus-felület L 0,86-0,88, C 0,07-0,09; avatar L kb. 0,85. Annál halványabb színezett felület csak ráközelítve válik el a fehértől. Pötty, vékony él és ikon a telített lépcsőt kapja.
- **Példa** (a `generate --accent "#4F46E5"` kimenetéből): akcentus #4F46E5, hover #4433D3, sötét akcentusszöveg #3E27C9, halvány gomb #D2CEFF; semlegesek #F0EFF8 / #DFDEE9 / #D7D6E2 / #C8C7D4 / #575667 / #1A1828; hiba szöveg #AF3D36; figyelmeztetés szöveg #8D5E00, ikon #D76F00.
- **Azonos szerep, azonos L és C.** A kategóriaszínek halvány háttere, éle és sötét szövege szerepenként azonos világosságú és telítettségű, csak a színezet tér el.
- **Nincs tiszta fekete elem a színes akcentus mellett.** Haladássáv, kitöltött ikon az akcentust vagy a semleges skála sötét lépcsőjét kapja.
- **Sárga helyett narancs.** Kontrasztra sötétítve a sárga barnás lesz (Atlassian), ezért a figyelmeztetés ikonja narancs felé hajló borostyán.
- **Ha a megrendelő egy korábbi változatot jónak mond, mérd meg, és pontosan állítsd vissza.** A képernyőfotó pixelei a monitor színprofiljában vannak: előbb a beágyazott ICC-profilból konvertáld sRGB-be (Pillow ImageCms), csak utána mintavételezz. Ha van böngésző a környezetben, renderelj, és tedd a saját verziódat a fotó mellé, mielőtt átadod.

### A szín mint a flow segítője

- **A tömör akcentus a következő lépést jelöli**, az akcentusszínű szöveg azt, ami kattintható. Másra nem használod.
- **Az állapot látszódjon**: kész, folyamatban, hátralévő; kiválasztott; olvasatlan.
- **A figyelemnek költségvetése van.** Egy nézetben egy dolog kérhet azonnali figyelmet.
- **A romboló szín a rombolás pillanatában jelenik meg**, nem állandóan.
- **A szín tájékozódási pont lehet**, ha mindenhol ugyanazt jelöli.

## Betűtípus

Két szerepet válassz szét: a **felületi betű** dolgozik (címkék, gombok, adatok, törzsszöveg), a **címbetű** adja a karaktert. Sokszor egy család mindkettőt ellátja. Ha a megrendelőnek van betűtípusa, azt használd, és az alábbi próbákkal ellenőrizd.

### Mitől jó egy felületi betű

- **Nagy x-magasság**: kis méretben is olvasható.
- **Nyitott formák**: a c, e, a, s nyílásai nem záródnak be.
- **Megkülönböztethető karakterek**: Il1 O0 rn m szétválik.
- **Kissé széles arányok és egyenletes ritmus.**
- **Elég változat**: legalább 400, 500, 600 vastagság, táblázatos számjegyek.
- **Nyelvi lefedettség**: magyarnál a hosszú ő és ű a próba (Árvíztűrő tükörfúrógép).
- **Megjelenítés**: Windows-on és alacsony felbontáson is tiszta marad-e 12-14 px-en.

### Formavilág

| Típus | Karakter | Mire jó | Mire figyelj |
|---|---|---|---|
| Humanista groteszk | meleg, emberi | felületi szöveg, kis méret | a legbiztosabb sűrű felületre |
| Neo-groteszk | semleges, tárgyilagos | általános felület | zárt formák kis méretben romlanak; könnyen jellegtelen |
| Geometrikus groteszk | modern, barátságos | címsor, rövid feliratok | az a, o, e hasonlít; hosszú szövegben fárasztó |
| Antikva (talpas) | szerkesztőségi, megbízható | címsor, olvasnivaló | sűrű vezérlőkben ritkán jó |
| Slab | erős, technikai | kiemelés, címsor | takarékosan |
| Monospace | pontos, gépi | kód, azonosító, számoszlop | folyószövegre nem |

Ne nyúlj reflexből ugyanahhoz az egy semleges betűhöz minden tervnél. Natív alkalmazásnál a rendszerbetű teljes értékű választás.

### Párosítás és szedés

- **Az alapértelmezés egy család.** Második betű csak akkor jön, ha szerepe van. Kettő plusz egy mono a felső határ.
- **Kontraszt vagy egyezés, de ne hasonlóság.** Két majdnem egyforma betű hibának látszik.
- **Ami közös legyen**: hasonló x-magasság, arányok és hangulat. **Egy főnök van.**
- **A legbiztosabb párosítás a szupercsalád.** A szerepek ne keveredjenek.
- Nagy címsor: szűkebb betűköz (kb. -1 és -2% között) és sortáv (1,1-1,3). Kis nagybetűs felirat: tágabb betűköz. Kisbetűs törzsszöveg betűközét ne állítsd.
- Táblázatban, számlálóban, összegeknél táblázatos számjegyek.
- 400 alatti vastagság felületen nincs. Hamis félkövér és dőlt nincs.
- Sorhossz 45-75 karakter, balra zárt szedés. Hosszabb olvasnivaló (cikk, leírás) legalább 16 px; sűrű felületen az adat és a rövid szöveg 14-15 px.

## Szöveghierarchia és feliratok

| Szerep | Mire való | Jellemző megjelenés |
|---|---|---|
| Oldalcím | a nézet neve, egy van belőle | 24-32 px (weboldal főcíme nagyobb is lehet), 600-700, elsődleges szín |
| Szekciócím | tartalmi blokkok neve | 16-18 px, 600, elsődleges szín |
| Törzs és érték | olvasandó tartalom, adatérték | 14-16 px, 400-500, elsődleges szín |
| Címke | mező vagy adat neve | 12-13 px, 500, másodlagos szín |
| Meta | időbélyeg, számláló, segédszöveg | 12-13 px, 400, másodlagos szín |
| Vezérlő | gomb, fül, menüpont felirata | 13-15 px, 500-600 |

- **Két szomszédos szint legalább két tulajdonságban térjen el.** A méretlépcsők között legalább 1,2-szeres arány legyen.
- **A szekciócím nem címke.** Fölötte nagyobb térköz van, mint alatta.
- **Címke és érték párnál az érték a fontos.** Ahol az érték magáért beszél, a címke el is hagyható.
- **Három semleges szövegszín elég**: elsődleges, másodlagos, letiltott. Ezen felül csak szerepszín írhat szöveget: link (akcentus), hiba, figyelmeztetés. A másodlagos színű szöveg ne legyen többségben.
- **Vastagság**: 400 és 500 a szövegre, 600-700 a kiemelésre.
- **Nagybetűs címke** csak rövid felirathoz, növelt betűközzel, egyetlen szerepre.
- 4-6 betűméret elég egy teljes termékhez.

## Ikonok

Minél értelmezhetőbb egy ikon, annál többet egyszerűsít a felületen. Egy félreérthető ikon viszont rosszabb, mint ha nem lenne.

- **Kevés ikon egyetemes**: kezdőlap, keresés, nyomtatás, bezárás, kosár. A többi jelentése a környezettől függ.
- **Az ikon mellé felirat jár, és mindig látszik**, nem hoverre. Navigációban kötelező.
- **Csak ikon akkor maradhat**, ha egyetemes; vagy naponta sokszor használt, szűk eszköztár része (tooltip és aria-label kell); vagy minden sorban ismétlődő művelet.
- **Háromféle ikon van**, csökkenő érthetőséggel: hasonlósági, utaló (metafora) és önkényes. Válaszd a legközvetlenebbet, a konvenciót ne írd felül.
- **Egy ikon, egy jelentés; egy jelentés, egy ikon.** Figyelj a kétértelműekre (óra, harang, zászló, szem, ceruza).
- **5 másodperces szabály**: ha ennyi idő alatt nem jut eszedbe egyértelmű ikon, használj szöveget.
- Az ikon ott segít, ahol megkülönböztet, eltérő sziluettel. Ha minden sor előtt hasonló ikon áll, egyik sem segít. Ne díszíts ikonnal minden címsort, gombot és menüpontot.
- **Státuszikonok** formában is térjenek el (pipa, háromszög, nyolcszög). **Irányjelek** következetesek: lefelé lenyitás, jobbra továbblépés, ferde nyíl külső hivatkozás. Emoji nem ikon.
- **Egy készlet**, azonos rács, vonalvastagság (1,5-2 px), sarok és vonalvég, a szöveg vastagságához illesztve.
- **Méretek**: 16 px szöveg mellett, 20 px gombban, 24 px önállóan. A kattintható terület asztali gépen 32-40 px, érintőképernyőn 44-48 px.
- **Kitöltött és körvonalas**: egy alapstílus; a kitöltés állapotjelzésre való.
- Az ikon a szöveg színét veszi fel, a felirat előtt, 6-8 px távolságra. Csak ikonos gombnak aria-label, díszítő ikonnak aria-hidden.

## Állapotok

- **Üres**: magyarázat és egy gomb az első lépéshez. Több üres szekció egy összevont "hozzáadás" sorrá olvadhat.
- **Betöltés**: az elrendezést tükröző skeleton.
- **Részleges**: kevés adat, egyetlen elem, nagyon hosszú szöveg, hiányzó kép.
- **Ideális**: valószerű tartalommal, ne lorem ipsummal.
- **Hiba**: mi történt, miért, mit tehet most. A beírt adat ne vesszen el.
- **Siker**: egyértelmű visszajelzés és a következő lépés.
- **Interakciós állapotok**: alap, hover, fókusz, lenyomott, kiválasztott, letiltott, betöltő.
- **Szélsőségek**: offline, lejárt munkamenet, jogosultság hiánya, 0 találat.

## Űrlapok és mikroszöveg

- Minden mezőnél kérdezd meg: tényleg kell ez most?
- Egy oszlop, a címke a mező fölött és mindig látható. A placeholder nem címke.
- Megtekintésre szolgáló adat olvasható értékként jelenjen meg, és kattintásra váljon szerkeszthetővé. Egy adatlap ne nézzen ki kitöltendő űrlapnak: a dátum emberi formában („holnap, péntek 12:30”), alatta a pontos dátum, az üres mező helyett „+ … megadása”.
- Ritkán használt beállítás a szerkesztés pillanatában jelenjen meg, ne állandóan.
- Az üzenetmező segédszövege rövid („Enter: küldés”); a további funkciókat (említés, csatolás) gomb mutassa, ne mondat.
- Validálj a mező elhagyásakor. A hibaüzenet a mező mellett jelenik meg, megmondja a javítást.
- Engedékeny bevitel, és semmit ne kérj be kétszer.
- A gomb igével mondja meg, mi történik, és az eredményt nevezi meg: Mentés, Fizetés 4 990 Ft, Projekt törlése.
- Hibaüzenet emberi nyelven, megoldással.
- Ugyanaz a dolog mindenhol ugyanazt a nevet kapja. Rövid, konkrét, zsargon és belső fogalmak nélkül.

## Válaszidő, mozgás, akadálymentesség, platform

- 0,1 mp alatt azonnalinak hat. 1 mp fölött betöltési állapot, 10 mp közelében haladásjelző és megszakítási lehetőség.
- A mozgás magyarázzon, 150-300 ms. Tartsd tiszteletben a csökkentett mozgás beállítást.
- Minden elérhető billentyűzetről, logikus sorrendben, jól látható fókuszjelzővel. Húzás helyett legyen kattintásos alternatíva.
- Valódi gombok és linkek, szöveges alternatíva képekhez és ikon gombokhoz. Használható 200%-os nagyításnál is.
- Semmi fontos ne függjön kizárólag a hovertől.
- Sűrű, profi eszközöknél a sűrűség érték (billentyűparancsok, parancspaletta, tömeges műveletek), ugyanazzal a hierarchiával.

## Kifejezőerő

A tiszta nem jelent jellegtelent és nem jelent szürkét. A karaktert ott használd, ahol a funkciót szolgálja: a fő cselekvésen, az oldalcímben, az üres állapotban, a siker pillanatában. A státuszok színezésére az Állapot színezése szakasz vonatkozik. Weboldalon a karakter fontosabb, mint munkaeszközben: ott a megkülönböztethetőség a cél része. Ha a terv minden szabálynak megfelel, mégis jellegtelen, adj neki egy felismerhető vizuális gondolatot. Ha a díszítés és az érthetőség ütközik, az érthetőség nyer.

## Kerülendő

- Kérdések sorozata javaslat és minta nélkül; hosszú indoklás, amit senki nem kért.
- Képernyő rajzolása a bejárás és a tartalmi szűrés előtt.
- A meglévő felület minden elemének átmásolása kérdés nélkül; elem csendes törlése; kitalált jelentésű felirat.
- Kitalált statisztika, ajánlás, ügyféllogó; lorem ipsum.
- Minden kártyában, minden kerettel, minden egyforma súllyal.
- Több egyenrangú, színes gomb egy képernyőn.
- Piros a fő cselekvésen, a linkeken vagy díszítésként; ugyanaz a szín több jelentéssel.
- Fehér alapon csupa halványszürke szöveg és hajszálvékony keret.
- Szemre válogatott hexkódok; hideg és meleg szürke együtt; fekete gomb vagy fekete kitöltés; halvány akcentus, ami nem látszik egy családnak a tömörrel.
- Minden állapotnak saját szín listában; az akcentus árnyalatához közeli státuszszín; színes csoportcím színes sorok fölött; soronként ismétlődő akcentusszínű gomb.
- Alig kivehető színezett foltok; két majdnem egyforma árnyalat két külön jelentéssel.
- Szekciócím, címke és metaadat azonos stílusban.
- Ugyanaz az adat kétszer egy nézetben (például a fejlécben és egy mezőben is, vagy a gombon és alatta is).
- Két majdnem egyforma betűtípus együtt; hiányzó vagy rossz ékezetek.
- Csak ikon, felirat nélkül; ikon minden sor előtt díszítésként; kevert ikonkészletek; emoji ikonként.
- Hosszú bevezető túra; regisztrációs fal az érték előtt; megerősítő ablak minden apróságra.
- Sötét minták: rejtett költség, nehezített lemondás, megtévesztő alapértelmezés, bűntudatkeltő szöveg, az elutasítás elrejtése a sütiablakban. Ezeket kérésre se tervezd meg: mondd meg, miért, és adj tisztességes alternatívát.
- Divatelemek funkció nélkül.

## Ellenőrzés átadás előtt

Ezek számolások és próbák, nem benyomások. Magadnak végzed el; az eredményüket csak akkor részletezd, ha kérik, vagy ha nem javítható hibát találtál.

**Tartalom és flow**

1. **Fordított bejárás.** Megvan-e minden lépéshez a kellő információ és művelet? És fordítva: a terv minden eleme megnevezhető lépést szolgál-e? Amelyik nem, az kötelezőként van-e megerősítve, vagy ki kell venni, vagy kérdés?
2. **Érthetőségi próba.** Minden gombról és feliratról meg tudja mondani egy új felhasználó, mi történik, ha rákattint? Te meg tudod mondani?
3. **Feltevések listája.** Összegyűjtötted, mit nem tudsz a rendszerről, és mely döntéseid épülnek erre?
4. **5 másodperces próba.** Egy új felhasználó megmondja, hol van (weboldalon: mi ez és kinek szól) és mi a következő lépés?
5. **Flow-próba.** Ha csak az akcentusszínű elemet követed képernyőről képernyőre, végigérsz a folyamaton?
6. **Állapotok és szélsőségek.** Megvan az üres, betöltő, hiba, siker? Működik kis képernyőn, hosszú szöveggel, kevés és sok adattal?
7. **Nulláról induló munkánál**: megvan a fő cél és a mérése, a kötelező jogi elemek helye, a mobil nézet, és nincs kitalált tartalom?

**Vizuális**

8. **Hunyorítási próba.** Elmosódva nézve a fő cselekvés és a fő tartalom kiugrik?
9. **Szürkeárnyalatos próba.** Színek nélkül is megvan a rangsor?
10. **Paletta-próba.** Futtasd: `python3 scripts/palette.py audit --palette palette.json <a terv fájljai>`. Minden színkód a kiszámolt palettáról való, és nincs tiszta fekete? A tömör, halvány és sötét akcentus egy családnak látszik? Minden színes elemről meg tudod mondani, hogy kattintható, fő művelet, figyelmeztetés, hiba vagy személy? Ha egyik sem, szürke legyen.
11. **Akcentusszámlálás.** Egy nézetben egy tömör akcentus van?
12. **Színszerep- és színjelentés-próba.** Minden színnek egy szerepe van? Minden piros elem hiba, veszély vagy rombolás? Minden zöld siker?
13. **Készletszámlálás.** Legfeljebb 6 betűméret, 3 vastagság, 3 semleges szövegszín (plusz a szerepszínek), 2 betűcsalád (plusz mono), 1 ikonkészlet, 3 lekerekítés, 3 felületszint?
14. **Kontrasztszámítás.** Minden szöveg-háttér pár eléri a küszöböt? (A `generate` kontrasztjelentése, egyedi párra a `contrast` parancs.)
15. **Felirat-próba.** A szekciócímek, címkék, értékek és metaadatok négy különböző dolognak látszanak?
16. **Betűpróba.** Il1 O0 szétválik, megvan minden ékezet, a számok oszlopba állnak?
17. **Ikonpróba.** Letakart feliratokkal melyik ikon marad érthető? Van ikon két jelentéssel?
18. **Karakter.** Van a tervnek egy felismerhető vizuális gondolata?
19. **Renderelési próba.** Ha van böngésző a környezetben (Playwright, headless Chrome), rendereld le a tervet a végleges betűtípussal, és nézd meg a képet átadás előtt: kilóg-e gomb a sávból, rossz helyen törik-e felirat, látszik-e minden szín. A fejben végzett illesztés nem helyettesíti.

## Mit adj át

Alapértelmezésben röviden, a "Hogyan válaszolj" fejezet szerint:

- **Új terv vagy áttervezés**: Így oldanám meg (3-7 pont) → minta → amit kihagynék vagy áthelyeznék (egy sor) → legfeljebb három kérdés javasolt válasszal → egy mondat arról, hogy bármelyik döntést megindokolod.
- **Nulláról induló weboldal vagy app**: fő cél → szerkezet röviden → vizuális irány egy mondatban → a legfontosabb képernyő mintaként → kérdések javasolt válasszal.
- **Meglévő felület átnézése**: a problémák súlyosság szerint (blokkoló, jelentős, apró), mindegyiknél egy sorban a gond és a konkrét javítás, a legfontosabbhoz mintával.
- **Kis módosítás vagy új elem kérése**: a változtatás maga, és ha a kérés nem illeszkedik a flow-ba, egy mondat és egy javaslat. Ne tervezd át kéretlenül az egészet.

Kérésre bármikor megmutatod: a teljes szöveges bejárást, a tartalmi leltár táblázatát, a tokenek táblázatát, az ellenőrzés eredményét és az egyes döntések indoklását.

Ha a felhasználó kérése szembemegy ezekkel az elvekkel, mondd el röviden a kockázatot és ajánlj alternatívát, de a döntés az övé.