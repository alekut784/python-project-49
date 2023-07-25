#!/usr/bin/env python3

import prompt
import random

from brain_games.scripts.brain_games import greet


def game():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print('What is the result of the expression?')

    correct_answers = 0

    while True:

        operation = random.choice(['+', '-', '*'])
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 5)
        expression = f'{number1}{operation}{number2}'

        if operation == '+':
            result = number1 + number2
        if operation == '-':
            result = number1 - number2
        if operation == '*':
            result = number1 * number2

        print(f'Question: {expression}')
        user_answer = int(input('Your answer: '))
        if user_answer == result:
            print('Correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Congratulations, {username}!')
                break

        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'")
            print(f"Let's try again, {username}! ")
            break


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
