import random

#Create a list containing the names of your 5 favorite fruits.
word_list = ["apple", "banana", "pear", "grapes", "cherry"]

#random method to select from list
random_word_from_word_list = random.choice(word_list)

#get and check user input
def ask_for_input():
    while True:
        #user input
        guess = input(str("Enter a single letter :"))
        #checks
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

#check if letter is in random word from word list
def check_guess(guess): 
    guess = guess.lower()
    if guess in random_word_from_word_list:
        print(f"Good guess! {guess} is in the word.")
    else: 
        print("Sorry, {guess} is not in the word. Try again.")
          
#run functions
check_guess(ask_for_input())