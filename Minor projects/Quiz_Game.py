questions = [
    {
        "question": "What is the capital of India?", 
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },


{
    "question": "Which language is used for AI and ML?", 
    "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
    "answer": "A"
},

{
    "question": "What is 5 + 5?", 
    "options": ["A. 8", "B. 9", "C. 10", "D. 11"], 
    "answer": "C"
},

{
    "question": "Which data structure stores key-value pairs?",
    "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
    "answer": "D"
}

]

def start_quiz():
    score = 0
    
    print("\n ***** Quize Game *****")
    
    for number, question in enumerate(questions, start = 1):
        print(f"\nQuestion {number}: {question['question']}")
        
        
        for option in question["options"]:
            print(option)
            

            
        user_answer = input("Enter your answer (A/B/C/D):").upper()
        
        if user_answer == question["answer"]:
            print("Correct Answer!")
            score += 1
            
        else:
            print("Wrong Answer!")
            print("Correct Answer!", question["answer"])
            
    print("\n ===== Quiz Finished =====")
    print("Your Score:", score , "/", len(questions))
    
    percentage = (score/len(questions))*100
    print("percentage:", percentage, "%")
    
while True:
            
    print("\n ***** Quiz Menu *****")
    print("1. start Quiz")
    print("2. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        start_quiz()
        
    elif choice == "2":
        print("Thank you for playing!")
        break 
    
    else:
        print("Invalid choice! please try again.")
    