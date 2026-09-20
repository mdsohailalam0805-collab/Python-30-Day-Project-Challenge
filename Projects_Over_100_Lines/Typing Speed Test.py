
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
while True:

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
        exit()
        

    sentence = random.choice(sentences[difficulty])

    print("\n Type the following sentence:")
    print(sentence)   

    print("\n Press Enter when you are ready.")

    start_time = time.time()
    user_text = input(">")
    end_time = time.time()

    time_taken = end_time - start_time  

    print(f" Time Taken : {time_taken:.2f} seconds")

    typed_words = user_text.split()
    words_count = len(typed_words)

    print(f"Words Typed : {words_count}")

    time_in_minutes = time_taken / 60

    wpm = words_count / time_in_minutes

    print(f"WPM : {wpm:.2f}")

    original_words = sentence.split()
    correct_words = 0

    for i in range (min(len(typed_words) , len(original_words))):
        
        if typed_words[i] == original_words[i]:
            correct_words += 1
            
    accuracy = (correct_words / len(original_words)) * 100
    print(f"Accuracy : {accuracy:.2f}")

    incorrect_words = len(original_words) - correct_words
    print(f"Incorrect Words :{incorrect_words}")

    print("\n=====RESULT=====")
    print(f"Time Taken : {time_taken:.2f}seconds")
    print(f"Words Typed : {words_count}")
    print(f"WPM : {wpm}")
    print(f"Correct Words : {correct_words}")
    print(f"Incorrect Words : {incorrect_words}")
    print(f"Accuracy : {accuracy:.2f}%")


    if accuracy >= 90:
        print("Performence : Excellent")
        
    elif accuracy > 70:
        print("Performence : Good")
        
    else:
        print("Performence : keep practicing")
        
    play_again = input("\n Do you want to play again!")

    if play_again.lower() != "yes":
        print("Thanks for playing.")
        break