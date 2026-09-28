import json
import os

FILE = "expenses.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def add(amount, note):
    items = load()
    items.append({"amount": amount, "note": note,
                  "at": datetime.now().isoformat(timespec="seconds")})
    with open(FILE, "w") as f:
        json.dump(items, f, indent=2)

def total():
    return sum(i["amount"] for i in load())

from datetime import datetime  # noqa: E402  (used for timestamps)

if __name__ == "__main__":
    add(float(input("amount: ")), input("note: "))
    print("total so far:", total())
