import random as rd

max = int(input("Please enter max number : "))
min = 1
guesses = 0
number = 0

g = 1
while not number == g:
    g = rd.randint(min , max)
    print(f"Is your number is {g} (y for yes/ l for lower/ h for higher : ) ")
    a = input()
    if a.lower() == "y":
        print(f"yeah i took {guesses}")
        break
    elif a.lower() == "l":
        guesses += 1
        max = g
    elif a.lower() == "h":
        guesses += 1
        min = g
    else :
        pass






















