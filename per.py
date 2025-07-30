items = {}
total = 0

while True:
    item = input("Enter an item 'Q' to exit: ")
    if item.lower() == "q":
        break
    quantity = int(input(f"Enter the quantity of {item}: "))
    price = int(input(f"Enter the price of {item}: "))
    price *= quantity
    items.update({item : price})

for i in items.values():
    total += i

total += total*0.2

for x,y in items.items():
    print(f"The total of {x} is ${y:.1f}")

print(f"The total of your items is ${total}")










