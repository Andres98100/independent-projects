#!/usr/bin/python3
class Rules:
    def repeat(self):
        print("Good luck...")
    def rules_play(self):
        print("1. To start you have to type difficulty from 1-3")
        print("2. For the first level, you will type"
                " numbers in order from 1-100 with certain parameters")
        print("3. For the second level, you will"
                " get a random number from 1 to 100 and type the correct answer")
        print("4. And for the third level, we will maintain the"
                " rules of the second level, but you only have 5 seconds to answer")
    def rules_lvl1(self):
        print("Rules of the first level: ")
        print("1. Player must type numbers from 1 to 100")
        print("2. If a number is divisible by 3, you must type 'Fizz'")
        print("3. If a number is divisible by 5, you must type 'Buzz'")
        print("4. If a number is divisible by 3 and 5, you must type 'FizzBuzz'")
        print("5. You only have 3 lifes")
        print("6. You get 10 points for each right answer")
        print("7. If you type the wrong answer, you loose 1 life and 5 points")
        self.repeat()
        
    def rules_lvl2(self):
        print("Rules of the second level: ")
        print("1. If the number is divisible by 3, you must type 'Fizz'")
        print("2. If the number is divisible by 5, you must type 'Buzz'")
        print("3. If the number is divisible by 3 and 5, you must type 'FizzBuzz'")
        print("4. Else, you must type the same number that pops")
        self.repeat()
    
    def rules_lvl3(self):
        print("0. you will have 5 seconds to answer each question or you will lose a life.")
        self.rules_lvl2()