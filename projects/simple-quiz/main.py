def ask_question(question, answer):
    '''Asks a question and returns True if the answer is correct, False otherwise.'''
    user_answer = input(f'{question}: ').strip().lower()
    if user_answer == answer.lower():
        print('Correct!')
        return True
    else:
        print(f'Incorrect. The correct answer is {answer}.')
        return False


def run_quiz(questions):
    '''Runs the quiz with the provided questions and returns the final score.'''
    score = 0
    for question, answer in questions.items():
        if ask_question(question, answer):
            score += 1
    return score


if __name__ == '__main__':
    questions = {
        'What is the capital of France?': 'Paris',
        'What is 2 + 2?': '4',
        'What color is the sky?': 'Blue',
        'What is the name of the earth satellite?': 'Moon'
    }

    print('Welcome to the Simple Quiz!')
    print('Answer the following questions:')

    final_score = run_quiz(questions)

    print('\nQuiz complete!')
    print(f'Your final score is: {final_score}/{len(questions)}')
