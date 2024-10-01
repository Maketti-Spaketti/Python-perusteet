print("Program starting.")

hexi = input("\nInsert a hex color: ")
if hexi.startswith("#"):
    hexi = hexi[1:]
print("\nColors")
print(f"- Red {hexi[0:2]}")
print(f"- Green {hexi[2:4]}")
print(f"- Blue {hexi[4:6]}\n")
print("Program ending.")
