#!/usr/bin/env python3

import prompt
import random
 
from brain_games.scripts.brain_games import greet

def game():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while True:
        number = random.randint(1, 100)
        answer = input(f'Question: {number} ')

        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Condratulations, {username}!')
                break
        else:
            if (answer == 'yes'):
                answer2 = 'no'
            else:
                answer2 = 'yes'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer2}'. Let's try again, {username}!")
            break


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
