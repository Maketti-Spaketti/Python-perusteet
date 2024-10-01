print("Program starting.")
print("Insert two integers.")
eka = int(input("Insert first integer: "))
toka = int(input("Insert second integer: "))
summa = eka + toka
print("Comparing inserted integers.")
if eka == toka:
    print("Integers are the same")
elif eka > toka:
    print("First integer is greater.")
else:
    print("Second integer is greater.")
print("\nAdding integers together")
print(f"{eka} + {toka} = {summa}\n")
print("Checking the parity of the sum...")
if summa % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")
