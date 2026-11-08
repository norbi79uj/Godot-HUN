# Kiadási szöveg – Godot HUN 4.7.2-hu-test.1

> **ELŐKÉSZÍTETT SZÖVEG – NEM PUBLIKÁLT KIADÁS.**
>
> Ezt a dokumentumot a későbbi GitHub Release-hez készítettük. A Release jelenleg piszkozat, a tárhely privát. Nyilvános megosztáshoz külön jóváhagyás és a függő ellenőrzések lezárása kell.

## Godot HUN 4.7.2 – első részleges magyar F1-teszt

A **Godot HUN** a Godot Engine **4.7.2-stable** forrására épülő **nem hivatalos**, Windows x86_64 tesztváltozat. A cél, hogy a Godot beépített **F1 osztályreferenciája** fokozatosan magyarul legyen olvasható.

### Mit tartalmaz?

- Külön összeállított Godot Windows-szerkesztőt.
- **Részleges magyar F1-súgót**: például a `Node2D` osztály magyar leírása és több metódusmagyarázata már működő tesztben megjelent.
- Eredeti `LICENSE.txt` és `COPYRIGHT.txt` dokumentumokat, valamint egy magyar `OLVASS_EL_Godot_HUN_4.7.2.txt` útmutatót.
- A GitHubon külön `.po` munkafájlokat a fordítás további javításához.

### Mi NEM része?

- **Nem teljes Godot-magyarítás.** Számos F1-osztály és Inspector-felirat még angol.
- Nem hivatalos Godot Engine-kiadás, és nem a Godot fejlesztőinek támogatott terméke.
- Nem bizonyított, hogy minden számítógépen, Windows-verzión vagy grafikus környezetben hibamentesen fut.

### Használat

1. Töltsd le a `Godot-HUN-4.7.2-Teszt.zip` fájlt **a később közzétett kiadásból**.
2. Csomagold ki egy saját, új mappába; **ne írd felül** a jelenlegi Godot-telepítésedet.
3. Indítsd a `godot.windows.editor.x86_64.exe` fájlt.
4. A Godot F1 osztályreferenciájában keresd meg például a `Node2D` osztályt.

A tesztverzió használata előtt érdemes biztonsági mentést készíteni a fontos projektekről.

### Ellenőrzött adatok

- ZIP: `Godot-HUN-4.7.2-Teszt.zip`
- Méret: **81 579 340 bájt**
- SHA-256: `aa421ee6dc8accf65c4f1b05f3594d3e9eec2db5d0a8b09657433990bd14533e`
- A helyi Windows-próbán az EXE elindult és a `Node2D` F1-fordítása megjelent. Ez nem általános kompatibilitási garancia.

### Licenc és hozzáférés

A Godot motor eredeti MIT-licencének és a kapcsolódó harmadik fél komponensek jogi nyilatkozatainak megőrzése kötelező. A Godot HUN saját fordítási hozzájárulásainak MIT-licencnyilatkozata: [LICENSE-TRANSLATIONS.txt](../LICENSE-TRANSLATIONS.txt).

A projekt **a saját letöltési helyén mindig ingyenesen** kívánja hozzáférhetővé tenni ezt a magyarítást. Az MIT-licenc azonban nem zárja ki mások kereskedelmi továbbfelhasználását.

### Hibajelzés és közreműködés

A később nyilvános GitHub-tárhelyen az **Issues** fülön lehet majd bejelenteni a fordítási hibákat. A hibajelentésben kérjük a Godot verzióját, az F1-osztály nevét, az angol szöveget, a hibás magyar mondatot és a javasolt javítást.

További útmutató: [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## Kiadás előtti teendők

- [x] A release-csomag feltöltése és digitális egyezésének ellenőrzése.
- [x] A projekt ingyenes hozzáférési elvének és saját fordítási MIT-nyilatkozatának dokumentálása.
- [x] A tesztkiadás ismert korlátainak egyértelmű megfogalmazása.
- [ ] Külső komponensek és fordítási eredet szükséges jogi ellenőrzéseinek lezárása.
- [ ] Szükség esetén további kompatibilitási próba, illetve a még nem próbált részek világos megjelölése.
- [ ] A projektgazda külön engedélye a publikus GitHub-tárhelyre és a kiadás publikálására.
