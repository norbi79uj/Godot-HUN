# Godot-HUN – 49. szakasz: TabContainer forrásellenőrzés

Forrás: godotengine/godot, `4.7`, `doc/classes/TabContainer.xml`.
Vizsgált javaslatok: 45., 46., 47. és 48. szakasz (`forditas/javaslatok/`).

## Mennyiségi eredmény

- Eredeti F1 osztályleírások/metódusok/tulajdonságok/jelzések/állandók/tématételek: **86**.
- Összes javasolt bejegyzés: **86**.
- Eredeti bejegyzéshez pontosan párosított: **86**.
- Hiányzó eredeti bejegyzések: **0**.
- Többször előforduló azonos kategóriájú bejegyzések: **0**.
- Angol forrásszöveg-eltérések: **0**.
- BBCode-hivatkozás / jelölésmultihalmaz eltérések: **0**.

A `tab_hovered` és `tab_selected` kétszer szerepelnek, de **külön kategóriákban** (eseményjelzés, illetve témastílus), ezért nem duplikációk. PO-katalógusba történő végleges összevonáskor a teljes angol `msgid` alapján kell egyeztetni.

## Lektorálási figyelmeztetések (eredeti Godot-forrás)

1. A `tab_{index}/icon` tulajdonság leírása *a fül címének szövegét* említi ikon helyett.
2. A `tab_{index}/title` tulajdonság leírása *az eszköztipp szövegét* említi cím helyett.
3. A `tabs_position` tulajdonság eredeti leírása *vízszintes igazítást* mond, miközben az osztály `TabPosition` értékei felül/alul elhelyezést jelölnek.

Ezeket nem javítottuk ki csendben a forrásszövegtől eltérő `msgid`-del: a magyar szöveg jelenleg követi az angol leírás jelentését. A végleges lektoráláskor, illetve upstream hibajelentés lehetőségének vizsgálatakor külön döntést igényelnek.

## Korlátok

Ez célzott, a 45–48. szakasz javaslatfájljaira kiterjedő forrás-/jelölésellenőrzés. **Nem** történt fő PO-összevonás, teljes PO-szintaktikai ellenőrzés `msgfmt`-tel, Godot-build vagy GitHub Actions CI-futtatás; a meglévő automatizált ellenőrzés korábbi hibája sem tekinthető megoldottnak.

## Következő lépés

A `TabContainer` javaslatok teljes katalógusba való deduplikált összevonása és a három upstream súgóanomália célzott lektorálása.
