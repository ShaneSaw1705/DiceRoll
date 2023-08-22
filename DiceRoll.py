import random
#Dictionary declaring each number as a dice

Dice = {1 : "|   |\n| 0 |\n|   |",
        2 : "0   |\n|   |\n|   0",
        3 : "0   |\n| 0 |\n|   0",
        4 : "0   0\n|   |\n0   0",
        5 : "0   0\n| 0 |\n0   0",
        6 : "0   0\n0   0\n0   0"}

run = True
while run:
        Dice1 = random.randint(1,6)
        Dice2 = random.randint(1,6)
        print(Dice[Dice1])
        print("----------------------------")
        print(Dice[Dice2])
        print("You rolled ",(Dice1 + Dice2))
        
        #Breaks the loop to see if the user wants to roll again
        answer = input("Roll again? (y/n) ")
        if answer == "n":
                run = False

print("Thanks for playing")