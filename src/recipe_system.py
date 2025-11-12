"""
System przepisow kulinarnych.
UWAGA: Ten kod ma MNÓSTWO duplikacji! Uzyj wzorca Template Method.

Kazdy przepis ma te same kroki:
1. Wyswietl naglowek
2. Zbierz skladniki
3. Przygotuj
4. Gotuj
5. Podaj
6. Wyswietl stopke

Ale szczegoly sa rozne dla kazdego przepisu!
"""
from typing import List, Dict


class PastaRecipe:
    """Przepis na makaron - pelno powielonego kodu!"""
    
    def __init__(self):
        self.name = "Spaghetti Bolognese"
        self.prep_time = 10
        self.cook_time = 20
    
    def prepare(self) -> Dict:
        """Przygotuj danie wedlug przepisu"""
        steps = []
        
        # Naglowek
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)
        
        # Krok 1: Skladniki
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Makaron spaghetti 250g")
        steps.append("  - Mielone mieso 300g")
        steps.append("  - Sos pomidorowy 400ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Czosnek 2 zabki")
        
        # Krok 2: Przygotowanie
        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Pokroj cebule w kostke")
        steps.append("  - Posiekaj czosnek")
        steps.append("  - Odmierz makaron")
        
        # Krok 3: Gotowanie
        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Zagotuj wode z sola")
        steps.append("  - Wrzuc makaron, gotuj 10 min")
        steps.append("  - Podsmaż cebule i czosnek")
        steps.append("  - Dodaj mieso, smaż 5 min")
        steps.append("  - Dodaj sos, gotuj 10 min")
        
        # Krok 4: Podawanie
        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Odcedz makaron")
        steps.append("  - Polej sosem")
        steps.append("  - Posyp parmezanem")
        
        # Stopka
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)
        
        result = "\n".join(steps)
        print(result)
        
        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }


class PizzaRecipe:
    """Przepis na pizze - ZNOWU to samo! Copy-paste!"""
    
    def __init__(self):
        self.name = "Pizza Margherita"
        self.prep_time = 15
        self.cook_time = 25
    
    def prepare(self) -> Dict:
        """Przygotuj danie wedlug przepisu"""
        steps = []
        
        # Naglowek - identyczny jak w PastaRecipe!
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)
        
        # Krok 1: Skladniki
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Maka 300g")
        steps.append("  - Drozdze 7g")
        steps.append("  - Sos pomidorowy 200ml")
        steps.append("  - Mozzarella 200g")
        steps.append("  - Bazylia swieża")
        
        # Krok 2: Przygotowanie
        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Zrob ciasto z maki, drozdzy i wody")
        steps.append("  - Zostaw do wyrośniecia 1h")
        steps.append("  - Pokroj mozzarelle")
        
        # Krok 3: Gotowanie
        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Nagrzej piekarnik do 220°C")
        steps.append("  - Rozwałkuj ciasto")
        steps.append("  - Posmaruj sosem")
        steps.append("  - Poloz ser")
        steps.append("  - Piecz 15 min")
        
        # Krok 4: Podawanie
        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Wyjmij z piekarnika")
        steps.append("  - Dodaj swieża bazylie")
        steps.append("  - Pokroj na kawalki")
        
        # Stopka - znowu to samo!
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)
        
        result = "\n".join(steps)
        print(result)
        
        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }


class SaladRecipe:
    """Przepis na salatke - JESZCZE WIECEJ kopii tego samego!"""
    
    def __init__(self):
        self.name = "Salatka Grecka"
        self.prep_time = 15
        self.cook_time = 0  # Salatka nie wymaga gotowania!
    
    def prepare(self) -> Dict:
        """Przygotuj danie wedlug przepisu"""
        steps = []
        
        # Naglowek - TEN SAM co wyzej!
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)
        
        # Krok 1: Skladniki
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Pomidor 3 szt")
        steps.append("  - Ogorek 1 szt")
        steps.append("  - Feta 150g")
        steps.append("  - Oliwki 100g")
        steps.append("  - Oliwa z oliwek")
        
        # Krok 2: Przygotowanie
        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Pokroj pomidory w osemki")
        steps.append("  - Pokroj ogorka w plastry")
        steps.append("  - Pokrusz fete")
        
        # Krok 3: Gotowanie - dla salatki to mieszanie!
        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Wymieszaj warzywa w misce")
        steps.append("  - Dodaj oliwki")
        steps.append("  - Polej oliwa")
        steps.append("  - Posyp feta")
        
        # Krok 4: Podawanie
        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Przeloz na talerz")
        steps.append("  - Posyp oregano")
        
        # Stopka - i znowu to samo!
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)
        
        result = "\n".join(steps)
        print(result)
        
        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }


class SoupRecipe:
    """Przepis na zupe - i tu tez kopiujemy jak szaleni!"""
    
    def __init__(self):
        self.name = "Zupa Pomidorowa"
        self.prep_time = 10
        self.cook_time = 30
    
    def prepare(self) -> Dict:
        """Przygotuj danie wedlug przepisu"""
        steps = []
        
        # Naglowek - copy paste z 3 innych klas!
        steps.append("=" * 50)
        steps.append(f"PRZEPIS: {self.name}")
        steps.append(f"Czas przygotowania: {self.prep_time} min")
        steps.append(f"Czas gotowania: {self.cook_time} min")
        steps.append("=" * 50)
        
        # Krok 1: Skladniki
        steps.append("\n[KROK 1] Zbierz skladniki:")
        steps.append("  - Pomidory 1kg")
        steps.append("  - Bulion 1l")
        steps.append("  - Smietanka 200ml")
        steps.append("  - Cebula 1 szt")
        steps.append("  - Makaron drobny 100g")
        
        # Krok 2: Przygotowanie
        steps.append("\n[KROK 2] Przygotuj skladniki:")
        steps.append("  - Pokroj pomidory")
        steps.append("  - Posiekaj cebule")
        steps.append("  - Odmierz makaron")
        
        # Krok 3: Gotowanie
        steps.append("\n[KROK 3] Gotuj:")
        steps.append("  - Podsmaż cebule")
        steps.append("  - Dodaj pomidory, duś 10 min")
        steps.append("  - Zalej bulionem")
        steps.append("  - Gotuj 15 min")
        steps.append("  - Zmiksuj")
        steps.append("  - Dodaj smietanke i makaron")
        steps.append("  - Gotuj 5 min")
        
        # Krok 4: Podawanie
        steps.append("\n[KROK 4] Podaj danie:")
        steps.append("  - Przelej do misek")
        steps.append("  - Dodaj groszek ptysiowy")
        
        # Stopka - ZNOWU!
        steps.append("\n" + "=" * 50)
        steps.append("SMACZNEGO!")
        steps.append("=" * 50)
        
        result = "\n".join(steps)
        print(result)
        
        return {
            "name": self.name,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.prep_time + self.cook_time,
            "steps": steps
        }


# Przykladowe uzycie
if __name__ == "__main__":
    print("\n>>> TESTOWANIE SYSTEMU PRZEPISOW <<<\n")
    
    recipes = [
        PastaRecipe(),
        PizzaRecipe(),
        SaladRecipe(),
        SoupRecipe()
    ]
    
    for recipe in recipes:
        result = recipe.prepare()
        print(f"\nCzas calkowity: {result['total_time']} min")
        print("\n" + "~" * 70 + "\n")
