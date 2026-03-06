menu = {"Burtger": 5, "Pizza": 8, "Pasta": 7, "Salad": 4, "Soda": 2}

print("Welcome to the Restraunt!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: ${price}")

most_expensive = max(menu, key=menu.get)
cheapest = min(menu, key=menu.get)
print("The most expensive item is:", most_expensive)
print("The cheapest item is is:", cheapest)
n = int(input("\nHow many items would you like to order?"))

total = 0
for i in range(n):
    order = input(f"Enter item {i + 1}: ")
    if order in menu:
        total += menu[order]
        print(f"Added {order} - ${menu[order]}")
    else:
        print(f"Sorry, {order} is not on the menu.")

print(f"\nYour total bill is: ${total}")

 