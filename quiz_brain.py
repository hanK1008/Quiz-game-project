
# Creating class

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.final_score = ''

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        number = self.question_number
        user_answer = input(f"Q.{number + 1}: {self.question_list[number].qsn} (True/False)?: ")
        correct_answer = self.question_list[number].ans
        self.check_answer(user_answer, correct_answer)
        self.question_number += 1
        self.final_score = f"{self.score}/{self.question_number}"

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it wright")
        else:
            print("That's wrong.")

        print(f"Your current score: {self.score}/{self.question_number +1 }\n")



