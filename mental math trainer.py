import random
import time

score = 0
total_questions = 5  # Number of questions per round

print("Mental Math Trainer")
print("Answer the questions as fast as you can!")
input("Press Enter to start...\n")

for i in range(total_questions):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    # Prepare question
    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)

    print(f"Q{i+1}: {question} = ?")
    start_time = time.time()
    try:
        user_answer = int(input("Your answer: "))
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)

        if user_answer == correct_answer:
            print(f"Correct! Time taken: {time_taken} sec\n")
            score += 1
        else:
            print(f"Wrong. Correct answer was {correct_answer}. Time taken: {time_taken} sec\n")
    except ValueError:
        print("Invalid input. Skipping question.\n")

print(f"Quiz finished! You scored {score}/{total_questions}")
