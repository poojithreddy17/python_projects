#Rock_Paper_scissor
import random 

emojis ={"r":"🪨","p":"📄","s":"✂️"}
choices = ("r","p","s")

while True:
    user_choice = input("Rock,Paper and Scissors?(r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue
    computer_choice = random.choice(choices)   
    print(f"your choise is {emojis[user_choice]} and the computer chose {emojis[computer_choice]}") 
    if user_choice == computer_choice:
        print("Tie")    
    elif ((user_choice == "r" and computer_choice == "s")or
        (user_choice == "s" and computer_choice == "p")or
        (user_choice == "p" and computer_choice == "r")):
        print("you win")
    else:
        print("you lose")  
        
    should_continue = input("continue? (y/n): ").lower()  
    if should_continue == "n":
        break
      
    