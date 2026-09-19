
import random

choices = ["Rock" , "Paper" , "Scissors"]

user_score = 0
computer_score = 0

while True:

    user_choice = int(input("Enter your Choice (1-3) or 4 to Exit:"))

    if user_choice == 4:
        print("Thanks For Playing!")
        break
    
    elif user_choice == 1:
        user_choice = "Rock"
    
    elif user_choice == 2:
        user_choice = "Paper"
    
    elif user_choice == 3:
        user_choice = "Scissors"
        
    else:
        print("Invalid Choice!")
        continue
    
    print(f" You Chose : {user_choice}")

    computer_choice = random.choice(choices)

    print(f"Computer Chose : {computer_choice}")


    # winnig condition

    if computer_choice == user_choice:
        print("It's a Draw!")
    
    elif(user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Scissors" and computer_choice == "Paper") or \
        (user_choice == "Paper" and computer_choice == "Rock"):
        
        print("You Win!")
        user_score += 1
    
    else:
        print("Computer Win!")
        computer_score += 1
    
    print(f"User Score : {user_score}")
    print(f"Computer Score : {computer_score}")
    print("-" * 30)
    
print("\n===== FINAL SCORE =====")
print(f"User Score     : {user_score}")
print(f"Computer Score : {computer_score}")