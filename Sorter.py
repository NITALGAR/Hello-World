l = []
ask = 0

while True :
    num = input("Please enter a number(q to quit): ")
    if num == "q":
        break
    num = int(num)
    if num not in l:
        l.append(num)

l.sort()
print("The sorted numbers while be :")

for i in l:
    print(i,end=";")
print()

while ask != "q":
    ask = input('Do you want to add(a) or delete(d) an item or quit (q): ')

    if ask.lower() == "a":
        while True :
            num = input("What numbers you want to add (q to quit): ")
            if num == "q" :
                break
            num = int(num)
            if num not in l:
                l.append(num)

    elif ask.lower() == "d":
        while True :
            num = input("What numbers you want to delete (q to quit): ")
            if num == "q" :
                break
            num =int(num)
            l.remove(num)

    l.sort()
    print("The sorted numbers while be :")

    for i in l:
        print(i,end=";")
    print()






