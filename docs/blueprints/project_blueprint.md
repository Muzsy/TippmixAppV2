Cím: [MVP] TippmixApp minimálisan működőképes verzió generálása

Kérlek, generáld le a TippmixApp alkalmazás első, minimálisan működőképes verzióját (MVP) a `project_blueprint.md` fájl alapján.

### Követelmények:

#### Képernyők:
- `home_screen.dart`: főoldal navigációs csempével („Fogadás indítása”)
- `match_ticket_screen.dart`: OddsAPI-ból beolvasott meccsek és kimenetelek listázása
- `create_ticket_screen.dart`: kiválasztott fogadásokból szelvény készítése

#### Modellek:
- `match_model.dart`, `selection_model.dart`
- `ticket_model.dart` (final struktúra szerint)

#### Szervizek:
- `match_service.dart`: Firestore-ból meccslista betöltés
- `ticket_service.dart`: szelvény validálás, beküldés

#### Funkciók:
- Szelvény csak egy fogadóiroda fogadásaiból állhat
- Beküldés csak akkor, ha még nem járt le a legkorábbi `commenceTime`
- Kötéstiltás logika: ne lehessen egy meccs több kimenetelét felvenni
- Beküldéskor a státusz `pending`, a nyeremény kiszámolva tárolva

#### Lokalizáció:
- `intl_hu.arb`, `intl_en.arb`, `intl_de.arb`
- Lokalizált kulcsok használata minden szöveghez

#### Teszt:
- Legalább 1 teszt minden `service` fájlhoz (`*_test.dart`)
- Modell validálás `ticket_model_test.dart`

### Elrendezés:
- `lib/screens/`, `lib/models/`, `lib/services/`, `lib/widgets/`
- `test/screens/`, `test/models/`, `test/services/`
- `l10n/` – lokalizációs fájlok

### Referencia:
Lásd: `docs/blueprints/project_blueprint.md`

---

**A cél:** Egy működőképes, buildelhető Flutter alkalmazás MVP szinten, amivel már lehet odds API eseményre szelvényt összeállítani és beküldeni.
