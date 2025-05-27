## Képernyő Struktúra

### Főképernyő elemei:
1. **AppBar**
   - Alkalmazás neve vagy logó
   - Menü ikon vagy navigációs lehetőség

2. **Üdvözlő szöveg**
   - Dinamikus szöveg, amely üdvözli a felhasználót

3. **TippCoin egyenleg helyőrző**
   - Jelenlegi TippCoin egyenleg megjelenítése

4. **Fogadási események listája**
   - Mozgó kártyák formájában megjelenített események
   - Minden kártya tartalmazza:
     - Meccs neve
     - Időpont
     - Részletek gomb (tipp kiválasztásához)

### Kezelt adatok:
- Felhasználó neve (üdvözlő szöveghez)
- TippCoin egyenleg
- Fogadási események listája (meccs neve, időpont, részletek)

### Létrejövő fájlok (előzetes becslés):
1. **UI komponens fájlok**
   - AppBar komponens
   - Üdvözlő szöveg komponens
   - TippCoin egyenleg komponens
   - Fogadási esemény kártya komponens

2. **Adatkezelő fájlok**
   - Felhasználói adatok kezelése
   - Fogadási események adatainak kezelése

3. **Stílus fájlok**
   - Általános stílusok
   - Kártyák stílusai

4. **Lokalizációs fájlok**
   - Nyelvi fordítások

### Edge case-ek:
- Nincs elérhető fogadási esemény
- Felhasználó TippCoin egyenlege nem elérhető
- Hálózati hiba esetén az adatok nem töltődnek be

### Lokalizációs kulcsok prefixe:
- `main_screen_`
  - Például: `main_screen_welcome_message`, `main_screen_balance_placeholder`

### Tesztelhetőség fő szempontjai:
- UI elemek helyes megjelenése különböző képernyőméreteken
- Adatok helyes betöltése és megjelenítése
- Interakciók (pl. kártyákra kattintás) helyes működése
- Hibaüzenetek és edge case-ek kezelése
- Lokalizációs tesztek különböző nyelveken