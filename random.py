questions = {
   "What is the capital of France?": "Paris",
   "Which planet is known as the Red Planet?": "Mars",
   "What is 5 + 3?": "8"
}

score = 0

for question, answer in questions.items():
   user_answer = input(question + " ").strip().capitalize()
   if user_answer == answer:
       print("Correct! ✅")
       score += 1
   else:
       print(f"Wrong ❌ The correct answer is {answer}.")

print(f"Final Score: {score}/{len(questions)}")

for question, answer in questions.items():
   user_answer = input(question + " ").strip().capitalize()
   if user_answer == answer:
       print("Correct! ✅")
       score += 1
   else:
       print(f"Wrong ❌ The correct answer is {answer}.")

print(f"Final Score: {score}/{len(questions)}")




