from questions import Question
from data import question_data
from quizbrain import QuizBrain

question_bank=[]


for q in question_data:

    answer=q["correct_answer"]
    que=q["question"]
    new_question=Question(que,answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():

    quiz.next_question()

print("you have completed the quiz")
print(f"your total score {quiz.score}/{quiz.question_number}")