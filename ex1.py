num = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "10":"ten"}
while True:
    print("Enter a number between 1 and 10 or 'exit' to quit:")
    user_input = input()
    if user_input.lower() == 'exit':
        break
    elif user_input in num:
        print(num[user_input])
    else:
        print("Invalid input. Please enter a number between 1 and 10 or 'exit'.")





















