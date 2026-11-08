# Godot HUN – kiadás előtti megfelelőségi ellenőrzés

**Ellenőrzés dátuma:** 2026. november 8.  
**Célkiadás:** `4.7.2-hu-test.1`  
**Állapot:** privát GitHub-tárhely, **mentett Release-piszkozat**; nincs publikálva.

## Igazolt eredmények

- [x] A GitHub Release jelenleg **draft=true**, **prerelease=true**; tag: `4.7.2-hu-test.1`.
- [x] Pontosan egy GitHub-melléklet: `Godot-HUN-4.7.2-Teszt.1.zip` (a javított csomag).
- [x] A GitHubon lévő ZIP mérete: **81 616 373 bájt**; SHA-256: `f44ff14ceb5f1fe8beb0746c0430547498961aa25ff77385504d19c93c346421`.
- [x] A javított helyi ZIP és a GitHub-melléklet **mérete és SHA-256 ellenőrzőösszege egyezik**.
- [x] A ZIP `testzip()` ellenőrzése sikeres; öt fájl és egy gyökérmappa található benne.
- [x] `LICENSE.txt` (1149 bájt) és `COPYRIGHT.txt` (100108 bájt) jelen van, az eredeti, feltöltött dokumentumokkal **bájtra azonos**.
- [x] A frissített `OLVASS_EL_Godot_HUN_4.7.2.txt` és a saját `LICENSE-TRANSLATIONS.txt` szerepel a javított ZIP-ben.
- [x] `godot.windows.editor.x86_64.exe` (162 961 920 bájt) szerepel a ZIP-ben.
- [x] A felhasználó korábbi képei igazolták a helyi indítást és a magyar Node2D F1-súgó működését, valamint a ZIP kicsomagolásából indított Godot sikeres elindulását **ugyanazon Windows-gépen**.

## Licencértékelés

### Godot motor

A mellékelt eredeti `LICENSE.txt` a Godot Engine hozzájárulóinak szerzői jogi nyilatkozatát és az **MIT/Expat licencet** tartalmazza. Az engedély feltétele a szerzői jogi és licencnyilatkozat megtartása a másolatokban / jelentős részekben. Ez a csomagban teljesül.

A `COPYRIGHT.txt` a Godot és külső függőségek eltérő licenceit is részletezi. A mellékelése helyes lépés a szerzői jogi tájékoztatáshoz.

### Azóta igazolt előrelépések (2026. november 8.)

- [x] A projektgazda elfogadta a magyar fordítás MIT-licencű, ingyenesen hozzáférhető közzétételét, beleértve az MIT által engedélyezett kereskedelmi felhasználást.
- [x] A `LICENSE-TRANSLATIONS.txt` elkészült; a `CONTRIBUTING.md` a jövőbeni közreműködők MIT-feltételeit ismerteti.
- [x] A Godot hivatalos licencoldala szerint a Godot MIT-licencű, módosított változatban is terjeszthető, a licenc- és szerzői jogi nyilatkozatok megtartásával: https://godotengine.org/license/
- [x] A hivatalos szerkesztő- és osztályreferencia-fordítások `msgid`/`msgstr` tartalma MIT-licencű: https://github.com/godotengine/godot-editor-l10n
- [x] A Godot hivatalos megfelelőségi útmutatója a motorhoz csatolt `COPYRIGHT.txt`-t javasolja a külső könyvtárak nyilatkozatainak dokumentálására: https://docs.godotengine.org/en/stable/about/complying_with_licenses.html

### A javított kiadási ZIP ellenőrzése (2026. november 8.)

- [x] A fordítás saját MIT-nyilatkozata (`LICENSE-TRANSLATIONS.txt`) bekerült a ZIP-be.
- [x] A magyar útmutató frissítve, az eredeti Godot-licencek megőrizve.
- [x] Az ötfájlos ZIP sértetlenségét helyben ellenőriztük; az EXE változatlan maradt.
- [x] A javított csomag a GitHub Release-piszkozat egyetlen melléklete.
- [x] A GitHub API szerint a melléklet **81 616 373 bájt**, SHA-256: `f44ff14ceb5f1fe8beb0746c0430547498961aa25ff77385504d19c93c346421`; ez egyezik a javított helyi csomaggal.
- [x] A GitHubon tárolt SHA256SUMS és kiadási dokumentáció az új melléklethez igazítva.

**Fontos:** a feltöltött fájl GitHub-neve `Godot-HUN-4.7.2-Teszt.1.zip` lett, ezért a fájlnév az ellenőrzőösszeg-fájlban is pontosan ez. A ZIP belső könyvtárneve ettől nem változott.

### Ami még nincs lezárva

**Megkülönböztetés:** a hivatalos Godot-útmutató szerinti licencfájlok meglétét már igazoltuk; az opcionális függőség-audit nem jelenti automatikusan, hogy hiányzik egy kötelező irat. A `COPYRIGHT.txt` megőrzése a Godot hivatalosan ajánlott eljárása. Forrás: https://docs.godotengine.org/en/stable/about/complying_with_licenses.html


