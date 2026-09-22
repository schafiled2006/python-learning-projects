import argparse
import json
import os

DATA = 'todos.json'

def load():
    if not os.path.exists(DATA):
        return []
    with open(DATA, 'r', encoding='utf-8') as f:
        return json.load(f)

def save(t):
    with open(DATA, 'w', encoding='utf-8') as f:
        json.dump(t, f, ensure_ascii=False, indent=2)

def add(text):
    t = load()
    t.append({'task': text, 'done': False})
    save(t)

def list_all():
    t = load()
    for i, it in enumerate(t, 1):
        print(i, '[x]' if it.get('done') else '[ ]', it.get('task'))

def done(idx):
    t = load()
    if 0 < idx <= len(t):
        t[idx-1]['done'] = True
        save(t)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--add')
    p.add_argument('--list', action='store_true')
    p.add_argument('--done', type=int)
    args = p.parse_args()
    if args.add:
        add(args.add)
    if args.list:
        list_all()
    if args.done:
        done(args.done)

if __name__ == '__main__':
    main()


def clamp(value, low, high):
    """Keep value inside [low, high]."""
    return max(low, min(high, value))
