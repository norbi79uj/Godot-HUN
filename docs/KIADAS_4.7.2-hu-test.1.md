# Godot HUN 4.7.2 – első privát tesztkiadás

**Tervezett címke:** `4.7.2-hu-test.1`  
**Állapot:** előzetes / tesztkiadás  
**Nyilvános kiadás:** még nincs jóváhagyva; a GitHub Release jelenleg piszkozat és a tárhely privát

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

`Godot-HUN-4.7.2-Teszt.zip` – helyben elkészített ZIP. A ZIP-et **feltöltöttük a privát GitHub Release-piszkozathoz**, de a kiadást még nem publikáltuk. A feltöltött fájl mérete **81 579 340 bájt**, SHA-256: `aa421ee6dc8accf65c4f1b05f3594d3e9eec2db5d0a8b09657433990bd14533e`.

A ZIP-ben:
- `Godot-HUN-4.7.2-Teszt/godot.windows.editor.x86_64.exe`
- `Godot-HUN-4.7.2-Teszt/LICENSE.txt`
- `Godot-HUN-4.7.2-Teszt/COPYRIGHT.txt`
- `Godot-HUN-4.7.2-Teszt/OLVASS_EL_Godot_HUN_4.7.2.txt`

## Korlátok

A fordítás **nem teljes**. Több osztály angol, az Inspector számos tulajdonságcsoportja szintén angol. A kódazonosítókat szándékosan nem fordítjuk le.

A hivatalos Godot Engine fejlesztésétől független közösségi kísérlet. Ne állítsuk be hivatalos Godot-kiadásként.

## Mi a következő lépés?

A dokumentáció és a licencszabályok pontosítása után a hátralévő, másik Windows-gépen végzett kompatibilitási próba és a többosztályos F1-fordítás ellenőrzése **későbbi tesztkörbe** tartozhat. Ezeket nem tekintjük teljesítettnek. Az első kiadást következetesen **nem hivatalos, részleges, előzetes tesztkiadásnak** kell nevezni. A nyilvános megosztás külön döntést és a jogi ellenőrzések lezárását igényli.

## A csomag sértetlenségének ellenőrzése

A GitHubon a `kiadasok/4.7.2-hu-test.1/SHA256SUMS.txt` tartalmazza a Release-hez feltöltött ZIP **SHA-256 ellenőrzőösszegét**. Ez a csomag sértetlenségét segít ellenőrizni, de önmagában nem hitelesíti a kiadó személyazonosságát, és nem helyettesíti a vírusellenőrzést.

Windows PowerShellben, a ZIP-et tartalmazó mappában:

```powershell
(Get-FileHash -Algorithm SHA256 -Path '.\\Godot-HUN-4.7.2-Teszt.zip').Hash.ToLower()
```

A kapott érték egyezzen a `SHA256SUMS.txt` első mezőjével. Ha nem egyezik, ne futtasd a letöltött programot.
