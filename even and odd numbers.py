n = int(input('Give me a number : '))
prime = True


print(f"{n} is even!" if n % 2 == 0 else f"{n} is odd!")

for x in range(2,n):
    if n % x == 0:
        print (f"{n} isn't a prime number")
        prime = False
        break

if n>1 and prime :
    print(f"{n} is a prime number")
else :
    print(f"{n} isn't a prime number")

print("and it's divisors are : ")



for i in range(1,n+1):
    if n % i ==0 :
        print(i)

