import random

def game():
    print("you are playing the game..")
    score = random.randint(1,101)

    # fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if not(hiscore == ""):
            hiscore  = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score : {score}")
    if(score>hiscore or hiscore ==""):
        #write this hiscore to the file
        with open("hiscore.txt" ,"w") as f:
            f.write(str(score))
    return score

game()