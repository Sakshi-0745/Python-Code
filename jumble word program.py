import random

words = ['python', 'program', 'developer', 'jumble', 'keyboard', 'laptop', 'syntax', 'variable']
score = 0
def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

print("Welcome to the Jumble Word Game!")
print("Unscramble the letters to guess the word.\nType 'exit' to quit.\n")

while True:
    original = random.choice(words)
    jumbled = jumble_word(original)

    print(f"Jumbled word: {jumbled}")
    guess = input("Your guess: ").lower()

    if guess == 'exit':
        print(f"Game ended. Your final score: {score}")
        break
    elif guess == original:
        score += 1
        print(f"Correct! Score: {score}\n")
    else:
        print(f"Incorrect! The word was '{original}'. Score: {score}\n")
