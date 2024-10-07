print("Program starting.")
print("Welcome to the unit converter program!\n"
      "Follow the menu instructions below.\n\n"
      "Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")
print("")
if choice == "0":
    print("Exiting...")
elif choice == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice = input("Your choice: ")
    if choice == "0":
        print("Exiting...")
    elif choice == "1":
        value = int(input("Insert meters: "))
        print(f"{value:.1f} m is {value/1000:.1f} km")
    elif choice == "2":
        value = int(input("Insert kilometers: "))
        print(f"{value:.1f} km is {value*1000:.1f} m")
    else:
        print("Unknown option.")
elif choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice = input("Your choice: ")
    if choice == "0":
        print("Exiting...")
    elif choice == "1":
        value = int(input("Insert grams: "))
        print(f"{value:.1f} g is {value/453.6:.4f} lb")
    elif choice == "2":
        value = int(input("Insert pounds: "))
        print(f"{value:.1f} lb is {value*453.6:.1f} g")
    else:
        print("Unknown option.")
else:
    print("Unknown option.")
print("\nProgram ending.")
