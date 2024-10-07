print("Program starting.\n")

sanat = []
while sana := input("Insert word (empty stops): "):
    sanat.append(sana)

print("\nYou inserted:")
print(f"- {len(sanat)} words")
print(f"- {sum(len(x) for x in sanat)} characters")

print("\nProgram ending.")