- [x] **AI-segített fordítás jogalapja dokumentálva:** az angol forrás MIT-licencű Godot-osztályreferencia; az OpenAI felhasználási feltételei szerint a kimenetet a felhasználó felhasználhatja, az esetleges harmadik fél jogainak tiszteletben tartásával. Részletek: [fordítás eredete](FORDITAS_EREDET_ES_JOGOSULTSAGOK.md).
- [x] A projektgazda megerősítette, hogy **nem másoltunk át kész magyar fordításokat** más forrásokból. Ez alapján nincs jelenleg azonosított, külön engedélyre váró külső magyar fordítás. **Feltételes megjegyzés:** ha később konkrét külső, védett szöveg átvétele derül ki, annak jogát külön rendezni kell; minden lehetséges szövegegyezés hiánya nem igazolt.
- [x] A Godot hivatalos, asztali terjesztésre javasolt eljárása szerinti `LICENSE.txt` és `COPYRIGHT.txt` a kiadási ZIP-ben szerepel. Ez **dokumentációs megfelelési ellenőrzés**, nem független jogi szakvélemény.
- [x] A projektgazda megerősítése szerint **nem került hozzá külön külső összetevő**, így jelenleg nincs azonosított, a Godot eredeti `COPYRIGHT.txt` által nem fedett új csomag- vagy attribúciós kötelezettség. A teljes buildfüggőség-audit nem történt meg; ha utóbb eltérő bizonyíték merül fel, azt külön rendezni kell.
- [ ] Másik, tiszta Windows-környezetben való indítási teszt.
- [ ] Több F1-osztály, grafikai mód, fájlmegnyitás és hiányzó fordítás részletes ellenőrzése.
- [ ] Nyilvános megosztás jóváhagyása és az első kiadás világos, **nem hivatalos / részleges / teszt** címkézése.

## A ZIP fájljainak korábban ellenőrzött SHA-256 értékei

| Fájl | SHA-256 |
| --- | --- |
| `COPYRIGHT.txt` | `cb1980c88089573bcacd7221d777c689bb8bbd778799f24c27fca0fe5f774d6d` |
| `godot.windows.editor.x86_64.exe` | `bf5542ea21d011ee87448daa191741a8b08b0ddfac0320c98b867c3d6fe2e5da` |
| `LICENSE.txt` | `b0435e3b3e4e55238f05f4b306f30524a1b2e20147810d436eaa554fa6855c80` |
| `OLVASS_EL_Godot_HUN_4.7.2.txt` | Frissített változat a javított ZIP-ben; a korábbi hash már nem érvényes |

## Kiadási döntés: szükséges feltételek és vállalt tesztkorlátok

**Szükséges, még megerősítendő feltételek:**

- [x] **A projektgazda 2026. november 8-án kifejezetten megerősítette:** a magyar fordítás a Godot eredeti angol szövege alapján, ChatGPT segítségével készült; más weboldalakról vagy kész magyarításokból nem másoltunk át magyar fordításokat. Ez projektgazdai nyilatkozat, **nem** független plágium- vagy jogi audit. Ha később ellenkező konkrét adat merül fel, azt kiadás előtt vagy után külön megvizsgáljuk.
- [x] **Projektgazdai megerősítés (2026. november 8.):** a Windows-buildbe a hivatalos Godot-forráson és a saját magyar fordításon/dokumentáción kívül **nem került külön külső forrás vagy összetevő**. A mellékelt eredeti `LICENSE.txt` és `COPYRIGHT.txt` változatlan. Ez a projektgazda nyilatkozata, **nem** a fordítói eszközlánc és valamennyi beépített függőség független, tételes auditja.
- [x] **Projektgazdai jóváhagyás (2026. november 8.):** a projektgazda a kérdésre igennel válaszolva jóváhagyta a GitHub-tárhely nyilvánossá tételét és az első, nem hivatalos, részleges tesztkiadás megjelentetését az ismert tesztkorlátok feltüntetésével. **A két GitHub-művelet még nem történt meg**; a tárhely privát, a Release továbbra is piszkozat. A közzététel állapotát külön ellenőrizni kell.

**Tesztkiadásként vállalható, nyíltan jelzett korlátok (nem állítjuk teljesítettnek):**

- [ ] Másik, tiszta Windows-gépen végzett indítási próba: **nem történt meg**. Az első kiadást nem szabad általánosan kompatibilisnek nevezni.
- [ ] Több F1-osztály, különféle grafikus módok és projektek részletes vizsgálata: **nem történt meg**. A kiadás részleges, visszajelzésekre nyitott teszt.
- [ ] A GitHubon időközben tovább szerkesztett `.po` munkakatalógus és a már lefordított EXE teljes egyezése: **nincs igazolva**. A kiadott EXE korábbi pillanatfelvétel; az újabb PO-javításokhoz új build szükséges. Ne hirdessük úgy, mintha minden jelenlegi munkafordítás a kiadott EXE-ben lenne.

**Csomagvizsgálat (2026. november 8.):** a javított helyi ZIP újra megnyitható és a ZIP-fájlok CRC-ellenőrzése sikeres; az útmutató már hivatkozik a `LICENSE-TRANSLATIONS.txt` fájlra. Ez **nem** helyettesíti a Windows-on végzett futási próbát.

**Fontos:** az első két megerősítési pont nem független jogi audit; akkor tekinthető rendben lévőnek, ha a projektgazda a tényleges források ismeretében jóhiszeműen meg tudja erősíteni, és nincs ismert ellentmondás.

## Következő javasolt teendő

A közösségi licenc szabályai már dokumentáltak. A nyilvános terjesztés előtt a **valóban nyitott** harmadik fél / attribúciós és működési kérdéseket kell lezárni, majd a projektgazda külön jóváhagyását kérni. A GitHub Release-piszkozatot addig ne publikáljuk; a privát tárhely és a helyi programok változatlanok maradhatnak.
