import random as rd
from random import choice

opion = 0

options =("rock","papier","scissors")
coice = rd.choice(options)

options =("rock","papier","scissors")
while True:
    if opion =="q":
        break
    while not opion in options:
        opion = input(f"Please enter a choice {options} :  ")
        if opion == "q":
            break
    if not opion== "q":


        if coice == opion:
            print("TIE")

        elif coice == "rock" and opion == "papier" or coice=="papier" and opion =="scissors" or coice=="scissors" and opion =="rock":
            print("Congratulation you won!!")

        else:
            print("You lose good luck next time.")
        print(f"I chosed {coice}")
        break
















