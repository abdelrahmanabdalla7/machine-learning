class Quiz:
    def __init__(self):
        self.scores=0
    def ask_answer(self,question,answers):
        answer_number=1
        print(question)
        for i in answers:
            print(f"{answer_number}. {i}")
            answer_number+=1
    def check_answer(self,given_answer,correct_answer):
        if given_answer==correct_answer:
            self.scores+=20
            print("Hooray! That's correct  😊 ...  ")
        else:
            print("No ! That's not Correct  😑 ... ")
    def show_result(self):
        if  self.scores>= 20:
            print(f"\nScore {self.scores} \n Pass")
        else:
            print(f"\nScore {self.scores} \n Faild")