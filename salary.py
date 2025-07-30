salaries = {"A":(200,1000,20),"B":(150,800,20),"C":(120,500,15),"D":(100,350,15),"E":(80,100,10)}
grade = input("Enter the grade of the employee: ").upper()
hour = int(input("Enter the number of hours worked: "))
salary = salaries.get(grade)

total = (salary[0]*hour)+(salary[1]*(hour//salary[2]))
print(f"The salary is: {total}")















