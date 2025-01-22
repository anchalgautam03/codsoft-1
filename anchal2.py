""""
Working of project:
1-input from user(Rock ,Paper,Scissor)
2-computer choice(computer will choose randomly not conditionally)
3-Result print

cases:
A-Rock
Rock-Rock=tie
Rock-Paper=Paper win
Rock-Scissor=Rock win

B-Paper
Paper-paper=tie
Paper-Rock=Paper win
Paper-Scissor=Scissor win

C-Scissor
Scissor-Scissor=tie
Scissor-Rock=Rock win
Scissor-Paper=Scissor win


"""

import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter you move=Rock,Paper,Scissor= ")
comp_choice=random.choice(item_list)

print(f"user choice={user_choice},computer choice={comp_choice}")
