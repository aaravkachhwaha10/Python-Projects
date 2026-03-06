distance  = float(input("Enter the total distance of the trip(in km): "))
efficency = float(input("Enter the car's fuel efficency (km per liter):"))
fuel_price = float(input("Enter the fuel price per liter:"))
fuel_used = distance / efficency
total_cost = fuel_used * fuel_price
print("\n--- Trip Summary ---")
print("Total Distance:" + str(distance) + " km")
print("Fuel Efficincy:" + str(efficency) + " km/1")
print("Fuel used:" + str(round(fuel_used, 2)) + " liters")
print("Fuel Price: $" + str(fuel_price) + " per liter")
print("Total Fuel Cost: $" + str(round(total_cost, 2)))