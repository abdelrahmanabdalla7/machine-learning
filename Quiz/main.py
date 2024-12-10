from quiz import Quiz

questions = [
    {
        'question': 'How many hours are there in a day?',
        'answers': ['18',   '24', '12', '06'],
        'correct_answer': '24'
    },
    {
        'question': 'How many letters are there in the English alphabet?',
        'answers': ['25', '27', '26', '28'],
        'correct_answer': '26'
    },
    {
        'question': 'Name the house made of ice?',
        'answers': ['Cave', 'Home', 'Igloo', 'Apartment'],
        'correct_answer': 'Igloo'
        },
]
quiz=Quiz()
for problem in questions:
    quiz.ask_answer(problem["question"], problem["answers"])
    given_answer=input("\n Answer:")
    quiz.check_answer(given_answer, problem["correct_answer"])
quiz.show_result()