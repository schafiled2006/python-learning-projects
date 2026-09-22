import string

ALPHABET = string.ascii_lowercase

def shift_char(ch, k):
    if ch not in ALPHABET:
        return ch
    idx = (ALPHABET.index(ch) + k) % 26
    return ALPHABET[idx]

def encode(text, k):
    return "".join(shift_char(c, k) for c in text.lower())

def decode(text, k):
    return encode(text, -k)

if __name__ == "__main__":
    msg = input("message: ")
    k = int(input("shift: "))
    secret = encode(msg, k)
    print("encoded:", secret)
    print("decoded:", decode(secret, k))
