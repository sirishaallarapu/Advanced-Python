
def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your answer: ").strip().lower() 
    if user_answer == correct_answer.lower():
        print("Correct!")
        return 1  
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")
        return 0  

def display_score(score, total_questions):
    print(f"\nYou completed the quiz!")
    print(f"Your score: {score} out of {total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Your score percentage: {percentage:.2f}%")

def main():
    questions_and_answers = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "In which year did the Titanic sink?", "answer": "1912"}
    ]

    score = 0 
    total_questions = len(questions_and_answers)
    for qa in questions_and_answers:
        score += ask_question(qa["question"], qa["answer"])
    display_score(score, total_questions)

if __name__ == "__main__":
    main()
