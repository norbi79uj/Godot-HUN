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

### Ami még nincs lezárva

- [ ] **Közösségi fordítások saját felhasználási engedélye:** a repóban szereplő `.po` munkafájlokra és később elfogadott külső hozzájárulásokra még nincs végleges, a jogosultak által jóváhagyott licenc-/hozzájárulási szabály. A Godot `LICENSE.txt` *önmagában nem dönti el* a külön elkészített fordítás saját jogállását.
- [ ] Külső könyvtárak terjesztési követelményeinek végső tételes összevetése az adott Windows-builddel. A `COPYRIGHT.txt` összesíti őket, de nem garantálja önmagában minden feltétel teljesítését.
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

A nyilvános terjesztés előtt tisztázni kell a fordítás jogállását, és a közösség számára egységes közreműködési licencet választani a jogosultak jóváhagyásával. A GitHub Release-piszkozatot addig ne publikáljuk. A privát tárhely és a helyi programok változatlanok maradhatnak.
