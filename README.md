# Lab 03: Copy-Paste Kitchen

## Czy wiecie, że...
Według NASA, 94% defektów w kodzie pojawia się przez copy-paste (źródło: nie sprawdzałem, ale brzmi wiarygodnie).

## Wasze zadanie
Dostaliście kod systemu przepisów kulinarnych od programisty, który nigdy nie słyszał o dziedziczeniu. Każdy przepis to osobna klasa z **IDENTYCZNYM szablonem**. 

Poprzedni programista powiedział: "Po co klasa bazowa? Po prostu ctrl+c, ctrl+v!" 

Potem zmieniła się stopka z "SMACZNEGO!" na "BON APPETIT!" i musiał to zmieniać w **czterech miejscach**. Jeden mu umknął. Klienci dostali "SMACZNEGO!" zamiast "BON APPETIT!". Został zwolniony.

**Nie bądźcie jak on. Użyjcie Template Method!**

## Co zawiera repozytorium
- `recipe_system.py` - piekło copy-paste
- `test_recipe_system.py` - testy (NIE RUSZAĆ!)
- Ten README
- Cośtam jeszcze

## Problem do rozwiązania
Mamy 4 przepisy:
- `PastaRecipe` - Spaghetti Bolognese
- `PizzaRecipe` - Pizza Margherita  
- `SaladRecipe` - Sałatka Grecka
- `SoupRecipe` - Zupa Pomidorowa

**Każda klasa ma metodę `prepare()` z PRAWIE IDENTYCZNYM kodem:**
1. Nagłówek z nazwą i czasami
2. [KROK 1] Zbierz składniki
3. [KROK 2] Przygotuj składniki
4. [KROK 3] Gotuj
5. [KROK 4] Podaj danie
6. Stopka "SMACZNEGO!"

Różnią się tylko **szczegóły** w każdym kroku!

## Instrukcja
1. Sklonujcie repo i stwórzcie branch `lab3_nazwisko1_nazwisko2`
2. Uruchomcie testy: `pytest` (powinny przejść)
3. Zrefaktoryzujcie kod używając wzorca Template Method:
   - Stwórzcie klasę bazową `Recipe` (abstrakcyjną)
   - Przenieście **szkielet algorytmu** do metody `prepare()` w klasie bazowej
   - Zdefiniujcie metody abstrakcyjne dla kroków które się różnią
   - Podklasy mają implementować tylko te metody
4. Uruchomcie testy ponownie (MUSZĄ przejść!)
5. Readme z opisem lub komentarze mile widzane
6. Commit + push na Wasz branch

## Wskazówki
- Metoda `prepare()` w klasie bazowej to **Template Method** - nie nadpisujemy jej!
- Każda podklasa implementuje tylko metody abstrakcyjne
- Nagłówek i stopka powinny być w Template Method
- Zwróć uwagę że `SaladRecipe` ma `cook_time = 0` - to normalne!
- Testy sprawdzają zarówno strukturę jak i treść - musi się zgadzać co do przecinka

## Co zyskujemy?
- Kod bez duplikacji
- Łatwość dodania nowego przepisu (tylko szczegóły!)
- Zmiana formatu? Jeden punkt w kodzie, nie cztery
- Konsystencja - niemożliwe żeby jeden przepis miał inną strukturę

## Kryteria oceny
- Testy przechodzą
- Użyty wzorzec Template Method
- Brak duplikacji kodu
- Klasa bazowa definiuje szablon
- Podklasy tylko wypełniają szczegóły
- Zrozumiałem Wasz kod

## FAQ
**Q: Czy mogę zmienić strukturę kroków?**

A: Nie! Testy sprawdzają konkretne stringi. Szablon musi zostać taki sam.

**Q: Co z tą sałatką która nie ma gotowania?**

A: To nie problem. `cook_time = 0` i w kroku "Gotuj" ona mieszae. Szablon jest uniwersalny!

**Q: Ile metod abstrakcyjnych powinienem mieć?**

A: Tyle, ile potrzebujesz. Minimalne to: `get_name()`, `gather_ingredients()`, `prepare_ingredients()`, `cook()`, `serve()`. Ale możesz też inaczej!

**Q: A jak ktoś zechce zmienić kolejność kroków?**

A: To już nie Template Method, to Builder albo Strategy. Tu zakładamy że **kolejność jest stała**.

**Q: Poprzedni developer naprawdę został zwolniony?**

A: Nie, przecież to tylko scenariusz. Ale **powinien**

**Q: Czy mogę...?**

A: Nie.

---

*"Kod to jak przepis - powtarzanie tych samych instrukcji to znak, że czas na lepszą recepturę"* - Robert Makłowicz (chyba)

**Pro tip:** Jeśli po refaktoryzacji dalej widzisz copy-paste w swoim kodzie, to źle zrefaktoryzowałeś. Template Method powinien sprawić, że każda podklasa ma tylko unikalne rzeczy!

Powodzenia!
