# Godot HUN 🇭🇺

**Ingyenes, közösségi Godot-magyarítás – fejlesztés alatt.**

A projekt célja a Godot játékmotor magyar nyelvű használatának megkönnyítése, különösen a beépített **F1 osztályreferencia** fordításával. A későbbiekben a közösségi hibajavítások és a könnyen indítható Windows-kiadás előkészítése is cél.

> **Állapot (2026. november 8.):** a Godot 4.7.2-stable forrásból fordított Windows-szerkesztő helyben sikeresen elindult. A Node2D osztály súgójában magyar leírások és metódusmagyarázatok látszanak. Ez **részleges fordítás**, nem teljes magyar felület, és még nem publikus, ellenőrzött kiadás. A korábbi teszt nem igazolja, hogy minden osztály vagy panel magyarul működik.

## Mi van itt?

| Fájl | Tartalom |
| --- | --- |
| [Összevont PO](forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po) | 2185 egyedi angol szöveghez tartozó magyar munkafordítás |
| [TextEdit PO](forditas/TextEdit_4_7_2_hu_reszlet.po) | 292 TextEdit-bejegyzés munkafordítása, az összevont katalógussal összehangolva |
| [Ellenőrző program](forditas/ellenorzes.py) | PO-bejegyzések, jelölések és gettext-szintaxis ellenőrzése |
| [Tesztelés és összeállítás](docs/TESZTELES_ES_FORDITAS.md) | A működő helyi teszt és az újraépítés leírása |

Az itt tárolt `.po` állományok **munkakatalógusok**, nem a teljes, hivatalos Godot-fordítás. A `TextEdit` 292 bejegyzése **nem adandó hozzá** a 2185-höz: azok már szerepelnek az összevont fájlban.

## Közösségi javítások

A tervezett nyilvános kiadás után hibabejelentéseket és pull requesteket szeretnénk fogadni. A javaslatok ellenőrzése után kerülhetnek be a fordításba. Programozási azonosítók (például `Node2D`, `global_position`) maradjanak változatlanok.

## Biztonság és terjesztés

- A jelenlegi tárhely **privát**; a magyar Windows-kiadás még nincs közzétéve.
- Ne keverd össze ezt a projektet a hivatalos Godot Engine kiadással; ez **nem hivatalos közösségi magyarítás**.
- A saját fordítási hozzájárulásokhoz létrehoztuk a [MIT-licencnyilatkozatot](LICENSE-TRANSLATIONS.txt); az eredeti Godot- és harmadik fél jogi nyilatkozatokat ez nem helyettesíti. A nyilvános kiadás előtti attribúciós és működési ellenőrzések még folyamatban vannak.
- A lefordított program helyi biztonsági másolata külön található a fejlesztő gépén, **nem** ebben a tárhelyben.

## Ingyenesség és közösségi licenc – elfogadott projektelv

**A Godot HUN-t ezen a projekten keresztül mindig ingyenesen tesszük elérhetővé.** Nem kérünk pénzt a magyarítás vagy a hivatalos projektletöltés használatáért.

A magyar fordítások tervezett licence **MIT**, amely a szabad használaton és módosításon túl a kereskedelmi újrafelhasználást is megengedi. Ez tudatos döntés; mások esetleges kereskedelmi felhasználása nem változtat a mi ingyenes terjesztési vállalásunkon.

**Licencelési státusz:** a projektgazda jóváhagyta a fordítások MIT-licencű közreadását, és elkészült a [fordítási licencnyilatkozat](LICENSE-TRANSLATIONS.txt). A fordítási szövegek és esetleges külső tartalmak jogosultságait a nyilvános kiadás előtt tovább ellenőrizzük. A GitHub kiadási piszkozat továbbra sem nyilvános.

## A fordítás eredete és licencellenőrzése

Az előzetes forrás- és jogosultsági vizsgálat eredménye: [Fordítás eredetének ellenőrzése](docs/FORDITAS_EREDET_ES_JOGOSULTSAGOK.md).

Az alapul szolgáló Godot osztályreferencia és hivatalos fordítások MIT-licencűek, de a saját magyar `msgstr` szövegek eredetét még tételesen ellenőrizni kell. A teljes katalógus 2185 magyarított bejegyzése nem azonos a teljes Godot-dokumentáció fordításával.

## Kapcsolódó oldalak

- [Godot Engine](https://godotengine.org/)
- [Godot forráskód](https://github.com/godotengine/godot)
- [Godot fordítási útmutató](https://contributing.godotengine.org/en/latest/development/translations.html)
- [Smaragd Editor](https://github.com/norbi79uj/Smaragd-Editor)

**Cél:** ingyenesen használható és közösen javítható magyar Godot.
