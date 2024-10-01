options: dict[int, str] = {
    1: "Print welcome message",
    2: "Print the name backwards",
    3: "Print the first character",
    4: "Show the amount of characters in the name",
    0: "Exit"
}

print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
nimi = input("Before the menu, please insert your name: ")
print("\nOptions:")
for i in options:
    print(f"{i} - {options[i]}")
try:
    valinta = int(input("Your choice: "))
    if valinta == 1:
        print(f"Welcome {nimi}!")
    elif valinta == 2:
        print(f'Your name backwards is "{nimi[::-1]}"')
    elif valinta == 3:
        print(f'The first character in name "{nimi}" is "{nimi[0]}"')
    elif valinta == 4:
        print(f'There are {len(nimi)} characters in the name "{nimi}"')
    elif valinta == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
except ValueError:
    print("Unknown option.")
print("\nProgram ending.")
