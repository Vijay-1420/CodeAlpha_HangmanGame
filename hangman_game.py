import random

hangman_words = ["python", "java", "javascript", "hangman", "programming"]
secret_word = random.choice(hangman_words)

print("Welcome to Hangman!")

display = []
for _ in range(len(secret_word)):
    display.append("_")
print(" ".join(display))

guessed_letters = []
lives = 6
game_over = False

while game_over is False:
    # 1. Player guesses
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
        
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
        
    guessed_letters.append(guess)
    
    # 2. Check guess & 3. Update display (if needed)
    if guess in secret_word:
        for position in range(len(secret_word)):
            letter = secret_word[position]
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"Lives remaining: {lives}")
        
    # 4. Print display
    print(" ".join(display))
    
    # 5. Check win
    if "_" not in display:
        game_over = True
        print("You win!")
        continue  # Skips the loss check since they won
        
    # 6. Check lose
    if lives == 0:
        game_over = True
        print("You lose!")
        print(f"The secret word was: {secret_word}")