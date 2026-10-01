import random

def add_tile(grid):
    empty = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
    if not empty:
        return grid
    r, c = random.choice(empty)
    grid[r][c] = 2 if random.random() < 0.9 else 4
    return grid

def slide(row):
    tiles = [t for t in row if t]
    merged, skip = [], False
    for t in tiles:
        if skip:
            skip = False
        elif merged and merged[-1] == t:
            merged[-1] *= 2
            skip = True
        else:
            merged.append(t)
    return merged + [0] * (4 - len(merged))

def rotate(grid, direction):
    if direction == "a":
        return [list(row) for row in grid]
    if direction == "d":
        return [row[::-1] for row in grid]
    if direction == "w":
        return [list(col) for col in zip(*grid)]
    return [list(col)[::-1] for col in zip(*grid)]

def move(grid, direction):
    rotated = rotate(grid, direction)
    moved = [slide(row) for row in rotated]
    if direction == "d":
        moved = [row[::-1] for row in moved]
    elif direction == "s":
        moved = [list(col) for col in zip(*[row[::-1] for row in moved])]
    elif direction == "w":
        moved = [list(col) for col in zip(*moved)]
    return moved

def show(grid):
    for row in grid:
        print("".join(f"{t or '.':>5}" for t in row))

def main():
    grid = add_tile(add_tile([[0] * 4 for _ in range(4)]))
    while True:
        show(grid)
        key = input("move (wasd/q): ").strip().lower()
        if key == "q":
            break
        if key in ("w", "a", "s", "d"):
            grid = add_tile(move(grid, key))

main()
