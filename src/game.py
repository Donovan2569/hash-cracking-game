import os
import json
import hashlib

class Game:
    def __init__(self):
        self.modes = ['easy', 'medium', 'hard']
        self.mode = ""
        with open("./.wordlists/hash_challenges.json", 'r') as f:
            self.data = json.load(f)
         
    def getMode(self):
        self.mode = input("Pick your mode: (Easy, Medium, Hard) ").lower()
        while self.mode not in self.modes:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.mode = input("Please enter a valid mode: (Easy, Medium, Hard) ").lower()

        return self.play()

    def play(self):
        level = 0
        while level < len(self.data[self.mode]):
            os.system('cls' if os.name == 'nt' else 'clear')

            current_entry = self.data[self.mode][level]
            algorithm = current_entry['algorithm'].lower()
            stored_hash = current_entry['hash']
            hint = current_entry['hint']

            show_hint = False 

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{self.mode.capitalize()} {algorithm} {stored_hash}")

                if show_hint:
                    print(f"Hint: {hint}")

                guess = input("Enter your guess (or type 'hint', 'exit'): ").strip()

                if guess.lower() == "hint":
                    show_hint = True
                    continue

                if guess.lower() == "exit":
                    return self.lose()

                if self.check_guess(guess, stored_hash, algorithm):
                    print("Correct!")
                    level += 1
                    break
                else:
                    print("Incorrect. Try again.")

        next_mode = ""
        while next_mode not in ['yes', 'no']:
            next_mode = input("Would you like to play a different difficulty? ('yes' or 'no'): ").lower()

        if next_mode == "yes":
            return self.getMode()

        return self.win()

    def check_guess(self, guess, stored_hash, algorithm):
        guess = guess.lower().encode('utf-8')

        if algorithm == 'md5':
            guess_hash = hashlib.md5(guess).hexdigest()
        elif algorithm == 'sha1':
            guess_hash = hashlib.sha1(guess).hexdigest()
        elif algorithm == 'sha256':
            guess_hash = hashlib.sha256(guess).hexdigest()
        else:
            # default to md5 if unknown algorithm
            guess_hash = hashlib.md5(guess).hexdigest()

        return guess_hash == stored_hash

    def win(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Congratulations! You completed {self.mode} mode!")

    def lose(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Better luck next time!")
