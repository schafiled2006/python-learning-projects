import os
import time

NOTES_DIR = "notes"

def save_note(title, body):
    os.makedirs(NOTES_DIR, exist_ok=True)
    fname = time.strftime("%Y%m%d") + "-" + title.lower().replace(" ", "-") + ".md"
    path = os.path.join(NOTES_DIR, fname)
    with open(path, "w") as fh:
        fh.write(f"# {title}\n\n{body}\n")
    return path

def list_notes():
    if not os.path.isdir(NOTES_DIR):
        return []
    return sorted(os.listdir(NOTES_DIR))

if __name__ == "__main__":
    title = input("title: ")
    print("body (finish with an empty line):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    print("saved:", save_note(title, "\n".join(lines)))
