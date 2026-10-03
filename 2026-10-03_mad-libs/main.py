STORY = "Today I bought a {adj} {noun} and it only cost {number} dollars!"

def ask(label, cast=str):
    return cast(input(f"{label}: "))

def fill(story):
    return story.format(
        adj=ask("adjective"),
        noun=ask("noun"),
        number=ask("number", int),
    )

def main():
    print()
    print(fill(STORY))

main()
