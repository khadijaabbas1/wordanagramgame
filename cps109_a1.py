'''
The purpose of this code is to implement a simple word anagram game where the 
player is tasked with having to unscramble a randomly chosen word. The program
loads a list of words from a file, filters out words that is less than five letters
and then presents the player with a random scrambled word. If the player sucessfully 
unscrambles the word, their score is calculated based on the length of the word,
and consecutive correct guesses contribute to an accumulating score. If the player quits, 
the game concludes and their total score is displaced and the code resets the score to zero.

overall the game aims to provide an interactive and enjoyable word game experience 
while incorporating elements of sequence manipulation, control flow and user feedback. 

'''

# Import random module to shuffle the letters of the word
import random

word_file_path = "wordlist.txt"

# Read the words from a txt file
def load_words_from_file(file_path):
    # Save the words as a list and filter out words less than 5 letters
    with open(file_path, "r") as file:
        words = [word.strip() for word in file.readlines() if len(word.strip()) >= 4]
    return words

def choose_random_word(words): 
    # Choose a random word from the list
    return random.choice(words)

def scramble_word(word): 
    # Scramble the letters of the word
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def calculate_score(word):
    # Calculate the score to be the length of the word multipled by 10
    return len(word) * 10

def save_score(player, score):
    # Save the score of the user to a file
    with open("scores.txt", "a") as file:
        file.write(f"{player}: {score}\n")

def display_instructions():
    # Display the instructions of the anagram game to the user
    print("Welcome to Word Anagram!")
    print("Unscramble the given letters to form a word.")
    print("Type 'quit' to exit the game.")
    print()

def main():
    # Main function to orchestrate the overall flow and structure of the program
    word_file_path = "wordlist.txt" # Input from file
    words = load_words_from_file(word_file_path)
    # Ask the user to input their name
    player_name = input("Enter your name: ")
    display_instructions()
    
    # Create boolean flag to control the main loop
    play_game = True
    # Save the number of consecutive correct guesses and the total score
    consecutive_correct_guesses = 0
    total_score = 0 
    
    while play_game:
        # Loop until the user is able to guess the word or the user decides to give up
        original_word = choose_random_word(words)
        scrambled_word = scramble_word(original_word)
        print(f"Scrambled word: {scrambled_word}")
        
        # Initialize a variable to save the user's guesses
        guess = input("Enter your guess: ").lower()
        if guess == "quit":
            # If user quits then the game will end and the loop will break
            print("Thanks for playing!")
            play_game = False
            # Return score as 0
            total_score = 0
        elif guess == original_word:
            # If the answer is coorect then keep track of consecutive right answers
            consecutive_correct_guesses += 1
            score = calculate_score(original_word) * consecutive_correct_guesses
            print("Congratulations! You guessed it correctly.")
            # Record the overall score of the user
            total_score += score
            score = calculate_score(original_word)
            save_score(player_name, total_score)
            print(f"Your score: {score}")
        else:
            print(f"Incorrect. The correct word is: {original_word}. Try again.")
            # Restart the scoreboard from 0 if the answer is wrong 
            consecutive_correct_guesses = 0
            total_score = 0

    # Display scores from the file
    with open("scores.txt", "r") as file:
        print("\nScores:")
        print(file.read())
        
# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
