print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
nimi = input("Before the menu, please insert your name: ")
print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")
try:
    valinta = int(input("Your choice: "))
    if valinta == 1:
        print(f"Welcome {nimi}!")
    elif valinta == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
except ValueError:
    print("Unknown option.")
print("\nProgram ending.")
