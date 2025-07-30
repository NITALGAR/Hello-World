import random as rd

d = int(input("Please enter a difficulty: "))

number = rd.randint(1,d)
guesses = 1
guess = 0
print(f"I'm thinking in a number between 1 and {d} can you guess it?  ")
while not guess ==  number:
    guess = int(input("Take a guess : "))
    if guess < number :
        print("----HIGHER----")
        guesses += 1
    elif guess > number:
        print("----LOWER----")
        guesses += 1
    
if guesses == 1 :
    print(f"OMG!! you're a genius it's {number}")
    print(f"You took {guesses} guesses")
else:

    print(f"Congratulation it's {number}")
    print(f"You took {guesses} guesses")























