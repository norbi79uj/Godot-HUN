# Godot HUN – Lektorált 30: Control audit

Dátum: 2026-11-11
Kiinduló fájl: `Godot_4_7_2_hu_LEKTORALT_29.po`
Ellenőrzött fájl: `Godot_4_7_2_hu_LEKTORALT_30.po`

## Eredmények

- Összes nem üres msgid-bejegyzés: 2679.
- Control.xml hivatkozású bejegyzés: 180.
- Egyedi Control-kulcs: 144.
- Többszörös Control-kulcs: 36; mindegyik párnál a két msgid szóközöket/sortöréseket egységesítve azonos szöveg.
- Teljes katalógusban ismételt msgid: 0.
- BBCode/Godot jelöléseltérés: 0 (a katalógus egyszerű, szögletes zárójeles jelöléseire végzett összevetés szerint).
- Korábbi fordítások: mind a 2679 változatlan, új fordítás nincs.

## Figyelmet igénylő rész

A 36 Control-kulcs két, eltérő sortörésekkel vagy szóközökkel tárolt angol msgid-t tartalmaz. A gettext ezeket külön szövegként kezeli, ezért az automatikus összevonás adatvesztést vagy forrásverziós eltérést okozhat. Egyelőre mindkét megfogalmazást megtartottuk. A 4.7.2 célverzió eredeti dokumentációjával külön ellenőrizni kell, melyik változat fordul elő a tényleges buildben.

## Korlátok

Ez szöveges, szerkezeti audit; nem helyettesíti a `msgfmt --check`, a Godot fordítási pipeline, az F1-súgó megjelenítési próbáját és a Windows-build tesztjét. A jelen katalógus továbbra is részleges munkaváltozat, nem hivatalos teljes magyarítás.
