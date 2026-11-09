# Godot HUN 4.7.2 – a magyar munkafordítás állapotfelmérése

**Felmérés dátuma:** 2026. november 9.  
**Vizsgált források:** `forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po` és `forditas/TextEdit_4_7_2_hu_reszlet.po`.

## Ellenőrizhető eredmények

- Az összevont PO-ban **2185** eltérő, nem üres angol `msgid` és mindegyikhez nem üres magyar `msgstr` található.
- **96** Godot-osztályhoz rendelhető bejegyzés szerepel.
- Az osztályhoz rendelt **`brief`** mező 94 esetben, **`description`** mező 91 esetben szerepel.
- A külön TextEdit-katalógusban **292** bejegyzés van; ezeknek mind a 292 angol–magyar szövegpárja megtalálható a közös katalógusban (**0 eltérés**).
- A közös katalógusban **238** bejegyzés van kifejezetten `TextEdit.*` címkével. A külön TextEdit-katalógus további **54** bejegyzése más osztály címkéje alatt szerepel a közös katalógusban. Ez az azonos angol szövegek (`msgid`-ek) összevonásával magyarázható; **nem 54 hiányzó fordítás**.
- A két PO **munkakatalógus**, nem a teljes Godot-szerkesztő magyar felülete és nem a Windows EXE tételes tartalomjegyzéke.

## Bejegyzések eloszlása osztályonként

| Az osztályhoz rendelt bejegyzések száma | Osztályok száma |
| --- | ---: |
| 1–5 | 29 |
| 6–19 | 32 |
| 20–49 | 28 |
| 50–99 | 2 |
| 100+ | 5 |

**Megjegyzés:** a kevés bejegyzés nem feltétlenül jelent hiányos osztályt. A `msgid`-ek közösítéséből adódóan ugyanazt az angol mondatot több osztály is használhatja, miközben a közös PO csak egy osztály alatt sorolja fel.

## Teljes osztálylista – fordítások száma a munkakatalógusban

