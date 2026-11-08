# Godot HUN 4.7.2 – első privát tesztkiadás

**Tervezett címke:** `4.7.2-hu-test.1`  
**Állapot:** előzetes / tesztkiadás  
**Nyilvános kiadás:** még nincs jóváhagyva

## Mi készült el?

- A Godot Engine 4.7.2-stable Windows x86_64 módosított, külön összeállított szerkesztője.
- Részleges magyar beépített F1-osztálysúgó. A `Node2D` leírását és több metódusát sikeresen ellenőriztük magyarul.
- Egyetlen EXE-fájl, amely önállóan elindult az eredeti fordítási mappától függetlenül.
- `LICENSE.txt`, `COPYRIGHT.txt` és magyar `OLVASS_EL_Godot_HUN_4.7.2.txt` a ZIP-ben.

## Helyi ellenőrzések (2026-11-08)

- [x] SCons-fordítás sikeres: `scons: done building targets.`
- [x] A szerkesztő elindult a külön biztonsági mentésből.
- [x] A Node2D osztály magyar dokumentációja megjelent.
- [x] A négyfájlos ZIP sértetlen (`unzip -t`).
- [x] A ZIP-ből új helyre kicsomagolt EXE elindult a felhasználó Windows-gépén.
- [ ] Teszt külön, tiszta Windows-környezetben.
- [ ] Teljesebb fordítási és működési teszt.
- [ ] A terjesztett komponensek licenc- és attribúciós feltételeinek végleges ellenőrzése.
- [ ] A nyilvános közzététel kifejezett jóváhagyása.

## Tartalom

`Godot-HUN-4.7.2-Teszt.zip` – helyben elkészített ZIP. A ZIP-et **még nem töltöttük fel GitHub Release-hez**.

A ZIP-ben:
- `Godot-HUN-4.7.2-Teszt/godot.windows.editor.x86_64.exe`
- `Godot-HUN-4.7.2-Teszt/LICENSE.txt`
- `Godot-HUN-4.7.2-Teszt/COPYRIGHT.txt`
- `Godot-HUN-4.7.2-Teszt/OLVASS_EL_Godot_HUN_4.7.2.txt`

## Korlátok

A fordítás **nem teljes**. Több osztály angol, az Inspector számos tulajdonságcsoportja szintén angol. A kódazonosítókat szándékosan nem fordítjuk le.

A hivatalos Godot Engine fejlesztésétől független közösségi kísérlet. Ne állítsuk be hivatalos Godot-kiadásként.
