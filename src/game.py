import os
import json
import hashlib
from src import crypto
class Game:
    def __init__(self):
        self.decryption = ["caesar", "xor", "viginere"]
        self.modes = ['easy', 'medium', 'hard']
        self.mode = ""
        with open("./.wordlists/hash_challenges.json", 'r') as f:
            self.data = json.load(f)
         
    def getMode(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.mode = input("\033[0mPick your mode: (Easy, Medium, Hard)\033[36m ").lower()
        while self.mode not in self.modes:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.mode = input("\033[0mPlease enter a valid mode: (Easy, Medium, Hard)\033[36m ").lower()

        return self.play()

    def play(self):
        level = 0
        while level < len(self.data[self.mode]):
            os.system('cls' if os.name == 'nt' else 'clear')

            current_entry = self.data[self.mode][level]
            algorithm = current_entry['algorithm'].lower()
            stored_hash = current_entry['hash']
            stored_answer = current_entry['answer']
            hint = current_entry['hint']

            show_tools = False 
            hashText = ""
            shift = ""
            key = ""
            crackedHash = ""
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[36mHash: {stored_hash}\033[0m\n{hint}")

                if crackedHash:
                    print(f"\033[92mCracked Hash: {crackedHash}\033[0m")

                if show_tools:
                    print("\033[32mTools:")
                    for tool in self.decryption:
                        print(f"\033[32m{tool}\033[0m")
                guess = input("\033[0mEnter your guess (or type 'tools', 'exit'):\033[36m ").strip()

                if guess.lower() in self.decryption:
                    shift = ""
                    key = ""
                    hashText = input("\033[0mWhat is the hash?\033[36m ")
                    if guess.lower() == 'caesar':
                        while not shift:
                            shift = input("\033[0mHow far would you like to shift the text?\033[36m ")
                            for char in shift:
                                if char.isalpha():
                                    shift = ""
                                    break
                        crackedHash = crypto.caesar_cipher(hashText, int(shift), 'decrypt')
                    else:
                        while not key:
                            key = input("\033[0mWhat is the key to the cipher?\033[36m ")
                        
                        if guess.lower() == 'xor':
                            crackedHash = crypto.xor(hashText, key, 'decrypt')
                        elif guess.lower() == 'vigenere':
                            crackedHash = crypto.vigenere(hashText, key, 'decrypt')

                    show_tools = False
                    continue

                if guess.lower() == "tools":
                    show_tools = True
                    continue

                if guess.lower() == "exit":
                    return self.lose()

                if self.check_guess(guess, stored_answer, algorithm):
                    print("Correct!")
                    level += 1
                    break
                else:
                    print("Incorrect. Try again.")

        next_mode = ""
        while next_mode not in ['yes', 'no']:
            next_mode = input("\033[0mWould you like to play a different difficulty? ('yes' or 'no'):\033[36m ").lower()

        if next_mode == "yes":
            return self.getMode()

        return self.win()

    def check_guess(self, guess, stored_hash, algorithm):
        guess = guess.lower().encode('utf-8')
        guess_hash = hashlib.md5(guess).hexdigest()

        return guess_hash == stored_hash

    def win(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\033[32mCongratulations! You completed {self.mode} mode!\033[0m")

    def lose(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[31mBetter luck next time!\033[0m")
