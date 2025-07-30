num = input("Enter a number: ")
total = 0
nums = []

for i in range(1,5):
    x = int(num * i)
    total += x
    nums.append(x)

print("The numbers are : ", end="")

for x in nums :
    print(x, end=";")

print()

print(f"The total is: {total}")