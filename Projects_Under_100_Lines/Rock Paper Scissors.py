
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

# winnig condition
if computer_choice == user_choice:
    print("It's a Draw!")
    
elif(user_choice == "Rock" and computer_choice == "Scissors") or \
    (user_choice == "Scissors" and computer_choice == "Paper") or \
    (user_choice == "Paper" and computer_choice == "Rock"):
    print("You Win!")
    
else:
    print("Computer Win!")