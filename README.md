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
- Közzététel előtt ellenőrizni kell a Godot és a terjesztett összetevők licencfeltételeit, valamint a fordítások felhasználási jogait. Ennek lezárásáig nem adunk hozzá találomra licencet.
- A lefordított program helyi biztonsági másolata külön található a fejlesztő gépén, **nem** ebben a tárhelyben.

## Kapcsolódó oldalak

- [Godot Engine](https://godotengine.org/)
- [Godot forráskód](https://github.com/godotengine/godot)
- [Godot fordítási útmutató](https://contributing.godotengine.org/en/latest/development/translations.html)
- [Smaragd Editor](https://github.com/norbi79uj/Smaragd-Editor)

**Cél:** ingyenesen használható és közösen javítható magyar Godot.
