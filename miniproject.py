menu = {
     'Pizza': 40,
     'Burger': 60,
     'Salad': 50,
     'Pasta':70,
     'Mancuriyan': 100
}

print("Welcome to PYTHON Resturant")
print("Pizza : 40\nBurger : 60\nSalad : 50\nPasta : 70\nMancuriyan : 100")

Order_Total = 0

item_1 = input("Enter the name of item if you want to order =")
if item_1 in menu:
    Order_Total += menu[item_1]
    print(f"Your item {item_1} has been add your order = ")
else:
    print(f"This item {item_1} is not available yet")


another_item = input("Do you want another item ? Yes/No")
if another_item == "Yes":
 item_2 = input("Enter the name of item")
if item_2 in menu:
    Order_Total += menu[item_2]
    print(f"Your item {item_2} has been add your order")
else:
    print(f"This item {item_2} is not available yet")


print(f"The total number of amount your item {Order_Total}")