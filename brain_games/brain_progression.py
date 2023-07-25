#!/usr/bin/env python3

import prompt
import random


from brain_games.scripts.brain_games import greet


def game():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0

    while True:

        a_begin = random.randint(0, 2)
        a_end = random.randint(25, 30)
        step = random.randint(2, 4)
        progression = list(range(a_begin, a_end, step))
        random_index = random.randint(0, len(progression)-1)
        a_variable = progression[random_index]
        progression[random_index] = '..'

        print(f'Question: {progression}')
        user_answer = int(input('Your answer: '))
        if user_answer == a_variable:
            print('Correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Congratulations, {username}!')
                break

        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{a_variable}'")
            print(f"Let's try again, {username}! ")
            break


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
