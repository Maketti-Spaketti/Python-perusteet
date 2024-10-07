print("Program starting.\n")

luku1 = int(input("Insert starting value: "))
luku2 = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
tuloste = " ".join(str(x) for x in range(luku1, luku2+1))
print(tuloste)

print("\nProgram ending.")
