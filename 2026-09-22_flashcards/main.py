import csv
import random

CARDS_FILE = "cards.csv"

def load_cards():
    with open(CARDS_FILE, newline="") as fh:
        return [(q, a) for q, a in csv.reader(fh)]

def quiz():
    cards = load_cards()
    random.shuffle(cards)
    score = 0
    for question, answer in cards:
        input(f"Q: {question} (enter to reveal)")
        guess = input("your answer: ").strip().lower()
        if guess == answer.lower():
            print("correct!")
            score += 1
        else:
            print(f"answer was: {answer}")
    print(f"score: {score}/{len(cards)}")

quiz()
