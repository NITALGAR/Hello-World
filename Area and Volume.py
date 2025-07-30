import math


shapes =['triangle', 'square', 'rectangle','circle']
shapess = ['cube','prism']
cal = ['volume','area','Pythagore']

def volume():
    if ask2 in shapess:
        if ask2 == 'prism':
            h = float(input('Enter height : '))
            b = float(input('Enter base length : '))
            w = float(input('Enter weight : '))
            result = h * b * w
        else :
            s = float(input('Enter length : '))
            result = float(pow(s, 3,))
    print(f'The {ask} of {ask2} is {result}cm³')


#########################################
def area():
    if ask2 in shapes:
        if ask2 == 'triangle':
            h = float(input('Enter height : '))
            b = float(input('Enter base length : '))
            result = h * b * 0.5
        elif ask2 == 'rectangle' :
            l = float(input('Enter length : '))
            w = float(input('Enter weight : '))
            result = l * w
        elif ask2 == 'circle':
            r = float(input('Enter radius : '))
            are = r**2 * math.pi
            result = round(are,2)

        else :
            s = float(input('Enter length : '))
            result = pow(s,2)
    print(f'The {ask} of {ask2} is {result}cm²')
#########################################################
def pythagorean():
    g = input("do you want to calculate The hypotenuse or any side? (h or s) :")
    if g == 'h':
        a = float(input('Enter the 1ˢᵗ side : '))
        b = float(input('Enter the 2ⁿᵈ side : '))
        c = round(math.sqrt(pow(a,2)+pow(b,2)),2)
        print(f'The third side is {c}cm')
    elif g == 's':
        a = float(input('Enter the 1ˢᵗ side : '))
        b = float(input('Enter the hypotenuse length : '))
        c = round(math.sqrt(pow(b,2)-pow(a,2)),2)
        print(f'The third side is {c}cm')
    else :
        print('You didnt choose a valid option')



########################################################
##########################################################
while True :
    ask = input('What do you want to calculate? (area , volume , pythagore)(To quit type q) : ')

    if ask == 'pythagore':
        pythagorean()
    elif ask == 'area':
        ask2 = input(f'{ask} of what? (square , triangle , rectangle , circle) : ')
        if ask2 in shapes :
            area()
    elif ask == 'volume':
        ask2 = input(f'{ask} of what? (cube , prism) : ')
        if ask2 in shapess:
            volume()
        else :
            print(f'sorry i cant calculate {ask2} {ask}')
    elif ask.lower() == 'q':
        break

    else :
        print('You didnt choose a valid option')
































