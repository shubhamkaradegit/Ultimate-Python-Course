import random

'''
1 for snake 
-1 for water
0 for gun

'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter 's' for snake, 'g' for gun, 'w' for water: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}
you = youDict[youstr]

#By now we have 2 numbers (variable) computer and younum

print(f"You chose : {reverseDict[you]}")
print(f"Computer chose : {reverseDict[computer]}")


if(computer == -1 and you == 1):
    print("You won!")

elif(computer == 1 and you == 0):
    print("You won!")


elif(computer == 0 and you == -1):
    print("You won!")

elif(computer == you):
    print("It's a tie")

else:
    print("You lose!")
