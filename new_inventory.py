import random

def show_inv(ekwipunek, waga, max_waga):
    for i in ekwipunek.keys():
        print(i, "-", ekwipunek[i]["ilosc"], "; waga(x1):", ekwipunek[i]["waga"], "; wartosc(x1):", ekwipunek[i]["wartosc"])
    print("waga:", waga, "/", max_waga)
        
def add_item(ekwipunek, max_waga, lista_przedmiotow):
    while True:
        item = input("Jaki przedmiot chcesz dodać? ").lower().strip()
        if item == "quit":
            break
        if item in ekwipunek:
            amount = pobierz_liczbe()
            ekwipunek[item]["ilosc"] += amount
            waga = waga_oblicz(ekwipunek)
            if waga > max_waga:
                ekwipunek[item]["ilosc"] -= amount
                print("Nie możesz unieść więcej przedmiotów.")
        else:
            amount = pobierz_liczbe()
            if amount == 0:
                print("Nie dodano żadnych przedmiotów.")
            else:
                ekwipunek[item] = {}
                ekwipunek[item]["ilosc"] = amount
                if item in lista_przedmiotow:
                    ekwipunek[item]["waga"] = lista_przedmiotow[item]["waga"]
                    ekwipunek[item]["wartosc"] = lista_przedmiotow[item]["wartosc"]
                else:
                    ekwipunek[item]["waga"] = random.randint(1,10)
                    ekwipunek[item]["wartosc"] = random.randint(1,10)
                    lista_przedmiotow[item] = {"waga": ekwipunek[item]["waga"], "wartosc": ekwipunek[item]["wartosc"]}
                waga = waga_oblicz(ekwipunek)
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
            if amount <= ekwipunek[item]["ilosc"]:
                ekwipunek[item]["ilosc"] -= amount
                if ekwipunek[item]["ilosc"] == 0:
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
            print("Ten przedmiot jest w ekwipunku. Ilosc: ", ekwipunek[item]["ilosc"])
        else:
            print("Nie ma takiego przedmiotu w ekwipunku.")

def shop(ekwipunek, max_waga):
    while True:
        print("1. kup", "2. sprzedaj")
        wybor = input("Wybór: ").lower().strip()
        if wybor == "quit":
            break
        elif wybor == "1":
            while True:
                print("Sklep: miecz - 10, mikstura - 2")
                item = input("Co chcesz kupic? ").lower().strip()  
                ceny = {"miecz": {"cena" : 10, "waga": 5, "wartosc": 10}, 
                        "mikstura": {"cena" : 2, "waga": 1, "wartosc": 2} 
                        }  
                if item in ceny:
                    amount = pobierz_liczbe()
                    cena = ceny[item]["cena"] * amount
                    if item not in ekwipunek:
                        ekwipunek[item] = {"ilosc": 0, "waga": ceny[item]["waga"], "wartosc": ceny[item]["wartosc"]}
                    if ekwipunek["zloto"]["ilosc"] >= cena:
                        ekwipunek["zloto"]["ilosc"] -= cena
                        ekwipunek[item]["ilosc"] += amount
                        waga = waga_oblicz(ekwipunek)
                        if waga > max_waga:
                            ekwipunek["zloto"]["ilosc"] += cena
                            ekwipunek[item]["ilosc"] -= amount
                            print("Nie możesz unieść więcej przedmiotów.")
                    else:
                        print("Nie masz wystarczająco zlota.")
                elif item == "quit":
                    break
                else:
                    print("Nie ma takiego przedmiotu na sprzedaz.")
        elif wybor == "2":
                while True:
                    item = input("Jaki przedmiot chcesz sprzedac? ").lower().strip()
                    if item == "quit":
                        break
                    elif item in ekwipunek and item != "zloto":
                        amount = pobierz_liczbe()
                        if amount <= ekwipunek[item]["ilosc"]:
                            ekwipunek[item]["ilosc"] -= amount
                            ekwipunek["zloto"]["ilosc"] += ekwipunek[item]["wartosc"] * amount
                            if ekwipunek[item]["ilosc"] == 0:
                                ekwipunek.pop(item)
                        else:
                            print("Nie masz wystarczająco tego przedmiotu.")
                    else:
                        if item == "zloto":
                            print("To nie jest przedmiot.")
                        else:
                            print("Nie masz takiego przedmiotu.")


def waga_oblicz(ekwipunek):
    waga = 0
    for i in ekwipunek:
        waga += ekwipunek[i]["ilosc"] * ekwipunek[i]["waga"]
    return waga

def pobierz_liczbe():
    while True:
        try:
            liczba = int(input("Ile? ").strip())
        except ValueError:
            print("Podaj liczbę całkowitą.")
            continue
        if liczba < 0:
            print("Liczba nie może być ujemna.")
            continue
        return liczba

def menu():
    lista_przedmiotow = {"miecz": {"waga": 5, "wartosc": 10}, 
                 "mikstura": {"waga": 1, "wartosc": 2}, 
                 "zloto": {"waga": 0, "wartosc": 1}
                 }
    ekwipunek = {"miecz": {"ilosc" : 1, "waga": 5, "wartosc": 10}, 
                 "mikstura": {"ilosc" : 3, "waga": 1, "wartosc": 2}, 
                 "zloto": {"ilosc" : 50, "waga": 0, "wartosc": 1}
                 }
    max_waga = 50
    while True:
        waga = waga_oblicz(ekwipunek)
        print("1. show ", "2. add", "3. use", "4. check", "5. shop", "6. quit")
        option = input("Wybierz: ").strip()
        if option == "1":
            show_inv(ekwipunek, waga, max_waga)
        elif option == "2":
            add_item(ekwipunek , max_waga, lista_przedmiotow)
        elif option == "3":
            use_item(ekwipunek)
        elif option == "4":
            check(ekwipunek)
        elif option == "5":
            shop(ekwipunek, max_waga)
        elif option == "6":
            potwierdzenie = input("Napewno? (Y/N) \n").lower().strip()
            if potwierdzenie == "y":
                break
            elif potwierdzenie == "n":
                continue
        else:
            print("Nie jest to jedna z opcji.")

menu()