# main.py

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for each_question in question_data:
    text = each_question['text']
    answer = each_question['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