| Osztály | Bejegyzés | `brief` | `description` |
| --- | ---: | :---: | :---: |
| `TextEdit` | 238 | — | igen |
| `NavigationServer2D` | 138 | igen | — |
| `PopupMenu` | 124 | igen | igen |
| `LineEdit` | 123 | igen | igen |
| `ItemList` | 110 | igen | igen |
| `TabBar` | 96 | igen | igen |
| `TileSet` | 87 | igen | igen |
| `TileMapLayer` | 47 | igen | igen |
| `OptionButton` | 45 | igen | igen |
| `TabContainer` | 44 | igen | igen |
| `SpinBox` | 43 | igen | igen |
| `Label` | 40 | igen | igen |
| `MenuBar` | 39 | igen | igen |
| `CharacterBody2D` | 35 | igen | igen |
| `Curve` | 33 | igen | igen |
| `NavigationPolygon` | 30 | igen | igen |
| `SplitContainer` | 30 | igen | igen |
| `BaseButton` | 28 | igen | igen |
| `Camera2D` | 26 | igen | — |
| `AnimationNodeStateMachine` | 25 | igen | igen |
| `CollisionObject2D` | 25 | igen | igen |
| `Node2D` | 25 | igen | igen |
| `Polygon2D` | 25 | igen | igen |
| `ScrollContainer` | 25 | igen | igen |
| `AnimationPlayer` | 24 | igen | igen |
| `Curve2D` | 24 | igen | igen |
| `NavigationAgent2D` | 24 | igen | igen |
| `AudioStreamPlayer2D` | 22 | igen | igen |
| `Line2D` | 22 | igen | igen |
| `Animation` | 21 | igen | — |
| `TileSetAtlasSource` | 21 | igen | — |
| `Area2D` | 20 | igen | igen |
| `LinkButton` | 20 | igen | igen |
| `RayCast2D` | 20 | igen | igen |
| `SpriteFrames` | 20 | igen | igen |
| `Light2D` | 19 | igen | igen |
| `TileData` | 19 | igen | igen |
| `AnimatedSprite2D` | 18 | igen | igen |
| `NavigationRegion2D` | 17 | igen | igen |
| `ProgressBar` | 17 | igen | igen |
| `NavigationLink2D` | 16 | igen | igen |
| `Gradient` | 15 | igen | igen |
| `KinematicCollision2D` | 15 | igen | igen |
| `NavigationPathQueryParameters2D` | 15 | igen | igen |
| `ScrollBar` | 15 | igen | igen |
| `NavigationObstacle2D` | 14 | igen | igen |
| `NinePatchRect` | 13 | igen | igen |
| `Sprite2D` | 13 | igen | igen |
| `CheckBox` | 12 | igen | igen |
| `Parallax2D` | 12 | igen | igen |
| `TileMapPattern` | 12 | igen | igen |
| `TileSetScenesCollectionSource` | 12 | igen | — |
| `CheckButton` | 10 | — | igen |
| `GradientTexture2D` | 10 | igen | igen |
| `PathFollow2D` | 9 | igen | igen |
| `CollisionShape2D` | 8 | igen | igen |
| `NavigationPathQueryResult2D` | 8 | igen | igen |
| `PhysicsBody2D` | 8 | igen | igen |
| `RemoteTransform2D` | 8 | igen | igen |
| `AnimationTree` | 7 | igen | igen |
| `CollisionPolygon2D` | 7 | igen | igen |
| `AspectRatioContainer` | 6 | igen | igen |
| `BoxContainer` | 6 | igen | igen |
| `ButtonGroup` | 6 | igen | igen |
| `FlowContainer` | 6 | igen | igen |
| `MarginContainer` | 6 | igen | igen |
| `PointLight2D` | 6 | igen | igen |
| `CurveTexture` | 5 | igen | igen |
| `CurveXYZTexture` | 5 | igen | igen |
| `GridContainer` | 5 | igen | igen |
| `LightOccluder2D` | 5 | igen | igen |
| `MenuButton` | 5 | igen | igen |
| `OccluderPolygon2D` | 5 | igen | igen |
| `StaticBody2D` | 5 | igen | igen |
| `TextureRect` | 5 | igen | igen |
| `VisibleOnScreenNotifier2D` | 5 | igen | igen |
| `DirectionalLight2D` | 4 | igen | igen |
| `HScrollBar` | 4 | igen | igen |
| `VisibleOnScreenEnabler2D` | 4 | igen | igen |
| `VScrollBar` | 4 | igen | igen |
| `AnimatableBody2D` | 3 | igen | igen |
| `CanvasModulate` | 3 | igen | igen |
| `CenterContainer` | 3 | igen | igen |
| `ColorRect` | 3 | igen | igen |
| `GradientTexture1D` | 3 | igen | igen |
| `Panel` | 3 | igen | igen |
| `PanelContainer` | 3 | igen | igen |
| `Path2D` | 3 | igen | igen |
| `HBoxContainer` | 2 | igen | igen |
| `HFlowContainer` | 2 | igen | igen |
| `HSlider` | 2 | igen | igen |
| `HSplitContainer` | 2 | igen | igen |
| `VBoxContainer` | 2 | igen | igen |
| `VFlowContainer` | 2 | igen | igen |
| `VSlider` | 2 | igen | igen |
| `VSplitContainer` | 2 | igen | igen |

## Mit nem lehet ebből a két fájlból megállapítani?

1. **Nem számolható tényleges százalékos lefedettség**, amíg nincs a Godot 4.7.2-stable teljes angol osztályreferencia-katalógusával készített összehasonlítás. Az itt hiányzó eredeti angol szövegek nincsenek felsorolva a munkafájlban.
2. A jelenleg tárolt PO az első nyilvános `4.7.2-hu-test.1` EXE fordítása után is változott. Nem állítható, hogy minden mai `msgstr` már a kiadott programban van.
3. A Godot szerkesztőjének menüi, Inspector-mezői és eszköztippjei részben **másik lokalizációs rétegből** származnak; ezek lefedettségére ez az F1-katalógus nem ad arányszámot.
4. Egy `brief` vagy `description` megléte nem jelenti az adott osztály összes metódusának, tulajdonságának vagy jelzésének lefordítását.

## A következő felmérési lépés

A Godot **ugyanazon 4.7.2-stable** forrásverziójának teljes angol `doc/classes/*.xml` osztályreferenciáját kell összevetni a `msgid` szövegekkel. Ezután készíthető pontos lista azokról a F1-bejegyzésekről, amelyek még nem szerepelnek a magyar katalógusban. A hiánylistát érdemes külön kezelni az Inspector/tooltip/szerkesztőfelület fordításától.

**A nyilvános 4.7.2-hu-test.1 ZIP változatlan.** Ez a felmérés kizárólag a GitHubon tárolt munkakatalógus alapján készült.
