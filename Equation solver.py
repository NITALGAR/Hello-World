import math
from fractions import Fraction as fra
#########################################################################################################################
def first_degre():
    a = fra(input("Enter the coefficuent a :  "))  
    if a == 0:
        print('The equation has no solution ℝ.')
    else:
        b = fra(input("Enter the coefficuent b :  "))
        print()
        if -b % a == 0:
            print(f"The solution is x =  {-b/a}")
        else:
            if a < 0 and b > 0:
                print(f"The soltion is x = {abs(-b)}/{abs(a)}")
                print()
            else:
                print(f"The soltion is x = {-b}/{a}")
                print()
#######################################################################################################################
#######################################################################################################################
def second_degre():
    a = fra(input("Enter the coefficuent a :  "))
    if a == 0:
        print('The equation has no solution in ℝ.')
    else:
        b = fra(input("Enter the coefficuent b:  "))
        c = fra(input("Enter the coefficuent c:  "))
        d = pow(b, 2) - 4 * a * c
        print()
        print(f"Discriminant of this equation is : Δ = {round(d, 2)}")

        if d < 0:
            print('So,The equation has no solution in ℝ.')

        elif d == 0:
            print('So,The equation has one solution.')
            if -b % 2*a == 0:
                s = -b / (2*a)
            else:
                s = f"{-b}/{2*a}"
            print("x = ", s)
        elif d > 0:
            print('So,The equation has two solutions.')
            s1 = (-b - math.sqrt(d)) /( 2 * a)
            s2 = (-b + math.sqrt(d)) / (2 * a)
            print(" ")
            print(f"x = {round(s1)} , x'= {round(s2)}")
            print(" ")
#######################################################################################################################
#######################################################################################################################
while True:
    ask = input(
        "Do you want to solve a 1st degre or 2nd degre equation (1/2), To quit enter 'Q': ")
    if ask == "1":
        first_degre()
    elif ask == "2":
        second_degre()
    elif ask == "q":
        break
    elif not ask == 1 or 2:
        print("Your option isn't valid!")
        continue
