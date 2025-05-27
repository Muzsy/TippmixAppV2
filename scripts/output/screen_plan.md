### Képernyő Struktúra

1. **AppBar**
   - Alkalmazás neve vagy logó
   - Menü ikon vagy profil ikon

2. **Üdvözlő Szöveg**
   - Dinamikus üdvözlő üzenet a felhasználó nevével

3. **TippCoin Egyenleg**
   - Jelenlegi TippCoin egyenleg megjelenítése

4. **Fogadási Események Listája**
   - Mozgó kártyák formájában megjelenített események
   - Kártyánként megjelenítendő adatok:
     - Esemény neve
     - Esemény időpontja
     - Résztvevő csapatok vagy játékosok
     - Fogadási lehetőségek

### Kezelt Adatok

- Felhasználó neve és TippCoin egyenleg
- Fogadási események adatai:
  - Esemény azonosító
  - Esemény neve
  - Időpont
  - Résztvevők
  - Fogadási lehetőségek és szorzók

### Létrejövő Fájlok (előzetes becslés)

1. **UI komponens fájlok**
   - AppBar komponens
   - Üdvözlő szöveg komponens
   - TippCoin egyenleg komponens
   - Fogadási esemény kártya komponens

2. **Adatkezelő fájlok**
   - Felhasználói adatok kezelése
   - Események adatainak kezelése

3. **Stílus fájlok**
   - Általános stílusok
   - Kártya stílusok

4. **Lokalizációs fájlok**
   - Nyelvi fordítások

### Edge Case-ek

- Üres eseménylista kezelése
- Hibás vagy hiányzó felhasználói adatok
- Események adatainak frissítése közben fellépő hibák
- TippCoin egyenleg változásának kezelése

### Lokalizációs Kulcsok Prefixe

- `mainScreen.`

### Tesztelhetőség Fő Szempontjai

- UI elemek helyes megjelenítése különböző képernyőméreteken
- Fogadási események helyes betöltése és frissítése
- Felhasználói interakciók (pl. kártyára kattintás) helyes működése
- Lokalizációs szövegek helyes megjelenítése különböző nyelveken
- Hibakezelés és edge case-ek megfelelő kezelése