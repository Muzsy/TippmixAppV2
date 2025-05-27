### Képernyő Struktúra

1. **AppBar**
   - Alkalmazás neve vagy logója
   - Menü ikon vagy vissza gomb
   - Beállítások ikon

2. **Üdvözlő szöveg és TippCoin egyenleg**
   - Üdvözlő üzenet a felhasználónak
   - TippCoin egyenleg kijelző

3. **Fogadási események listája**
   - Mozgó kártyák formájában megjelenített események
   - Kártyák tartalma:
     - Esemény neve
     - Esemény időpontja
     - Részletek gomb

### Kezelt Adatok

- Felhasználó neve és TippCoin egyenleg
- Fogadási események listája (név, időpont, részletek)
- Lokalizációs adatok

### Létrejövő Fájlok (előzetes becslés)

1. **UI komponens fájlok**
   - AppBar komponens
   - Üdvözlő és TippCoin kijelző komponens
   - Fogadási esemény kártya komponens

2. **Adatkezelő fájlok**
   - Felhasználói adatok kezelése
   - Események adatainak kezelése

3. **Stílus fájlok**
   - Általános stílusok
   - Kártyák stílusai

4. **Lokalizációs fájlok**
   - Nyelvi fordítások

### Edge Case-ek

- Nincs elérhető fogadási esemény
- Felhasználó TippCoin egyenlege 0
- Hálózati hiba esetén az események nem töltődnek be

### Lokalizációs Kulcsok Prefixe

- `main_screen_`

### Tesztelhetőség Fő Szempontjai

- Felhasználói felület elemeinek helyes megjelenítése különböző képernyőméreteken
- Adatok helyes betöltése és megjelenítése
- Interakciók (pl. kártyákra kattintás) megfelelő működése
- Hibaüzenetek és edge case-ek kezelése
- Lokalizációs tesztek különböző nyelveken