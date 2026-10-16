menu = {
    "Burger": 12,
    "Pizza": 15,
    "Salad": 8
}

for item in menu:
    print(item, "$", menu[item])

food = input("Enter a food name: ")

if food in menu:
    print("Price: $", menu[food])
else:
    print("Item not on the menu.")