
def Oblicz_pole_figur(nazwa): \

    nazwa = nazwa.lower()


    if nazwa == "prostokat":
        a = int(input("Podaj dlugosc prostokata: "))
        b = int(input("Podaj szerokosc prostokata: "))

        pole_prostokata = a * b
        print(f"Pole prostokata wynosi {pole_prostokata}.")


    else:
        print("NIE MA TAKIEGO KSZTALTU!")


if __name__ == "__main__":
    nazwa_ksztaltu = input("Podaj nazwe figury gemetrycznej dla ktorej chcezs obliczyc pole: ")


    Oblicz_pole_figur(nazwa_ksztaltu)