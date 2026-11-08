# Godot HUN – kiadás előtti megfelelőségi ellenőrzés

**Ellenőrzés dátuma:** 2026. november 8.  
**Célkiadás:** `4.7.2-hu-test.1`  
**Állapot:** privát GitHub-tárhely, **mentett Release-piszkozat**; nincs publikálva.

## Igazolt eredmények

- [x] A GitHub Release jelenleg **draft=true**, **prerelease=true**; tag: `4.7.2-hu-test.1`.
- [x] Pontosan egy GitHub-melléklet: `Godot-HUN-4.7.2-Teszt.zip`.
- [x] A GitHubon lévő ZIP mérete: **81 579 340 bájt**; SHA-256: `aa421ee6dc8accf65c4f1b05f3594d3e9eec2db5d0a8b09657433990bd14533e`.
- [x] A beszélgetéshez feltöltött helyi ZIP ugyanezt a méretet és SHA-256-ot adta: **bájtra azonos**.
- [x] A ZIP `testzip()` ellenőrzése sikeres; négy fájl és egy gyökérmappa található benne.
- [x] `LICENSE.txt` (1149 bájt) és `COPYRIGHT.txt` (100108 bájt) jelen van, az eredeti, feltöltött dokumentumokkal **bájtra azonos**.
- [x] `OLVASS_EL_Godot_HUN_4.7.2.txt` (2735 bájt) szerepel a ZIP-ben.
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

### Konkrét javítás a terjesztési ZIP-hez

**A jelenlegi négyfájlos ZIP nem tartalmazza a projekt saját `LICENSE-TRANSLATIONS.txt` nyilatkozatát.** Az eredeti Godot `LICENSE.txt` és `COPYRIGHT.txt` már benne van. Az MIT licencszöveg és a szerzői jogi nyilatkozat megőrzése a fordítási tartalom továbbterjesztésekor is fontos; ezért a **nyilvános terjesztés előtt ajánlott a `LICENSE-TRANSLATIONS.txt` fájlt is beletenni** a ZIP-be, változatlan néven. A forrásban lévő eredeti licenceket nem szabad eltávolítani.

- [ ] A ZIP-be mellékelni a saját `LICENSE-TRANSLATIONS.txt` fájlt a repó gyökeréből.
- [ ] A ZIP-ben lévő magyar `OLVASS_EL_Godot_HUN_4.7.2.txt` szövegét a megjelenésnek megfelelően frissíteni, mert jelenleg még a privát tárhelyről ír.
- [ ] A frissített ZIP-et helyben ellenőrizni és **a GitHub Release-piszkozatban** lecserélni, majd a méretet és az SHA-256 összeget a `SHA256SUMS.txt` fájlban és a kiadási szövegben hozzáigazítani.

Ezek **csomagolási és dokumentációs teendők**, a működő Godot EXE újrafordítását nem igénylik. Eddig **nem** módosítottuk az eredeti ZIP-et vagy a GitHub Release-mellékletet.

Hivatalos tájékoztatás: https://godotengine.org/license/ és https://docs.godotengine.org/en/stable/about/complying_with_licenses.html

### Frissített csomag elkészült – GitHub-melléklet cseréje még hátravan

2026. november 8-án a helyi kiadási ZIP új változata elkészült, de **még nincs feltöltve a GitHub Release-be**. A javított csomagban már **öt fájl** található: az eredeti EXE, a Godot eredeti `LICENSE.txt` és `COPYRIGHT.txt`, a frissített magyar útmutató és a saját `LICENSE-TRANSLATIONS.txt`.

