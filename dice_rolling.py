#Dice_Rolling_Game
import random 

while True:
    choice = input("Roll the Dice: (y/n)").lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'{die1}, {die2}')
    elif choice == "n":
        print("Thanks for playing")
        break
    else:
        print("you have entered a invalid choice")        
