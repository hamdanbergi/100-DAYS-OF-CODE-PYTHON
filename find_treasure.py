print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

prompt = input("choose 'left' or 'right'")
if prompt == "right" or prompt == "Right":
    print("you fell through a hole and died!")
    print("GAME OVER")
elif prompt == "left" or prompt == "Left":
    print("you arrived at a pier ")
    prompt_2 = input("do you 'Swim' or 'look' for a 'Boat' ")
    if prompt_2 == "swim" or prompt_2 == "Swim":
        print("you reach the island but get sick ")
        print("you succumb to your sickness and you died ")
    elif prompt_2 == "look" or prompt_2 == "look" or prompt_2 == "boat" or prompt_2 == "Boat":
        print("You found a boat and reach the island ")
        prompt_3 = input("do you take a 'left' or 'right' ")
        if prompt_3 == "left" or prompt_3 == "Left":
            print("congratulations you have found the treasure")
        else:
            print("you get devoured by a beast")
    else:
        print("invalid input\n game over\n try again")
else :
    print("invalid input\n game over\n try again")
