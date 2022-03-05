from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    new_question = Question(questions["question"], questions["correct_answer"])
    question_bank.append(new_question)

# print(question_bank[5].qsn)  #testing code

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You completed the quiz.\nYour final score is: {quiz.final_score}")
