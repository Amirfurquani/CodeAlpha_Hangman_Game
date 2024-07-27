import random

def choose_word(words):
    return random.choice(words)

def play_hangman():
    words = ["delhi", "mumbai", "patna", "pune", "kochi", "mysore", "nagpur", "surat", "indore", "kanpur"]
    word = choose_word(words)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("HINT 1: - It's an Indian city")     
    print(f"HINT 2: - The city name has {len(word)} letters")

    while attempts < max_attempts:
        word_display = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
        print(word_display)

        if set(word_display.replace(' ', '')) == word_letters:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word_letters:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Oops! That letter is not in the word.")
            attempts += 1
            print(f"You have {max_attempts - attempts} attempts left.")

    else:
        print("Sorry, you ran out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing Hangman!")

if __name__ == "__main__":
    play_hangman()
