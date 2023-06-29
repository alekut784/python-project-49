import random

from brain_games.cli import welcome_user 
from brain_games.scripts.brain_games import greet


def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while True:
        number = random.randint(1, 100)
        answer = input(f'Question: {number} ')

        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('correct!')
            correct_answers += 1
            if correct_answers == 3:
                print('Condratulations!')
                break
        else:
            if (answer == 'yes'):
                answer2 = 'no'
            else:
                answer2 = 'yes'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer2}'. Let's try again, Bob!")
            break


def main():
    greet()
    welcome_user()
    game()


if __name__ == '__main__':
    main()
