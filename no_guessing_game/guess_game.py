from random import randint
from art import logo
easy_turns=10
hard_turns=5
def check(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        print("too low")
        return turns-1
    else:
        print(f"congratulation buddy! you matched the answer which is {answer}.")
       

def setdifficulty_level():
    level=input("choose the level :easy or hard")
    if level=="easy":
        return easy_turns
    else:
        return hard_turns
def game():
    print(logo)
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("think of the number between 1 and 100")
    turns=setdifficulty_level()
   
    answer=randint(1,100)
    print(f"let me remind you that the answer is {answer}")
    guess=0
    while answer!=guess:
        print(f"you have now {turns} turns remaining")

        guess=int(input("input your guess"))
        turns=check(guess,answer,turns)
        if turns==0:
            print("sorry! you lost the game")
            return
game()
   

