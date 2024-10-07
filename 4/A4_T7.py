print("Program starting.\n")
print("Check multiplicative persistence.")
luku = input("Insert an integer: ")
askelia = 0
while len(luku) > 1:
    askelia += 1
    prod = 1
    tuloste = []
    # import math
    # prod = math.prod(int(x) for x in luku)
    # print(" * ".join(x for x in luku) + f" = {prod}")
    for i in range(0, len(luku)):
        prod *= int(luku[i])
        tuloste.append(luku[i])
    print(f"{' * '.join(tuloste)} = {prod}")
    luku = str(prod)
print("No more steps.\n")
print(f"This program took {askelia} step(s)")

print("\nProgram ending.")
