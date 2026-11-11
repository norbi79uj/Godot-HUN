# Godot-HUN – 51. szakasz: TabContainer integráció előtti ellenőrzés

Forrás: `godotengine/godot`, `4.7`, `doc/classes/TabContainer.xml`.
Vizsgált fájl: `forditas/javaslatok/Godot_HUN_50_TabContainer_osszevont_lektoralasi_javaslat.po`.

## Automatikus, célzott ellenőrzés

- Feldolgozott, nem fejléc típusú PO-bejegyzés: **86**.
- Eredeti Godot 4.7 súgóbejegyzés: **86**.
- Hiányzó vagy az eredetihez nem illeszkedő bejegyzések: **0**.
- Duplikált teljes angol `msgid`: **0**.
- Külön kategóriában ismétlődő rövid tagnevek: **2** (nem hibák).
- BBCode-jelöléseltérések: **0**.
- Felismert PO-szerkezeti hibák a saját soronkénti feldolgozóban: **0**.

### Nem hibás névegyezések

- `tab_hovered`: külön eseményjelzés és témastílus.
- `tab_selected`: külön eseményjelzés és témastílus.

Mindkét pár különböző teljes angol `msgid` értéket használ, ezért a PO-katalógusban nincs ütközés.


## Lektorálási megjegyzések

A három tudatosan pontosított magyar jelentés változatlan angol `msgid` mellett szerepel a 50. szakasz összevont javaslatában: `tab_{index}/icon`, `tab_{index}/title`, `tabs_position`. Ezek az eredeti Godot-dokumentáció feltételezett pontatlanságaira reagálnak.

## Még nem ellenőrizhető / el nem végzett lépések

A fő munkakatalógus `forditas/Godot_4_7_2_hu_LEKTORALT_32.po` fájlja a csatlakoztatott lekérdezésben **üres tartalommal** érkezett vissza, ezért **nem** történt megbízható ütközésvizsgálat a fő katalógus meglévő angol `msgid` azonosítóival. A fő katalógus nem változott.

A jelen ellenőrzés saját PO-feldolgozóval történt; nem teljes `msgfmt --check` futtatás, nem Godot build és nem GitHub Actions teszt. A korábban fennálló CI-hibát nem tekintjük megoldottnak.

## Következő lépés

A fő katalógus tartalmát elérhetővé kell tenni (például letölthető/raw változatban vagy feldolgozható részletekben), utána a `msgid` ütközések és az esetleg már lefordított sorok feloldásával lehet biztonságosan összevonni.
