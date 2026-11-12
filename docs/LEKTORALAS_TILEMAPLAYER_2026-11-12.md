# Godot 4.7.2 – TileMapLayer lektorálási javaslatok (2026-11-12)

Ez a jegyzet a `forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po` állomány GitHubon ellenőrzött `TileMapLayer`-bejegyzéseihez készült. **Javaslatlista, nem beépített fordítás**; a PO-katalógust egyelőre változatlanul hagyjuk.

## Pontosítandó szövegek

| Azonosító | Jelenlegi magyar szöveg | Javasolt magyar szöveg | Indok |
| --- | --- | --- | --- |
| `TileMapLayer.occlusion_enabled` | Engedélyezi vagy letiltja a fény kitakarását. | Engedélyezi vagy letiltja a fénykitakarást. | Természetesebb, egységes szakkifejezés. |
| `TileMapLayer.collision_enabled` | Engedélyezi vagy letiltja az ütközéseket. | Engedélyezi vagy letiltja az ütközéskezelést. | A kapcsoló működését pontosabban írja le. |
| `TileMapLayer.get_cell_source_id` | Visszaadja a [param coords] koordinátáknál található cella csempeforrás-azonosítóját. Ha a cella nem létezik, [code]-1[/code] értéket ad vissza. | Visszaadja a [param coords] koordinátájú cella csempeforrás-azonosítóját. Ha a cella nem létezik, [code]-1[/code] értéket ad vissza. | Rövidebb, magyarosabb megfogalmazás; jelölések változatlanok. |
| `TileMapLayer.navigation_enabled` | Ha [code]true[/code], a navigációs területek engedélyezve vannak. | Ha az értéke [code]true[/code], a navigációs területek engedélyezettek. | Teljesebb, gördülékenyebb mondat. |

## Ellenőrzési szempontok

- A `[param ...]`, `[code]`, `[method ...]`, `[member ...]` és osztályhivatkozások érintetlenek maradjanak.
- A `TileMapLayer`, `TileSet`, `RID` és GDScript-azonosítók ne legyenek lefordítva.
- A `TextEdit` külön katalógusának 292 bejegyzését ne számoljuk hozzá ismét az összevont katalógus 2185 bejegyzéséhez.
- A tényleges beépítés után fussanak az `ellenorzes.py --require-msgfmt` vizsgálatok, és a Godot F1-súgóban történjen megjelenítési próba.

**Állapot:** lektorálási javaslatok rögzítve; katalógusba még nem vezetve.