- **Új ZIP:** `Godot-HUN-4.7.2-Teszt.zip`
- **Méret:** `81 616 373` bájt
- **SHA-256:** `f44ff14ceb5f1fe8beb0746c0430547498961aa25ff77385504d19c93c346421`
- **ZIP-teszt:** sikeres.
- **EXE SHA-256:** `bf5542ea21d011ee87448daa191741a8b08b0ddfac0320c98b867c3d6fe2e5da` – **változatlan**.
- A Godot eredeti licenc- és szerzői jogi fájljainak ellenőrzőösszege szintén változatlan.
- [x] Helyi javított ZIP előállítva és tartalma ellenőrizve.
- [ ] A GitHub Release-piszkozatban a **régi** melléklet lecserélése az új ZIP-re.
- [ ] Feltöltés után a GitHubon lévő új melléklet méretének és ellenőrzőösszegének visszaellenőrzése.
- [ ] Csak **a csere igazolása után** frissítendő a repó `kiadasok/4.7.2-hu-test.1/SHA256SUMS.txt` fájlja és a közzétételi ismertető korábbi SHA-256 adata.

**Figyelem:** a dokumentum korábbi részében és a GitHubon még a régi, `81 579 340` bájtos ZIP szerepel; ez nem a frissített csomag. A két állapotot nem szabad összekeverni.

### Ami még nincs lezárva

**Megkülönböztetés:** a hivatalos Godot-útmutató szerinti licencfájlok meglétét már igazoltuk; az opcionális függőség-audit nem jelenti automatikusan, hogy hiányzik egy kötelező irat. A `COPYRIGHT.txt` megőrzése a Godot hivatalosan ajánlott eljárása. Forrás: https://docs.godotengine.org/en/stable/about/complying_with_licenses.html


- [x] **AI-segített fordítás jogalapja dokumentálva:** az angol forrás MIT-licencű Godot-osztályreferencia; az OpenAI felhasználási feltételei szerint a kimenetet a felhasználó felhasználhatja, az esetleges harmadik fél jogainak tiszteletben tartásával. Részletek: [fordítás eredete](FORDITAS_EREDET_ES_JOGOSULTSAGOK.md).
- [ ] Ha konkrét külső magyar fordítás vagy más forrásból átvett védett szöveg azonosítható, annak jogosultságát a kiadás előtt külön tisztázni kell. A forráskatalógus puszta vizsgálata nem bizonyít minden lehetséges szövegegyezés hiányát.
- [x] A Godot hivatalos, asztali terjesztésre javasolt eljárása szerinti `LICENSE.txt` és `COPYRIGHT.txt` a kiadási ZIP-ben szerepel. Ez **dokumentációs megfelelési ellenőrzés**, nem független jogi szakvélemény.
- [ ] Csak akkor szükséges további összetevő-specifikus ellenőrzés vagy nyilatkozat, ha a saját build az eredeti `COPYRIGHT.txt` által nem fedett, külön hozzáadott külső összetevőt tartalmaz. Ilyen kiegészítőt a jelen dokumentáció nem azonosít, de az összes buildfüggőség tételes auditja nem történt meg.
- [ ] Másik, tiszta Windows-környezetben való indítási teszt.
- [ ] Több F1-osztály, grafikai mód, fájlmegnyitás és hiányzó fordítás részletes ellenőrzése.
- [ ] Nyilvános megosztás jóváhagyása és az első kiadás világos, **nem hivatalos / részleges / teszt** címkézése.

## A ZIP fájljainak SHA-256 ellenőrzése

| Fájl | SHA-256 |
| --- | --- |
| `COPYRIGHT.txt` | `cb1980c88089573bcacd7221d777c689bb8bbd778799f24c27fca0fe5f774d6d` |
| `godot.windows.editor.x86_64.exe` | `bf5542ea21d011ee87448daa191741a8b08b0ddfac0320c98b867c3d6fe2e5da` |
| `LICENSE.txt` | `b0435e3b3e4e55238f05f4b306f30524a1b2e20147810d436eaa554fa6855c80` |
| `OLVASS_EL_Godot_HUN_4.7.2.txt` | `6856904743c500e5d130d54364d0130d0525c96424fe5faf1a95984d5605c636` |

## Következő javasolt teendő

A közösségi licenc szabályai már dokumentáltak. A nyilvános terjesztés előtt a **valóban nyitott** harmadik fél / attribúciós és működési kérdéseket kell lezárni, majd a projektgazda külön jóváhagyását kérni. A GitHub Release-piszkozatot addig ne publikáljuk; a privát tárhely és a helyi programok változatlanok maradhatnak.
