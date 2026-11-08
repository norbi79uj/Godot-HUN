# Godot HUN 4.7.2 – ZIP-ellenőrzési jegyzőkönyv

**Dátum:** 2026-11-08  
**Tervezett címke:** `4.7.2-hu-test.1`  
**Kiadás állapota:** GitHub-piszkozat, előzetes; még nincs publikálva.

## 1. GitHub Release melléklete

A GitHub API alapján az egyetlen csatolt fájl:
- Név: `Godot-HUN-4.7.2-Teszt.zip`
- Méret: **82 220 632 bájt**
- SHA-256: `f0c95e750cb5f2a75c9ba54103722b241b185c4ea92c15d914575da95a1b3cf0`

A GitHub-példány **belső tartalmát még nem ellenőriztük külön**. A feltöltött fájl neve és metaadatai ellenőrzöttek.

## 2. A ChatGPT-beszélgetéshez csatolt ZIP külön ellenőrzése

- Név: `Godot-HUN-4.7.2-Teszt.zip`
- Méret: **81 579 340 bájt**
- SHA-256: `aa421ee6dc8accf65c4f1b05f3594d3e9eec2db5d0a8b09657433990bd14533e`
- A Python `zipfile.testzip()` szerint: **nincs sérült fájl**.
- A ZIP egy `Godot-HUN-4.7.2-Teszt/` könyvtárat tartalmaz, négy fájllal:

| Fájl | Kicsomagolt méret (bájt) | SHA-256 |
| --- | ---: | --- |
| `COPYRIGHT.txt` | 100 108 | `cb1980c88089573bcacd7221d777c689bb8bbd778799f24c27fca0fe5f774d6d` |
| `godot.windows.editor.x86_64.exe` | 162 961 920 | `bf5542ea21d011ee87448daa191741a8b08b0ddfac0320c98b867c3d6fe2e5da` |
| `LICENSE.txt` | 1 149 | `b0435e3b3e4e55238f05f4b306f30524a1b2e20147810d436eaa554fa6855c80` |
| `OLVASS_EL_Godot_HUN_4.7.2.txt` | 2 735 | `6856904743c500e5d130d54364d0130d0525c96424fe5faf1a95984d5605c636` |

## 3. Eltérés és következő ellenőrzés

A két ZIP **nem bájtra azonos**: különbözik a méret és a SHA-256. Ez lehet csupán eltérő ZIP-tömörítés is, de ezt nem szabad bizonyítás nélkül feltételezni.

**Következő lépés:** a GitHub-piszkozatból letöltött ZIP-et külön kell ellenőrizni; lehetőleg a benne lévő négy fájl SHA-256 értékét a fenti táblázathoz hasonlítva.

A forrásfájlból létrehozott Windows EXE-vel a felhasználó sikeres helyi indítási és magyar Node2D F1-tesztet végzett. Másik Windows-gépen és tiszta környezetben való teszt még hátravan.

**Nyilvános közzétételt csak az eltérés tisztázása és a kiadási feltételek végső ellenőrzése után javasolunk.**
