print("Program starting.")

number = int(input("Insert a positive integer: "))
output = [str(number)]
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    output.append(str(number))

print(" -> ".join(output))
print(f"Sequence had {len(output)-1} total steps.")

print("\nProgram ending.")
