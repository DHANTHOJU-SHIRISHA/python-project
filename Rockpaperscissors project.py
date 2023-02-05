#!/usr/bin/env python
# coding: utf-8

# In[13]:


from random import randint
pc=0
cc=0
limit=5
while True:
    choice=['rock','paper','scissor']
    player=input(f"choose from {choice}")
    comp=choice[randint(0,2)]
    print("computer chooses",comp)
    if player==comp:
        print("DRAW MATCH")
    elif player=="paper" and comp=="rock":
        print("Player 1 wins")
        pc=pc+1
    elif player=="rock" and comp=="scissor":
        print("Player 1 wins")
        pc=pc+1
    elif player=="scissor" and comp=="paper":
        print("Player 1 wins")
        pc=pc+1
    else:
        print("Computer won!!")
        cc=cc+1
    if pc==limit or cc==limit:
        break
print("Player score:",pc,"Computer score:",cc)
if pc==limit:
    print("Player wins the game")
elif cc==limit:
    print("Computer wins the game")

