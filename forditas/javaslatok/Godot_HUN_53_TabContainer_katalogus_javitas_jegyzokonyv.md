# Godot-HUN – 53. szakasz: célzott javítások és ütközéskezelés

A fő munkakatalógus: `forditas/Godot_4_7_2_hu_LEKTORALT_32.po`.

## Ellenőrzött eredmény

A fő katalógusban **2** célzott magyar fordítás javítva és visszaolvasással megerősítve:
- `TabContainer.tab_{index}/icon`: a fül ikonja.
- `TabContainer.tab_{index}/title`: a fül címszövege.

A `TabContainer.tabs_position` javasolt magyar változtatását **vissza kellett állítani**, mert az eredeti angol `msgid` (`The horizontal alignment of the tabs.`) közös a `TabBar.tab_alignment` bejegyzéssel. A PO-fájlban a szöveghez csak egy közös fordítás tartozik, és a fül felső/alsó helyzetéről szóló módosítás hibás lenne a TabBar esetében. A közös szöveg ismét: **A fülek vízszintes igazítása.** A TabContainer-nek ez kevésbé pontos, de a külön kontextus nélküli katalógusban nem javítható biztonságosan pusztán a magyar `msgstr` változtatásával.

- Bejegyzések száma: **2691**.
- Egyedi angol `msgid`: **2691**.
- Új vagy duplikált bejegyzés: **0**.
- Célzott javítások után a GitHub-fájl új blob-SHA-ja: `b77be28adc707eb7b7e17e9448253e5ec5dbe32b`.

## Korlátok

A változtatás nem `LEKTORALT_33` új kiadás, hanem a 32-es **munkakatalógus** pontosítása. Nem futott `msgfmt`, Godot-build vagy teljes GitHub Actions CI. A közös `msgid` ellentmondásához upstream kontextus vagy dokumentációjavítás lehet szükséges.
