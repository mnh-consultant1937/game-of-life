# game.py
import os

# ------------------------------
# CONFIGURATION
# ------------------------------
WIDTH = 5
HEIGHT = 5
DELAY = 0.1  # auto-run delay in seconds

# ------------------------------
# PREDEFINED PATTERNS
# ------------------------------
patterns = {
    "neighbor_test": [(0, 0), (1, 1)],
    "toad": [(4,4), (3,5), (3,6), (5,7), (6,5), (6,6)],
    "beacon": [(2,3), (2,4), (3,3), (3,4), (4,5), (4,6), (5,5), (5,6)],
    "glider": [(1,2), (2,3), (3,1), (3,2), (3,3)],
    "pulsar": [(2,4), (2,5), (2,6), (4,2), (4,7), (5,2), (5,7),
               (6,2), (6,7), (7,4), (7,5), (7,6)],
    "diehard": [(5,7), (6,7), (6,8), (10,8), (11,8), (12,8), (11,6)]
}

# ------------------------------
# BOARD FUNCTIONS
# ------------------------------
def create_board():
  board = []

  for row in range(HEIGHT):
    row_cells = []

    for col in range(WIDTH):
      row_cells.append('.')

    board.append(row_cells)

  return board

def display_board(board):
    """Print the board"""
    print("\nCurrent Board:")
    for row in board:
        print(' '.join(row))
    print()

def clear_screen():
    if os.name == 'nt':          # Windows
        os.system('cls')
    else:                        # Linux / macOS
        os.system('clear')

# ------------------------------
# GAME LOGIC
# ------------------------------
def count_live_neighbors(board, x, y):
    """Count live neighbors of a cell"""
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if board[ny][nx] == 'O':
                count += 1
    return count

def simulate(board):
    """Compute next generation"""
    new_board = create_board()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_live_neighbors(board, x, y)
            if board[y][x] == 'O':  # alive
                new_board[y][x] = 'O' if 2 <= neighbors <= 3 else '.'
            else:  # dead
                new_board[y][x] = 'O' if neighbors == 3 else '.'
    return new_board

def toggle_cell(board, x, y):
    """Toggle a cell alive/dead"""
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        board[y][x] = '.' if board[y][x] == 'O' else 'O'
    else:
        print("Coordinates out of range!")

def seed_pattern(board, pattern_name):
    """Seed a predefined pattern"""
    if pattern_name in patterns:
        for x, y in patterns[pattern_name]:
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                board[y][x] = 'O'
    else:
        print("Pattern not found!")
