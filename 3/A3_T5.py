options: dict[int, str] = {
    1: "Celcius to Fahrenheit",
    2: "Fahrenheit to Celcius",
    0: "Exit"
}

print("Program starting.")
print("\nOptions:")
for i in options:
    print(f"{i} - {options[i]}")
try:
    valinta = int(input("Your choice: "))
    if valinta == 1:
        lukema = int(input("Insert the amount of Celcius: "))
        vastaus = lukema * 1.8 + 32
        print(f"{lukema:.1f} °C equals to {vastaus:.1f} °F")
    elif valinta == 2:
        lukema = int(input("Insert the amount of Fahrenheit: "))
        vastaus = (lukema - 32) / 1.8
        print(f"{lukema:.1f} °F equals to {vastaus:.1f} °C")
    elif valinta == 0:
        print('Exiting...')
    else:
        print("Unknown option.")
except ValueError:
    print("Unknown option.")
print("\nProgram ending.")
