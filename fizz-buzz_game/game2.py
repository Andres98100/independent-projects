#!/usr/bin/python3
import time
import random
class fizzBuzz_game:
    def __init__(self):
        self.score = 0
        self.lifes = 3

    def play(self):
        print("1. To start you have to type difficulty from 1-3")
        print("2. For the first level, you will type"
                " numbers in order from 1-100 with certain parameters")
        print("3. For the second level, you will"
                " get a random number from 1 to 100 and type the correct answer")
        print("4. And for the third level, we will maintain the"
                " rules of the second level, but you only have 5 seconds to answer")
        level = int(input("What difficulty do you want to choose?: \n"))
        print("Not a valid difficulty")

        if level == 1:
            print("Rules of the game: ")
            print("1. Player must type numbers from 1 to 100")
            print("2. If a number is divisible by 3, you must type 'Fizz'")
            print("3. If a number is divisible by 5, you must type 'Buzz'")
            print("4. If a number is divisible by 3 and 5, you must type 'FizzBuzz'")
            print("5. You only have 3 lifes")
            print("6. You get 10 points for each right answer")
            print("7. If you type the wrong answer, you loose 1 life and 5 points")
            print("Good luck...")
            for n in range(1, 101):
                print(n)
                if self.lifes > 0:
                    r = str(input("Type your answer: "))
                    if (n % 3 == 0) and (n % 5 == 0):
                        i = 'FizzBuzz'
                    elif n % 3 == 0:
                        i = 'Fizz'
                    elif n % 5 == 0:
                        i = 'Buzz'
                    else:
                        i = n
                    if r == str(i):
                        print("Correct!")
                        self.score += 10
                    else:
                        print("Incorrect!")
                        self.score -= 5
                        self.lifes -= 1
                    print("Your score is: {}".format(self.score))
                    print("You have {} lifes".format(self.lifes))
                else:
                    print("Game over")
                    return

        elif level == 2:
            print("1. If the number is divisible by 3, you must type 'Fizz'")
            print("2. If the number is divisible by 5, you must type 'Buzz'")
            print("3. If the number is divisible by 3 and 5, you must type 'FizzBuzz'")
            print("4. Else, you must type the same number that pops")
            for j in range(1, 101):
                n = random.randint(1, 99)
                if self.lifes > 0:
                    print("The number is: {}".format(n))
                    r = str(input("Type your answer: "))
                    if (n % 3 == 0) and (n % 5 == 0):
                        i = 'FizzBuzz'
                    elif n % 3 == 0:
                        i = 'Fizz'
                    elif n % 5 == 0:
                        i = 'Buzz'
                    else:
                        i = n
                    if r == str(i):
                        print("Correct!")
                        self.score += 10
                    else:
                        print("Incorrect!")
                        self.score -= 5
                        self.lifes -= 1
                    if self.score < 0:
                        self.score = 0
                    print("Your score is: {}".format(self.score))
                    print("You have {} lifes".format(self.lifes))
                else:
                    print("Game over")
                    return

game = fizzBuzz_game()
game.play()