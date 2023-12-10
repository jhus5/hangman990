import random

#Create a list containing the names of your 5 favorite fruits.
word_list = ["apple", "banana", "pear", "grapes", "cherry"]

#random method to select from list
random_word_from_word_list = random.choice(word_list)

#user input
guess = input(str("Enter a single letter :"))
#checks
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not not a valid input")