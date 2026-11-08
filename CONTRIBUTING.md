# Közreműködés a Godot HUN magyarításában

A Godot HUN egy **nem hivatalos, ingyenes közösségi magyarítás**, amely jelenleg részleges F1 osztályreferencia-fordítást tartalmaz.

## Hogyan jelezz fordítási hibát?

A tárhely nyilvánossá tétele után az **Issues** fülön nyiss hibabejelentést, és add meg:
1. Godot-verzió (például 4.7.2-hu-test.1).
2. Osztály vagy felületelem neve (például Node2D).
3. Eredeti angol szöveg és a hibás magyar fordítás.
4. Javasolt javítás és – ha lehet – képernyőkép.

## Hogyan küldj fordításjavítást?

1. Készíts forkot, majd egy új ágat a módosításokhoz.
2. A `forditas/` könyvtárban javítsd a megfelelő `.po` szövegeket.
3. **Ne fordítsd le vagy módosítsd** a programozási azonosítókat, például `Node2D`, `global_position`, `[code]` és más jelöléseket.
4. Ha a TextEdit szövegeit módosítod, az összevont katalógusban is vezesd át az egyező `msgid` értékhez.
5. Futtasd a `python ellenorzes.py --require-msgfmt` ellenőrzést a `forditas/` mappában. Ehhez GNU gettext szükséges.
6. Nyiss Pull Requestet a változtatás rövid magyarázatával.

## Milyen fordítási elveket követünk?

- Érthető, következetes magyar szaknyelv.
- Az osztálynevek és API-függvénynevek maradjanak angolul, pontosan.
- A `.po` jelöléseket, kódpéldákat és hivatkozásokat meg kell őrizni.
- A javaslatokat az összevonás előtt átnézzük.

A projekt nem tartozik a Godot hivatalos fejlesztőcsapatához. A közösségi közreműködések licencelését a nyilvános megnyitás előtt rendezzük.
