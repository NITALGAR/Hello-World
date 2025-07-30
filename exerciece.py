import math as m

def ex_2() :
    age = input("How old are you?: ")
    height = input("Enter you height(m)?: ")
    print(f"You are {age} years old, and {height}m tall")
    pass

def ex_3() :
    distance = float(input("Enter the distance (km): "))
    distance *= 1000
    duration = float(input("Enter the duration (min): "))
    duration *= 60
    speed = round (distance/duration,2)
    print(f"The speed is {speed}m/s")
    pass

def ex_4() :
    sec = int(input("Enter the number of seconds: "))
    hour = m.floor(sec/3600)
    min = m.floor((sec%3600)/60)
    sec =(sec%3600)%60
    print(f"{hour}h:{min}min:{sec}s")
    pass

def ex_5() :
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        if num % 3 == 0:
            print(f"{num} is even, and divided by 3")
        else:
            print(f"{num} is even, but it's not divided by 3")
    elif num % 3 == 0 :
        print(f"{num} isn't even, but it's divided by 3")
    else:
        print(f"{num} isn't even, and it isn't divided by 3")
    pass

def ex_6() :
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    if num1 == 0 or num2 == 0 :
        print("The product will be null")
    elif num1 < 0 or num2 < 0 :
        print("The product will be negative")
    else:
        print("The product will be positive")
    pass

def ex_7() :
    operation = input("Enter an operation: ")
    print(eval(operation))
    pass


def ex_8() :
    num = int (input("How many marks you have: "))
    marks = {}
    total = 0
    coefficients = 0

    for i in range (num):
        mark = int(input("Enter the mark: "))
        coefficient = int(input("Enter its coefficient: "))
        marks[mark] = coefficient

    for i,x in marks.items():
        total += i*x

    for i in marks.values():
        coefficients += i

    print(f"The moyenne is: {round(total/coefficients,2)}")
    
ask = input("Do you want to execute what exercise(2/3/4/5/6/7/8):  ")
if ask == "2" : ex_2()
elif ask == "3" : ex_3()
elif ask == "4" : ex_4()
elif ask == "5" : ex_5()
elif ask == "6" : ex_6()
elif ask == "7" : ex_7()
elif ask == "8" : ex_8()
