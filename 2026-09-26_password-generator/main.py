import string
import secrets

CHARS = string.ascii_letters + string.digits + "!@#$%&*"

def make_password(length=12):
    if length < 6:
        raise ValueError("too short")
    return "".join(secrets.choice(CHARS) for _ in range(length))

def make_many(count, length=12):
    return [make_password(length) for _ in range(count)]

if __name__ == "__main__":
    for p in make_many(3):
        print(p)
