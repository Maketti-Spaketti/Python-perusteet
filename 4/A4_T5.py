print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
print("")
error = False
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    error = True
if not start <= inspect <= stop:
    print("Inspection value must be within the range of start and stop.")
    error = True
if not error:
    # print("First loop - inspection with break:")
    # print(" ".join(str(x) for x in range(start, stop) if x < inspect))
    # print("Second loop - inspection with continue:")
    # print(" ".join(str(x) for x in range(start, stop) if x != inspect))
    luvut = []
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspect:
            break
        luvut.append(str(i))
    print(" ".join(luvut))

    luvut = []
    print("Second loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspect:
            continue
        luvut.append(str(i))
    print(" ".join(luvut))

print("\nProgram ending.")
