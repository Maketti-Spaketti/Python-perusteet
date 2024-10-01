print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")
summa = 0.0
tehtavia = 7
for i in range(0, tehtavia):
    summa += float(input(f"A1_T{i+1}: "))
keskari = summa / tehtavia
print(f"\nIn total you spent {summa:.0f} minutes on programming.")
print(f"Average per task was {round(keskari, 2)} min and same rounded to the nearest integer {keskari:.0f} min.\n")
print("Program ending.")
