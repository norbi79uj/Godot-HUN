# Godot HUN 4.7.2 – lektorált 10. tesztváltozat előkészítése

**Állapot:** építési útmutató, még nem futtatott új EXE. Nem hivatalos, részleges magyar F1-súgó.

## Biztonság

- Az eredeti Godot telepítést és az előző sikeres EXE-t **ne írd felül**.
- Az alapul szolgáló fordítás változatlan: `forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po`.
- Az új munkafordítás: `forditas/Godot_4_7_2_hu_LEKTORALT_10.po` (2188 szöveg, 77 módosított bejegyzés, 78 célzott csere).
- A jobb oldali Inspector felületi címkéi ettől a PO-tól nem lesznek teljesen magyarok; ez a beépített F1-osztálysúgó fordítása.

## 1. Fordítás validálása

A Godot-HUN tárhely friss másolatában, olyan terminálban, ahol Python és `msgfmt` elérhető:

```bash
python forditas/ellenorzes_lektoralt.py
```

Az ellenőrzőprogram ellenőrzi a 2188 kulcsot, a 77 ténylegesen módosított szöveget, az eredeti F1-hivatkozásokat és a gettext szintaxist. A GitHub Actions automatikusan elvégzi ezt a vizsgálatot a tárolt PO-n.

## 2. Külön Godot 4.7.2-stable forrásmappa

A már korábban tesztelt Windows-környezet: MSYS2 UCRT64, C++/MinGW, Python, SCons.

**Az új teszthez a működő forrásmappából készíts külön másolatot**, például:

`C:\GodotHU-Test\godot-4.7.2-lektoralt10`

A források verziója maradjon **4.7.2-stable**; ne keverd újabb Godot-forrásba!

## 3. A lektorált PO bemásolása

A Godot-HUN tárhely `forditas/Godot_4_7_2_hu_LEKTORALT_10.po` fájlját másold az új Godot-forrásmásolatban ide:

`doc/translations/hu.po`

Ezt a helyet a korábbi Windows-tesztnél már kipróbáltuk. A forrásmásolatban meglévő `hu.po` állományról előbb készíts biztonsági mentést, vagy használj teljesen külön forrásmappát.

## 4. Fordítás MSYS2 UCRT64 terminálból

Az új forrásmásolat gyökerében:

```bash
scons platform=windows target=editor arch=x86_64 use_mingw=yes accesskit=no d3d12=no angle=no winrt=no -j4
```

A korábbi próba ezzel a paranccsal sikerült. A sikeres build végén a Windows-EXE a `bin/` könyvtárban jelenik meg.

## 5. F1 ellenőrzőpróba

- A frissen fordított szerkesztőt **külön** indítsd.
- F1-ben nézd meg: `Node2D`, `TileSet`, `Sprite2D`, `AnimationPlayer`, `CharacterBody2D`, `Area2D`, `Camera2D`, `LightOccluder2D`.
- Nézd meg, hogy a módosított magyar leírások láthatók-e és a linkek kattinthatók-e.
- Ha a program nem indul, ne módosítsd a régi működő EXE-t; a fordítóhiba naplója alapján javítsunk.

## 6. Tesztkiadás csomagolása

Új mappába csomagold az EXE-t és az eredeti projekt előírt licenceit/attribúcióit. **A korábbi kiadást ne módosítsd!** Nyilvános közzététel csak külön jóváhagyás, licencellenőrzés és Windows-teszt után.

A dokumentum előkészítés: új Windows EXE-t nem állítottunk elő a felhőben.
