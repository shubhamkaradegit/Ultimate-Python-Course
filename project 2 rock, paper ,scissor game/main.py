#implement rock paper scissor game
import random

computer = random.choice([-1,0,1])
youstr = input("Enter 'r' for rock, 'p' for paper, 's' for scissor: ")

youDict = {"r":1, "p":0, "s":-1}

reverseDict = {1:"rock", 0:"paper", -1:"scissor"}

you = youDict[youstr]

print(f"You chose : {reverseDict[you]}")
print(f"Computer chose : {reverseDict[computer]}")

if(computer == 1 and you == 0):
    print("You won!")
elif(computer == 0 and you == -1):
    print("You won!")
elif(computer == -1 and you == 1):
    print("You won!")
elif(computer == you):
    print("It's a tie")
else:
    print("You lose!")
