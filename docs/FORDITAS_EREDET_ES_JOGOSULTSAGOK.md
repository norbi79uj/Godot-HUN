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

## A magyar fordítás tényleges munkafolyamata

**A projektgazda visszajelzése (2026. november 8.):** a magyar `msgstr` szövegeket a ChatGPT asszisztens készítette a projektgazdával folytatott közös fordítási munkában. A projektgazda irányította a munkát, ellenőrizte a kimeneteket, és jóváhagyta az ingyenes, tervezetten MIT-licencű közzétételt.

- **Angol forrás:** a Godot 4.7.2 osztályreferenciája (`msgid`).
- **Magyar munkafordítás:** ChatGPT-vel generált és a projekt során szerkesztett magyar szöveg (`msgstr`).
- **Nyelvi alap:** általános magyar nyelvtudás, szótári és szaknyelvi fogalmak; ez önmagában nem jelent konkrét szótárból átmásolt, szerzői joggal védett szöveget.
- **Forráskezelés:** a fordítás és az angol szöveg nem tekinthető teljesen független műnek: az angol osztályreferencia alapján készült, ezért a Godot eredeti licencét és attribúcióit megőrizzük.
- **Korlát:** az AI-val készült fordítások pontos jogállása és az egyes szövegek esetleges más forrásokkal való egyezése nem állapítható meg pusztán a PO-fájlból. Nem állítjuk bizonyítatlanul, hogy mind a 2185 bejegyzés kizárólag saját, jogilag védett szerzői mű.

A projektgazda engedélyezi a projekt keretein belül létrehozott magyar munkafordítás közösségi felhasználását a tervezett MIT-feltételekkel, **amennyiben** nem sérülnek az alapanyag és esetleges harmadik felek jogai. A közösségi javítók saját hozzájárulásait külön szabályozzuk.

## A ChatGPT-kimenet felhasználásának feltételei – ellenőrizve

Az OpenAI közzétett felhasználási feltételei szerint a felhasználó és az OpenAI egymás közötti viszonyában a felhasználót illetik meg a kimenethez fűződő jogok a vonatkozó jogszabályok által megengedett mértékben; az OpenAI az esetleg őt megillető jogokat átruházza. Emiatt **önmagában a ChatGPT felhasználása miatt nem szükséges az OpenAI külön közzétételi engedélye**.

Ez **nem** szavatolja az AI-kimenet egyediségét, szerzői jogi védettségét vagy azt, hogy semmilyen részlete nem egyezhet más jogosult tartalmával. A projektgazda továbbra is felelős az alapul használt anyagok és harmadik felek jogainak tiszteletben tartásáért.

Források:
- OpenAI Terms of Use, „Your content”, „Ownership of content” és „Similarity of content”: https://openai.com/en-GB/policies/row-terms-of-use/
- Godot fordítási tárhely MIT-nyilatkozata: https://github.com/godotengine/godot-editor-l10n

**Következtetés:** a dokumentált munkafolyamat (Godot angol osztályreferencia → ChatGPT-asszisztált magyar fordítás → projektgazdai jóváhagyás) a megvizsgált feltételek alapján nem igényel külön OpenAI-licencet. Egy nem azonosított külső forrás esetleges jogát ez nem írja felül. Ez tájékoztató megfelelőségi megállapítás, nem jogi szakvélemény.

## Alapul szolgáló angol anyag jogi státusza

A Godot Engine hivatalos `godot-editor-l10n` repója szerint a szerkesztő és osztályreferencia katalógusainak `msgid` és `msgstr` tartalma **MIT-licencű**.

Forrás: https://github.com/godotengine/godot-editor-l10n

A Godot motor eredeti licencét és a beépített harmadik fél könyvtárak adatait az összeállított ZIP-ben a `LICENSE.txt` és `COPYRIGHT.txt` tartalmazza.

## A saját magyar fordításszövegek

A projektgazda **jóváhagyta az MIT-licenc elvét**, és vállalta, hogy a Godot HUN saját terjesztési felületén a magyarítás ingyenesen elérhető lesz, mások kereskedelmi újrafelhasználását ugyanakkor az MIT nem tiltja.

### Tisztázandó pontok a nyilvános kiadás előtt

- [x] A jelen projekt munkafolyamatának eredete dokumentálva: ChatGPT-asszisztált magyarítás a projektgazda irányításával.
- [x] A projektgazda dokumentálta, hogy a magyar munkafordítást ChatGPT-vel készítettük az MIT-licencű Godot angol szövege alapján; az OpenAI feltételeiben külön kimenet-felhasználási engedély nem szükséges.
- [ ] Ha konkrét, külső fordításból átvett részre utaló adat merül fel, annak jogosultságát külön tisztázni kell.
- [ ] A jogosultak tényleges hozzájárulása minden olyan szövegrészhez, amely nem kizárólag a projektgazda saját munkája vagy jogszerűen újrahasznosítható MIT-tartalom.
- [x] A saját fordításokhoz MIT-licencszöveg van a `LICENSE-TRANSLATIONS.txt` fájlban, a jövőbeni közreműködők feltételei a `CONTRIBUTING.md` dokumentumban szerepelnek.
- [ ] Közzététel előtt a csomag végső attribúciós és működési ellenőrzése.

**Fontos:** A munkafolyamat eredete a projektgazda beszámolója alapján ismert, de ebből önmagában nem következik, hogy minden egyes megfogalmazás jogilag kizárólagosan saját eredetű. A pontos jogosultságokat szükség esetén külön ellenőrizzük.

## Közösségi elv

A tervezett MIT-licenc esetén a külső közreműködőket előre tájékoztatjuk: az általuk beküldött, elfogadott fordításokat ugyanilyen nyílt licenc alatt kívánjuk terjeszteni. Az első nyilvános megnyitás előtt a projektdokumentációt ennek megfelelően véglegesítjük.
