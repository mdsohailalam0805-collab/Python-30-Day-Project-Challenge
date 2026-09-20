
import random
import time

sentences = {
    "Easy": [
        "Python is easy to learn.",
        "I love coding in Python.",
        "Practice makes programming better."
    ],

    "Medium": [
        "Python is a powerful programming language.",
        "Learning programming requires regular practice.",
        "Small projects help improve coding skills."
    ],

    "Hard": [
        "Consistency and problem solving skills are important for every programmer.",
        "Building real projects helps you understand programming concepts deeply.",
        "A good programmer improves by practicing and learning from mistakes."
    ]
}

print("\n =====TYPING SPEED TEST=====")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice:")

if choice == "1":
    difficulty = "Easy"
    
elif choice == "2":
    difficulty = "Medium"
    
elif choice == "3":
    difficulty = "Hard"
    
else:
    print("Invalid Choice!")
    

sentence = random.choice(sentences[difficulty])

print("\n Type the following sentence:")
print(sentence)   

print("\n Press Enter when you are ready.")

start_time = time.time()
user_text = input(">")
end_time = time.time()