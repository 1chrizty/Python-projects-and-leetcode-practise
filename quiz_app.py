''' Quiz app with timer using function '''

# 5 qust, mark, time > 15 [no need to validate]
import time
quiz_qusts = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "3. What is 5!?",
        "options": ["A. 24", "B. 720", "C. 120", "D. 150"],
        "answer": "C"
    },
    {
        "question": "4. What is the boiling point of water?",
        "options": ["A. 90°C", "B. 50°C", "C. 100°C", "D. 120°C"],
        "answer": "C"
    },
    {
        "question": "5. What is 7 x 8?",
        "options": ["A. 54", "B. 56", "C. 64", "D. 48"],
        "answer": "B"
    }
]

def quiz():
    score = 0
    for q in quiz_qusts:
        time1 = time.time()
        print('\n' + q['question'])
        for option in q['options']:
            print(option)
        
        user_answer = input('Enter your answer (A/B/C/D): ').upper()
        time2 = time.time()

        main_time = time2 - time1
        if user_answer == q['answer']:
            if main_time < 15:
                print('Correct!')
                score += 1
            else:
                print('Time exceeded!!!')
        else:
            print(f'Wrong! Correct answer is {q['answer']}')
    print(f'\nFinal score is {score} out of 5.')
quiz()