print("Program starting.\n")

luku1 = int(input("Insert starting value: "))
luku2 = int(input("Insert stopping value: "))

luvut = []
print("\nStarting while-loop:")
while luku1 <= luku2:
    luvut.append(str(luku1))
    luku1 += 1
print(" ".join(luvut))

print("\nProgram ending.")
