# quizbrain.py

class QuizBrain:
    def __init__(self,question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"That's the right answer your score: {self.score}/{self.question_no}")
        else:
            print(f"That's Wrong answer!!! your score: {self.score}/{self.question_no}")

        print(f"The correct answer was: {correct_answer}")
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_no < len(self.question_list)
        # above code is same as the below
        # if self.question_no < len(self.question_list):
        #     return True
        # else:
        #     return False
    
