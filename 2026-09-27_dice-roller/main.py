import random

DICE_ART = {
    1: "one", 2: "two", 3: "three",
    4: "four", 5: "five", 6: "six",
}

def roll(sides=6):
    return random.randint(1, sides)

def main():
    while True:
        cmd = input("roll? (y/n) ").strip().lower()
        if cmd != "y":
            break
        value = roll()
        print(f"You rolled a {value} ({DICE_ART[value]})")
    print("bye!")

if __name__ == "__main__":
    main()
