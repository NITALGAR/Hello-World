menu = {
    "Coffee": 9.0,
    "Milk": 5.50,
    "Espresso": 7.75,
    "Tea": 4.25,
    "Latte": 6.75,
    "Cappuccino": 8.50,
    "Hot Chocolate": 5.00,
    "Mocha": 7.25,
    "Americano": 6.00,
    "Macchiato": 7.00,
    "Flat White": 6.50,
    "Iced Coffee": 5.75,
    "Iced Latte": 7.00,
    "Frappuccino": 8.25,
    "Green Tea": 4.50,
    "Chai Latte": 5.75,
    "Herbal Tea": 4.75,
    "Caramel Latte": 7.50,
    "Pumpkin Spice Latte": 8.00,
    "Smoothie": 6.25,
    "Milkshake": 5.75,
    "Lemonade": 4.25,
    "Iced Tea": 4.75
}



order = []
total = 0

print("-------MENU-------")
for Key, value in menu.items():
        print(f"{Key:10} : ${value:.2f}")
print("------------------")

while True:
        s = input("Please take an order(Q to quit) : ")
        if s.capitalize() == "Q":
                break
        elif menu.get(s.capitalize()) is not None:
                order.append(s)
                total += menu.get(s.capitalize())
print(f"your order is {order} "
      f"and your total is : ${total:.2f}")














