print("Calculate fuel consumption.")
distance = float(input("Enter travel distance(kilometers): "))
fuel = float(input("Enter fuel usage(liters): "))
print(f"Fuel consumption is {fuel/(distance/100):.0f} l per 100 km")
