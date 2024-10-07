# Tää on aika vitsillä tehty
from typing import Callable


class Yksikkömuunnin():
    paavalikko: dict[int, str] = {
        1: "Length",
        2: "Weight"
        # 3: Volume
    }

    MENU = 0
    LUKU = 1
    MUUUNNETTAVA = 2
    MUUNNETTU = 3
    LASKURI = 4
    DECIMAALIT = 5

    alavalikko: dict[int, dict[int, tuple[str, str, str, str, Callable, int]]] = {
        1: {
            1: ("Meters to kilometers", "meters", "m", "km", lambda x: x/1000, 1),
            2: ("Kilometers to meters", "kilometers", "km", "m", lambda x: x*1000, 1)
            # 3: Miles to kilometers
        },
        2: {
            1: ("Grams to pounds", "grams", "g", "lb", lambda x: x/453.6, 4),
            2: ("Pounds to grams", "pounds", "lb", "g", lambda x: x*453.6, 1)
            # 3: Stones to pounds
        }
    }

    def printtaa_menu(self, menu, alamenu: bool = False):
        for i in menu:
            if not alamenu:
                print(f"{i} - {menu[i]}")
            else:
                print(f"{i} - {menu[i][self.MENU]}")
        print("0 - Exit")

    def aloita(s):
        print("Welcome to the unit converter program!\n"
              "Follow the menu instructions below.\n\n"
              "Options:")
        s.printtaa_menu(s.paavalikko)
        try:
            valinta = int(input("Your choice: "))
            if valinta == 0:
                print("\nExiting...")
                return
            print("\n" + f"{s.paavalikko[valinta]} options:")
            s.printtaa_menu(s.alavalikko[valinta], alamenu=True)
            ala_valinta = int(input("Your choice: "))
            if ala_valinta == 0:
                print("Exiting...")
                return
            muunnin = s.alavalikko[valinta][ala_valinta]
            lukema = float(input(f"Insert {muunnin[s.LUKU]}: "))
            muunnettu = muunnin[s.LASKURI](lukema)
            tarkkuus = f".{muunnin[s.DECIMAALIT]}f"
            print(f"{lukema:.1f} {muunnin[s.MUUUNNETTAVA]} is {muunnettu:{tarkkuus}} {muunnin[s.MUUNNETTU]}")
        except (KeyError, ValueError):
            print("Unknown option.")


if __name__ == "__main__":
    print("Program starting.")
    muunnin = Yksikkömuunnin()
    muunnin.aloita()
    print("\nProgram ending.")
