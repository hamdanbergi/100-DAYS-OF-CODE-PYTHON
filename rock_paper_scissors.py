import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
user_input = int(input("choose 0 for rock, 1 for paper, 2 for scissors: "))
computer_input = random.randint(0,2)
if 0 <= user_input <= 2:
    print (f"you chose {images[user_input]}")
    print (f"computer chose {images[computer_input]}")
    if user_input == computer_input:
        print(" its a draw")
    elif user_input == 0 and computer_input == 1:
        print("you lose")
    elif user_input == 0  and computer_input == 2:
        print("you win")
    elif user_input == 1 and computer_input == 0:
        print("you win")
    elif user_input == 1 and computer_input == 2:
        print("you lose")
    elif user_input == 2 and computer_input == 0:
        print("you lose")
    elif user_input == 2 and computer_input == 1:
        print("you win")
else :
    print("invalid choice\n Try again")
