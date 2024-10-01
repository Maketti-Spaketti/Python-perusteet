options: dict[int, str] = {
    1: "- In one multi-branched decision",
    2: "- In multiple independent if-statements",
    0: "- Exit"
}

print("Program starting.")
print("Testing decision structures.")
luku = int(input("Insert an integer: "))
print("Options:")
for i in options:
    print(f"{i} {options[i]}")
valinta = int(input("Your choice: "))
if valinta == 1:
    print("Using one multi-branched decision structure.")
    if luku >= 400:
        luku += 44
    elif luku >= 200:
        luku += 22
    elif luku >= 100:
        luku += 11
    print(f"Result is {luku}")
elif valinta == 2:
    print("Using multiple independent if-statements structure.")
    if luku >= 400:
        luku += 44
    if luku >= 200:
        luku += 22
    if luku >= 100:
        luku += 11
    print(f"Result is {luku}")
elif valinta == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("")
print("Program ending.")
