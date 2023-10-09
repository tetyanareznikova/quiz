class QuizQuestion:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_option.lower()

class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start_game(self):
        print("Welcome to the Quiz Game!")

        for question_num, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {question_num}:")
            print(question.question)
            for option_num, option in enumerate(question.options, start=1):
                print(f"{option_num}. {option}")

            user_answer = input("Enter the number of your answer: ")

            if user_answer.isdigit():
                user_answer = int(user_answer) - 1

                if 0 <= user_answer < len(question.options):
                    if question.is_correct(question.options[user_answer]):
                        print("Correct!")
                        self.score += 1
                    else:
                        print(f"Wrong! The correct answer was: {question.correct_option}")
                else:
                    print("Invalid answer number.")
            else:
                print("Invalid input. Please enter the number of your answer.")

        print(f"\nQuiz complete! Your score: {self.score}/{len(self.questions)}")

def main():
    quiz_game = QuizGame()

    # Add quiz questions here
    question1 = QuizQuestion("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris")
    question2 = QuizQuestion("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars")
    question3 = QuizQuestion("What is the largest mammal on Earth?", ["Elephant", "Giraffe", "Blue Whale", "Lion"], "Blue Whale")

    quiz_game.add_question(question1)
    quiz_game.add_question(question2)
    quiz_game.add_question(question3)

    quiz_game.start_game()

if __name__ == "__main__":
    main()
