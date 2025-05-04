import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile programming language.",
    "Typing fast requires a lot of practice.",
    "Consistency is the key to improvement.",
    "AI is changing the way we interact with technology."
]

def typing_test():
    print("Welcome to Typing Speed Tester!\n")
    input("Press Enter to start...")

    sentence = random.choice(sentences)
    print("\nType the following sentence:\n")
    print(f"> {sentence}\n")

    start_time = time.time()
    typed_text = input("Start typing:\n")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)
    word_count = len(sentence.split())
    speed = round(word_count / (time_taken / 60), 2)  # words per minute

    errors = sum(1 for a, b in zip(sentence, typed_text) if a != b)
    extra_chars = abs(len(sentence) - len(typed_text))
    total_errors = errors + extra_chars

    print("\n--- Results ---")
    print(f"Time Taken: {time_taken} seconds")
    print(f"Typing Speed: {speed} WPM")
    print(f"Errors: {total_errors}")

typing_test()

