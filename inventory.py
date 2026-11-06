def show_inv(ekwipunek):
    print(ekwipunek)

def add_item(ekwipunek):
    while True:
        item = input("Jaki przedmiot chcesz dodać? ").lower().strip()
        if item == "quit":
            break
        elif item in ekwipunek:
            amount = int(input("Ile? ").strip())
            ekwipunek[item] += amount
        else:
            ekwipunek[item] = 1

def use_item(ekwipunek):
    while True:
        item = input("Jaki przedmiot chcesz użyć? ").lower().strip()
        if item == "quit":
            break
        elif item in ekwipunek and item != "zloto":
            amount = int(input("Ile? ").strip())
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

def shop(ekwipunek):
    while True:
        print("Sklep: miecz - 10, mikstura - 2")
        item = input("Co chcesz kupic? ").lower().strip()
        if item == "miecz":
            amount = int(input("Ile? ").strip())
            if ekwipunek["zloto"] >= (10 * amount):
                ekwipunek["zloto"] -= (amount * 10)
                ekwipunek[item] += amount
            else:
                print("Nie masz wystarczająco zlota.")
        elif item == "mikstura":
            amount = int(input("Ile? ").strip())
            if ekwipunek["zloto"] >= (10 * amount):
                ekwipunek["zloto"] -= (amount * 10)
                ekwipunek[item] += amount
            else:
                print("Nie masz wystarczająco zlota.")
        elif item == "quit":
            break
        else:
            print("Nie ma takiego przedmiotu na sprzedaz.")

#def waga_oblicz(ekwipunej, waga):
#    for i in range(len(ekwipunek)):
#        print(ekwipunek[i])

def menu():
    ekwipunek = {"miecz": 1, "mikstura": 3, "zloto": 50}
    waga = {"miecz": 5, "mikstura": 1, "zloto": 5}

    while True:
        print("1. show ", "2. add", "3. use", "4. check", "5. shop", "6. quit")
        option = input("Wybierz: ").strip()
        if option == "1":
            show_inv(ekwipunek)
        elif option == "2":
            add_item(ekwipunek)
        elif option == "3":
            use_item(ekwipunek)
        elif option == "4":
            check(ekwipunek)
        elif option == "5":
            shop(ekwipunek)
        elif option == "6":
            break
        else:
            print("Nie jest to jedna z opcji.")

menu()
