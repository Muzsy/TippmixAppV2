# Fájl neve: project_blueprint.md
# Elérési út: /docs/blueprints/

# TippmixApp V2 - Projekt BluePrint (Home-First alapon)

Ez a dokumentum az AI agent által vezérelt fejlesztés alaptérképe. A projekt nem modulrendszerű, hanem képernyőalapú (anchor screen / home-first) stratégia szerint halad.

---

## Alapelv

- Minden fejlesztés egy **fő képernyőből** indul ki (pl. `home_screen`)
- Innen ágaznak el a komponensek: kártyák, logikák, szervizek, adatok
- Az AI mindig egy ilyen képernyőhöz kapcsolódó fájlokat generál
- Az adatok Firestore-ból érkeznek, az OddsAPI-ra alapozva

---

## 1. Aktuális fókusz: `home_screen`

### Cél:
- A felhasználó fogadási eseményeket lásson mozgó csempéken
- Rákattintva: tippelhet, szelvényt állíthat össze
- Lokalizált (HU/EN/DE), élő odds-szal

### Funkciók:
- Meccsek listázása
- Tippkártyák (könnyen kattintható)
- Navigáció szelvény összeállítóhoz
- Frissítés (pull to refresh / automatikus interval)

### Várható fájlok:
- `lib/screens/home_screen.dart`
- `lib/widgets/tip_card.dart`
- `lib/services/logic/home_service.dart`
- `lib/services/remote/match_service.dart`
- `lib/models/match_model.dart`, `tip_model.dart`
- `l10n/app_*.arb`
- `test/screens/home_screen_test.dart`

---

## 2. Architektúra

| Mappa | Cél |
|-------|-----|
| `screens/` | Képernyők (pl. home_screen, create_ticket_screen) |
| `widgets/` | Lokális vizuális elemek (pl. tip_card) |
| `models/` | Firestore-ra és OddsAPI-ra épülő adatmodellek |
| `services/logic/` | Állapotkezelés, feldolgozás |
| `services/remote/` | API hívások, adatletöltés |
| `test/` | Widget és logika tesztek |
| `l10n/` | Lokalizált kulcsok ARB formában |

---

## 3. Generálási szabályok
- Minden generált kód egyezzen a naming conventionökkel (snake_case Dartban)
- Csak azt generáljuk, ami az adott képernyőhöz tartozik
- Lokalizációs kulcs minden `Text` esetén
- Minden generált osztály tartalmazzon minimum kommentet (///)
- Teszt minden képernyőhöz automatikusan legyen előkészítve

---

## 4. További anchor screen-ek (később)
- `create_ticket_screen`
- `match_ticket_screen`
- `saved_tickets_screen`
- `profile_screen`
- `leaderboard_screen`

Minden ezekhez tartozó fejlesztés az `home_screen` használati igényei alapján indul.
