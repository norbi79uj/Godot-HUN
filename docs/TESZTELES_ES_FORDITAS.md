# Godot 4.7.2 – helyi magyar F1-teszt és biztonságos összeállítás

## A már elvégzett teszt

2026. november 8-án Windows alatt az eredeti Godot 4.7.2-stable forrásból sikeres fordítás készült MSYS2 UCRT64 környezetben. A külön tesztprojekt elindult, és a Node2D osztály F1-súgója magyar leírásokat jelenített meg.

A jobb oldali Inspector tulajdonságcsoportjai közül több továbbra is angol; ez **nem** a dokumentációs PO-fájl feladata, és nem jelenti a teszt kudarcát.

## Használt környezet

- Godot 4.7.2-stable forrás, helyi példa: `C:\GodotHU-Test\godot-4.7.2-stable`
- MSYS2 UCRT64, MinGW C++ fordító, Python, SCons
- Részleges magyar F1-katalógus: `forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po`
- A helyi kipróbálásban a PO-t `doc/translations/hu.po` helyre másolták. Ez a tesztben működött; más Godot-verzióknál újra kell ellenőrizni a kompatibilitást.

## Munkafordítás ellenőrzése

A repó gyökeréből:

```bash
cd forditas
python ellenorzes.py --require-msgfmt
```

Az ellenőrző script GNU gettext `msgfmt`-et igényel a teljes szintaxisellenőrzéshez. A korábbi helyi teszt 2185 összevont és 292 TextEdit-bejegyzést talált, mindkét fájl átment a `msgfmt --check` vizsgálaton.

## A helyi Windows-teszt fordítási parancsa

A Godot forrásának gyökeréből, MSYS2 UCRT64 terminálból:

```bash
scons platform=windows target=editor arch=x86_64 use_mingw=yes accesskit=no d3d12=no angle=no winrt=no -j4
```

A `no` kapcsolók a helyileg hiányzó opcionális függőségek kihagyására szolgáltak; nem általánosan kötelező beállítások. A sikeres helyi eredmény: `scons: done building targets.`

A Windows-szerkesztő a forrásfa `bin/` mappájában található. Ne írd felül vele az eredeti Godot-telepítést.

## Mit kell még ellenőrizni a nyilvános kiadás előtt?

1. A `.po` munkafájlok és a tényleges, Godotba beépített `hu.po` tartalmának egyezése.
2. Több osztály magyar szövegeinek megjelenése (pl. Node2D, TextEdit, TileMapLayer); angol visszaesések feljegyzése.
3. ZIP-kiadás tesztelése külön, tiszta Windows-mappából.
4. Verzió és eredet feltüntetése, licenc- és szerzői jogi nyilatkozatok ellenőrzése.
5. A tervezett kiadás egyértelmű jelölése: **nem hivatalos, részleges magyarítás**.

A cél az, hogy a végfelhasználónak később már ne kelljen MSYS2-t, SConsot vagy C++-fordítót telepítenie.
