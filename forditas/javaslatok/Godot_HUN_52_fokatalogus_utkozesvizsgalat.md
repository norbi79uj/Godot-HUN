# Godot-HUN – 52. szakasz: fő katalógus beolvasása és ütközésvizsgálat

## Források

- Fő munkakatalógus: `forditas/Godot_4_7_2_hu_LEKTORALT_32.po`, GitHub blob: `8a144bfcadef543a3ca4fd6029c15c8516c09571`.
- Lektorálási javaslat: `forditas/javaslatok/Godot_HUN_50_TabContainer_osszevont_lektoralasi_javaslat.po`.

A GitHub egyszerű fájlolvasása üres tartalmat adott vissza, de a blob-SHA alapú lekérés **sikeresen visszaadta a teljes fő munkakatalógust**.

## Összevetés

- Fő PO-ban található fordítási bejegyzések: **2691**.
- Javasolt TabContainer-bejegyzések: **86**.
- Már létező angol `msgid` a fő katalógusban: **86 / 86**.
- Teljesen azonos magyar szöveg: **21**.
- Eltérő, de létező magyar szöveg: **65**.
- A fő katalógusból hiányzó TabContainer `msgid`: **0**.
- A fő katalógus egészében ismétlődő `msgid`: **0**.
- A fő katalógus TabContainer szövegein belül eltérő BBCode-jelölések száma: **0**.

**Fontos:** nem szabad 86 új rekordot a fő katalógushoz fűzni: mind a 86 már benne van. A 65 eltérés fordítási variáns vagy lektorálási változtatás, ezért nem automatikusan hiba.

## Három célzott, szemantikailag indokolt javítási javaslat

1. `tab_{index}/icon`: fül ikonja (az eredeti leírás tévesen címszöveget említ).
2. `tab_{index}/title`: fül címszövege (az eredeti leírás tévesen eszköztippet említ).
3. `tabs_position`: a fülsáv felső vagy alsó elhelyezése (az eredeti leírás vízszintes igazítást említ).

Ezekhez külön, mindössze 3 tételes javítási PO-javaslat készült: `Godot_HUN_52_TabContainer_harom_javitas_javaslat.po`. Az angol `msgid` változatlan; a BBCode-jelölések egyeznek.

## Állapot

A fő kiadás **nem változott**, mert a meglévő 86 fordítás közül 65 eltérő változatot előbb érdemes emberi lektorálási szempontból mérlegelni. A három tartalmi hibagyanút külön kiválasztottuk. Nem futott teljes `msgfmt`, Godot-build vagy GitHub Actions CI.

## Javasolt következő lépés

A három célzott javítás beillesztése a fő munkakatalógusba, majd a fennmaradó 62 szövegváltozat differenciális lektorálása az eredeti fordítás indokolatlan felülírásának elkerülésére.
