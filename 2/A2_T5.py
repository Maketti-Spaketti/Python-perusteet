print("Program starting.\n")
sana = input("Insert a closed compound word: ")
print(f"The word you inserted is '{sana}' and in reverse it is '{sana[::-1]}'.")
print(f"The inserted word length is {len(sana)}")
print(f"Last character is '{sana[-1]}'\n")

print("Take substring from the inserted word by inserting...")
alku = int(input("1) Starting point: "))
loppu = int(input("2) Ending point: "))
askel = int(input("3) Step size: "))

print(f"\nThe word '{sana}' sliced to the defined substring is '{sana[alku:loppu:askel]}'.")
print("Program ending.")
