import random

#Create a list containing the names of your 5 favorite fruits.
word_list = ["apple", "banana", "pear", "grapes", "cherry"]

#_ to protect variable
#__ to make variable private


#create hangman class wiht two parameters
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #initialising all attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    #get and check user input
    def ask_for_input(self):
        while True:
            #obtain guess of letter from user
            guess = input(str("Guess a single letter :"))
            #print error is charecter is not an alphabet nor a single charecter
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical charecter.")
            
            #check if the guess has already been made
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")       
                
            # when carecter is from the alphabet and in single
            else:
                #Append the guess to the list_of_guesses ##moved up 
                self.list_of_guesses.append(guess)

                #call check guess method
                self.check_guess(guess)
                break ##a break was missing all this time! Thanks for pointing out Jared.

    #check if letter is in random word from word list
    def check_guess(self, guess): 
        #ensure letter is in lowercase
        letter_in_lowercase = guess.lower()
        
        #check charecter appears in the randomly selected word from the list
        if letter_in_lowercase in self.word:
            print(f"Good guess! {guess} is in the word.")

            # Create a for-loop that will loop through each letter in the word
            for i, letter in enumerate(self.word):
                # Create an if statement that checks if the letter is equal to the guess
                if letter == guess:
                    #In the if block, replace the corresponding "_" in the word_guessed with the guess
                    self.word_guessed[i] = guess

            # Outside the for-loop, reduce the variable num_letters by 1
            self.num_letters = self.num_letters - 1
            
            # line for checking code commented out.
            print(self.word_guessed, self.list_of_guesses)
        
        else: 
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
          
#run functions
def play_game(word_list):
    #assigned number of lives to 5
    num_lives = 5
    #instance of hangman class with to arguments
    game = Hangman(word_list, num_lives)

    #body of loop checking humber of lives, numer and letters
    while True:
        #test code to keep track of numbers for test purposes
        print(f"number of lives: {game.num_lives}, number of letters: {game.num_letters}")
        if game.num_lives == 0 or game.num_letters == 0:
            print("You lost!")
            #test code results on the fly
            #print(game.num_lives) ##now moved up
            break
        elif game.num_letters > 0:
            #test code results on the fly
            #print(game.num_letters)  ##now moved up
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(word_list)