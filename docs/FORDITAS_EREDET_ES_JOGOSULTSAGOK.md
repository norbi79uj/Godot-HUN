# Godot HUN – fordításszövegek eredetének ellenőrzése

**Ellenőrzés:** 2026. november 8.  
**Érintett verzió:** Godot 4.7.2, részleges magyar F1-osztálysúgó.

## Milyen fájlokat vizsgáltunk?

- `forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po`
- `forditas/TextEdit_4_7_2_hu_reszlet.po`
- `forditas/ellenorzes.py`

Ezeket az állományokat az előző `Smaragd-Editor` projekttárból **másolatként** hoztuk át, az eredeti tárhely módosítása nélkül.

## Tényszerűen ellenőrizhető adatok

- Az összevont katalógus **2185 különböző, nem üres `msgid`-et** tartalmaz.
- Mind az **2185** bejegyzésben van nem üres magyar `msgstr`; az egyező `msgid`-ekből nincs duplikátum.
- Minden bejegyzéshez szerepel forráshivatkozás, például `#: doc/classes/TileMapLayer.xml`.
- A `TextEdit` különálló 292 bejegyzése az összevont katalógus részhalmaza; **nem** további 292 külön fordítás.
- A PO fejlécében `Last-Translator: Hungarian translation working draft` szerepel, **nem konkrét szerzői lista**.
- Az összevont fájl elején szereplő régi munkamegjegyzés még „nem tesztelt” állapotra utal; ez **elavult**: 2026-11-08-án a Windows-tesztbuildben a `Node2D` F1-súgó magyar szövegeit ténylegesen kipróbáltuk. Ez **nem** jelent minden egyes bejegyzésre kiterjedő tesztet.

## Alapul szolgáló angol anyag jogi státusza

A Godot Engine hivatalos `godot-editor-l10n` repója szerint a szerkesztő és osztályreferencia katalógusainak `msgid` és `msgstr` tartalma **MIT-licencű**.

Forrás: https://github.com/godotengine/godot-editor-l10n

A Godot motor eredeti licencét és a beépített harmadik fél könyvtárak adatait az összeállított ZIP-ben a `LICENSE.txt` és `COPYRIGHT.txt` tartalmazza.

## A saját magyar fordításszövegek

A projektgazda **jóváhagyta az MIT-licenc elvét**, és vállalta, hogy a Godot HUN saját terjesztési felületén a magyarítás ingyenesen elérhető lesz, mások kereskedelmi újrafelhasználását ugyanakkor az MIT nem tiltja.

### Tisztázandó pontok a nyilvános kiadás előtt

- [ ] A magyar `msgstr` szövegek keletkezésének / átvételének nyomon követése, ideértve az esetleges külső fordítások és közreműködők azonosítását.
- [ ] A jogosultak tényleges hozzájárulása minden olyan szövegrészhez, amely nem kizárólag a projektgazda saját munkája vagy jogszerűen újrahasznosítható MIT-tartalom.
- [ ] A `forditas/` könyvtár licencét és hozzájárulási szabályait egyértelműen rögzítő végleges fájl.
- [ ] Közzététel előtt a csomag végső attribúciós és működési ellenőrzése.

**Fontos:** A PO-fájl fejlécéből és a korábbi tesztekből nem állapítható meg teljes bizonyossággal, hogy a 2185 magyar fordítás mindegyike önálló eredetű. Ezt nem szabad kész tényként állítani.

## Közösségi elv

A tervezett MIT-licenc esetén a külső közreműködőket előre tájékoztatjuk: az általuk beküldött, elfogadott fordításokat ugyanilyen nyílt licenc alatt kívánjuk terjeszteni. Az első nyilvános megnyitás előtt a projektdokumentációt ennek megfelelően véglegesítjük.
