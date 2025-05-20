#number_Guessing_game 
import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        
        if  guess < number_to_guess:
            print("too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations, you have guessed the correct number")          
            break
    except:
        print("you have entered a invalid input")    