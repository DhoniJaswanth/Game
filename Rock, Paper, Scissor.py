
"""
WORK FLOW OF PROJECT :
1 - Input from user(Rock, paper, Scissor)
2 - Computer choice (Computer will choose randomly not conditionally)
3 - Result print


Cases:
A - Rock 
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Ppaper - Scissor = Scissor win

C - Scissor 
Scissor - Scissor = tie
Scissor - Rock = Rock win 
Scissor - Paper = Scissor win

"""

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same : = match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")

    else:
        print("Rock smashes Scissor= you win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer win")

    else:
        print("Paper covers Rock = You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")

    else:
        print("Rock smashes Scissor, Computer win")
     
     