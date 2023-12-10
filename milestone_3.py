import random

#Create a list containing the names of your 5 favorite fruits.
word_list_of_fruits = ["apple", "banana", "pear", "grapes", "cherry"]

#random method to select from list
random_fruit_from_list = random.choice(word_list_of_fruits)

#get and check user input
def ask_for_input():
    while True:
        #user input
        user_guesses_a_letter = input(str("Enter a single letter :"))
        #checks
        if len(user_guesses_a_letter) == 1 and user_guesses_a_letter.isalpha():
            return user_guesses_a_letter
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

#check if letter is in random word from word list
def check_guess(user_guesses_a_letter): 
    letter_in_lowercase = user_guesses_a_letter.lower()
    if letter_in_lowercase in random_fruit_from_list:
        print(f"Good guess! {user_guesses_a_letter} is in the word.")
    else: 
        print("Sorry, {guess} is not in the word. Try again.")
          
#run functions
check_guess(ask_for_input())