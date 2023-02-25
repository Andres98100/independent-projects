#!/usr/bin/python3
import json
import random
import time
import os.path
from rules import Rules

class fizzBuzz_game(Rules):
    def __init__(self):
        "Initialization of constructor"
        self.users = []
        self.name = ""
        self.score = 0
        self.lifes = 3

    def play(self):
        "Function to execute the game"
        self.rules_play()
        self.registrer()
        level = int(input("What difficulty do you want to choose?: \n"))

        if level == 1:
            self.rules_lvl1()
            for n in range(1, 101):
                if self.lifes > 0:
                    print(f"The number is: {n}")
                    r = str(input("Type your answer: "))
                    self.execution(n, r)
                else:
                    print("Game over")
                    return

        elif level == 2:
            self.rules_lvl2()
            for j in range(1, 101):
                n = random.randint(1, 99)
                if self.lifes > 0:
                    print("The number is: {}".format(n))
                    r = str(input("Type your answer: "))
                    self.execution(n, r)
                else:
                    print("Game over")
                    return

        elif level == 3:
            self.rules_lvl3()
            for k in range(1, 101):
                n = random.randint(1, 99)
                if self.lifes > 0:
                    print(f"The number is: {n}")
                    timeout = False
                    start = time.time()
                    while not timeout:
                        r = str(input("Type your answer: "))
                        end = time.time()
                        if end - start >= 5:
                            timeout = True
                            print("Time's up!")
                            self.score -= 5
                            self.lifes -= 1
                            if self.lifes <= 0:
                                print("Game over")
                                return
                        elif r.strip() == "":
                            print("Please enter a valid answer!")
                        else:
                            timeout = True
                            self.execution(n, r, end - start)

                else:
                    print("Game over")
                    return

        elif level <= 0 or level > 3:
            print("Not a valid difficulty")

    def execution(self, n, r, time_toker):
        """Function to execute validation of answers"""

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
        if self.score < 0 :
            self.score = 0
        print("Your score is: {}".format(self.score))
        print("You have {} lifes".format(self.lifes))
        self.save_users("data_base.json")

    def registrer(self):
        self.name = input("Enter your name: ")
        self.users = [{
            "name": self.name,
            "score": self.score
        }]
        return self.users

    def save_users(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                if os.stat(filename).st_size > 0:
                    self.users = json.load(file)
                else:
                    self.users
        else:
            self.users

        updated_user = False
        for u in self.users:
            if u["name"] == self.name:
                u["score"] = self.score
                updated_user = True
                break
        if not updated_user:
            self.users.append({
                "name": self.name,
                "score": self.score
            })
        with open(filename, "w") as file:
            json.dump(self.users, file, indent=2)
            file.write('\n')

    def get_user_score(self, name):
        with open("data_base.json", "r") as file:
            users = json.load(file)
            for user in users:
                if user["name"] == name:
                    print(f"{name}'s score is {user['score']}")
                    return
            print(f"{name} is not found in the database")

    
game = fizzBuzz_game()
game.play()
while True:
    name = input("Enter a name to check their score, or 'exit' to exit: ")
    if name.lower() == "exit":
        break
    game.get_user_score(name)
