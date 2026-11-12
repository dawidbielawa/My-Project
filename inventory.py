import random

def show_inv(ekwipunek, waga, max_waga, waga_przedmiotow):
    for i in ekwipunek.keys():
        print(i, "-", ekwipunek[i], "; waga(x1):", waga_przedmiotow.get(i, 0))
    print("waga:", waga, "/", max_waga)
        
def add_item(ekwipunek, waga_przedmiotow, max_waga):
    while True:
        item = input("Jaki przedmiot chcesz dodać? ").lower().strip()
        if item not in waga_przedmiotow:
            waga_przedmiotow[item] = random.randint(1,10)
        if item == "quit":
            break
        elif item in ekwipunek:
            amount = pobierz_liczbe()
            ekwipunek[item] += amount
            waga = waga_oblicz(ekwipunek, waga_przedmiotow)
            if waga > max_waga:
                ekwipunek[item] -= amount
                print("Nie możesz unieść więcej przedmiotów.")
        else:
            amount = pobierz_liczbe()
            if amount == 0:
                print("Nie dodano żadnych przedmiotów.")
            else:
                ekwipunek[item] = amount
                waga = waga_oblicz(ekwipunek, waga_przedmiotow)
                if waga > max_waga:
                    ekwipunek.pop(item)
                    print("Nie możesz unieść więcej przedmiotów.")

def use_item(ekwipunek):
    while True:
        item = input("Jaki przedmiot chcesz użyć? ").lower().strip()
        if item == "quit":
            break
        elif item in ekwipunek and item != "zloto":
            amount = pobierz_liczbe()
            if amount <= ekwipunek[item]:
                ekwipunek[item] -= amount
                if ekwipunek[item] == 0:
                    ekwipunek.pop(item)
            else:
                print("Nie masz wystarczająco tego przedmiotu.")
        else:
            if item == "zloto":
                print("To nie jest przedmiot.")
            else:
                print("Nie masz takiego przedmiotu.")

def check(ekwipunek):
    while True:
        item = input("Jaki przedmiot chcesz sprawdzić? ").lower().strip()
        if item == "quit":
            break
        elif item in ekwipunek:
            print("Ten przedmiot jest w ekwipunku. Ilosc: ", ekwipunek[item])

def shop(ekwipunek, waga_przedmiotow, max_waga):
    while True:
        print("Sklep: miecz - 10, mikstura - 2")
        item = input("Co chcesz kupic? ").lower().strip()  
        if item == "miecz":
            amount = pobierz_liczbe()
            cena = 10 * amount
            if ekwipunek["zloto"] >= cena:
                ekwipunek["zloto"] -= cena
                ekwipunek[item] = ekwipunek.get(item, 0) + amount
                waga = waga_oblicz(ekwipunek, waga_przedmiotow)
                if waga > max_waga:
                    ekwipunek["zloto"] += cena
                    ekwipunek[item] = ekwipunek.get(item, 0) - amount
                    print("Nie możesz unieść więcej przedmiotów.")
            else:
                print("Nie masz wystarczająco zlota.")
        elif item == "mikstura":
            amount = pobierz_liczbe()
            cena = 2 * amount
            if ekwipunek["zloto"] >= cena:
                ekwipunek["zloto"] -= cena
                ekwipunek[item] = ekwipunek.get(item, 0) + amount
                waga = waga_oblicz(ekwipunek, waga_przedmiotow)
                if waga > max_waga:
                    ekwipunek["zloto"] += cena
                    ekwipunek[item] = ekwipunek.get(item, 0) - amount
                    print("Nie możesz unieść więcej przedmiotów.")
            else:
                print("Nie masz wystarczająco zlota.")
        elif item == "quit":
            break
        else:
            print("Nie ma takiego przedmiotu na sprzedaz.")

def waga_oblicz(ekwipunek, waga_przedmiotow):
    waga = 0
    for i in ekwipunek:
        waga += ekwipunek[i] * waga_przedmiotow.get(i, 0)
    return waga

def pobierz_liczbe(pytanie = "Ile? "):
    while True:
        try:
            liczba = int(input(pytanie).strip())
        except ValueError:
            print("Podaj liczbę całkowitą.")
            continue
        if liczba < 0:
            print("Liczba nie może być ujemna.")
            continue
        return liczba

def menu():
    waga_przedmiotow = {"miecz": 5, "mikstura": 1, "zloto": 0} 
    ekwipunek = {"miecz": 1, "mikstura": 3, "zloto": 50}
    max_waga = 50
    while True:
        waga = waga_oblicz(ekwipunek, waga_przedmiotow)
        print("1. show ", "2. add", "3. use", "4. check", "5. shop", "6. quit")
        option = input("Wybierz: ").strip()
        if option == "1":
            show_inv(ekwipunek, waga, max_waga, waga_przedmiotow)
        elif option == "2":
            add_item(ekwipunek, waga_przedmiotow, max_waga)
        elif option == "3":
            use_item(ekwipunek)
        elif option == "4":
            check(ekwipunek)
        elif option == "5":
            shop(ekwipunek, waga_przedmiotow, max_waga)
        elif option == "6":
            break
        else:
            print("Nie jest to jedna z opcji.")

menu()
