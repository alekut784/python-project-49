#!/usr/bin/env python3

import prompt
import random


from brain_games.scripts.brain_games import greet


def game():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    correct_answers = 0
    while True:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')

        if (is_prime(number) and answer == 'yes') or (not is_prime(number) and answer == 'no'):
            print('correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Congratulations, {username}!')
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
