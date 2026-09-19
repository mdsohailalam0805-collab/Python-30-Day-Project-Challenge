
import random

choices = ["Rock" , "Paper" , "scissors"]

computer_choice = random.choice(choices)

print(f"Computer Chose : {computer_choice}")

user_choice = int(input("Enter your Choice (1-3):"))

if user_choice == 1:
    user_choice = "Rock"
    
elif user_choice == 2:
    user_choice = "Paper"
    
elif user_choice == 3:
    user_choice = "Scissors"
    
print(f" You Chose : {user_choice}")