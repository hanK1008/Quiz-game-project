class Question:

    def __init__(self, text, answer):
        self.question = text
        self.ans = answer


new_qsn = Question("What is your name? ", "False")
print(new_qsn.ans)

