user = "admin"
password = "admin"
user_1 = ""
password_1 = ""
tries = 0

while user_1 != user and password_1 != password:
    user_1 = input("Please enter username: ")
    password_1 = input("Please enter password: ")
    tries +=1
    if user_1 == user and password_1 == password:
        continue
    print("Sorry Username or password is incorrect!")
    if tries >= 5 :
        print("you passed the maximum of tries please try again later")
        break
else:
    print("Welcome back Admin")
















