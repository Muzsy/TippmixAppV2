## Képernyő Struktúra

### Főképernyő elemei:
1. **AppBar**
   - Alkalmazás neve
   - Menü ikon vagy vissza gomb
   - Beállítások ikon

2. **Üdvözlő szöveg**
   - Dinamikus szöveg, amely köszönti a felhasználót

3. **TippCoin egyenleg**
   - Jelenlegi egyenleg megjelenítése
   - Frissítés gomb

4. **Fogadási események listája**
   - Mozgó kártyák formájában
   - Minden kártya tartalmazza:
     - Esemény neve
     - Időpont
     - Résztvevő csapatok/játékosok
     - Fogadási lehetőségek

### Kezelt adatok:
- Felhasználói adatok (név, TippCoin egyenleg)
- Fogadási események adatai (esemény neve, időpont, résztvevők, fogadási lehetőségek)
- Lokalizációs adatok

### Létrejövő fájlok (előzetes becslés):
1. **UI fájlok**
   - `main_screen.dart`: A főképernyő felépítése
   - `event_card.dart`: A fogadási esemény kártya komponens

2. **Adatkezelés**
   - `user_data.dart`: Felhasználói adatok kezelése
   - `event_data.dart`: Fogadási események kezelése

3. **Lokalizáció**
   - `localization.dart`: Lokalizációs kulcsok és szövegek

4. **Tesztelés**
   - `main_screen_test.dart`: Tesztesetek a főképernyőhöz
   - `event_card_test.dart`: Tesztesetek az esemény kártyához

### Edge case-ek:
- Nincs elérhető fogadási esemény
- Hálózati hiba esetén nem töltődnek be az adatok
- Felhasználói egyenleg frissítése sikertelen
- Nem támogatott nyelvi beállítás

### Lokalizációs kulcsok prefixe:
- `main_screen_`

### Tesztelhetőség fő szempontjai:
- UI elemek helyes megjelenítése különböző képernyőméreteken
- Adatok helyes betöltése és megjelenítése
- Felhasználói interakciók (pl. kártyára kattintás) helyes kezelése
- Hibaüzenetek és edge case-ek megfelelő kezelése
- Lokalizációs szövegek helyes megjelenítése különböző nyelveken