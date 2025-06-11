# logic.py
# All the core logic for the 2048 game—import this in 2048.py

import random  # We need random numbers for placing new tiles

# Initializes a new game board and prints controls for the user
def start_game():
    mat = []
    for _ in range(4):
        mat.append([0] * 4)  # 4x4 grid, all zeros at the start

    print("Commands are as follows:")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    add_new_2(mat)
    return mat

# Adds a new '2' tile to a random empty cell on the board
def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if not empty_cells:
        return
    r, c = random.choice(empty_cells)
    mat[r][c] = 2  # Place a 2 in a random empty spot

# Checks the current state of the game: WON, GAME NOT OVER, or LOST
def get_current_state(mat):
    # Win if any tile is 2048
    for row in mat:
        if 2048 in row:
            return 'WON'
    # If any cell is 0, game continues
    for row in mat:
        if 0 in row:
            return 'GAME NOT OVER'
    # Check if any adjacent cells can be merged
    for i in range(4):
        for j in range(4):
            if i < 3 and mat[i][j] == mat[i+1][j]:
                return 'GAME NOT OVER'
            if j < 3 and mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
    # No moves left: game lost
    return 'LOST'

# Slides all tiles to the left, removing empty spaces, no merges yet
def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_row = [num for num in mat[i] if num != 0]  # Remove zeros
        new_row += [0] * (4 - len(new_row))  # Fill with zeros at end
        if new_row != mat[i]:
            changed = True
        new_mat.append(new_row)
    return new_mat, changed

# Merges adjacent tiles with the same value, only for left move
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed

# Reverses each row (used for right moves)
def reverse(mat):
    return [row[::-1] for row in mat]

# Swaps rows and columns (used for up/down moves)
def transpose(mat):
    return [list(row) for row in zip(*mat)]

# Executes a left move: compress, merge, then compress again
def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)  # Final squeeze after merges
    return new_grid, changed

# Executes a right move: reverse, move left, reverse again
def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

# Executes an up move: transpose, move left, transpose back
def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

# Executes a down move: transpose, move right, transpose back
def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

# That's it! All game logic lives here. The main game loop goes in 2048.py