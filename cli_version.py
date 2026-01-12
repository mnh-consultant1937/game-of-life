import time
import os

# ------------------------------
# CONFIGURATION
# ------------------------------
BOARD_WIDTH = 12
BOARD_HEIGHT = 12
DELAY = 0.5  # seconds for auto-run

# Predefined patterns
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
# INITIALIZE BOARD
# ------------------------------
def create_board():
    return [['dead' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# ------------------------------
# DISPLAY BOARD
# ------------------------------
def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal
    print("Conway's Game of Life CLI")
    print("-" * (BOARD_WIDTH * 2))
    for row in board:
        print(' '.join('O' if cell == 'live' else '.' for cell in row))
    print("-" * (BOARD_WIDTH * 2))

# ------------------------------
# TOGGLE CELL
# ------------------------------
def toggle_cell(board, x, y):
    if 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT:
        board[y][x] = 'live' if board[y][x] == 'dead' else 'dead'
    else:
        print("Invalid coordinates!")

# ------------------------------
# SEED PATTERN
# ------------------------------
def seed_pattern(board, pattern_name):
    if pattern_name in patterns:
        for x, y in patterns[pattern_name]:
            if 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT:
                board[y][x] = 'live'
    else:
        print("Pattern not found!")

# ------------------------------
# SIMULATE NEXT GENERATION
# ------------------------------
def count_live_neighbors(board, x, y):
    neighbors = [(dx, dy) for dx in [-1,0,1] for dy in [-1,0,1] if not (dx == 0 and dy == 0)]
    live_count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < BOARD_WIDTH and 0 <= ny < BOARD_HEIGHT:
            if board[ny][nx] == 'live':
                live_count += 1
    return live_count

def simulate(board):
    new_board = create_board()
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            live_neighbors = count_live_neighbors(board, x, y)
            if board[y][x] == 'live':
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[y][x] = 'dead'
                else:
                    new_board[y][x] = 'live'
            else:
                if live_neighbors == 3:
                    new_board[y][x] = 'live'
                else:
                    new_board[y][x] = 'dead'
    return new_board

# ------------------------------
# AUTO-RUN SIMULATION
# ------------------------------
def auto_run(board):
    try:
        while True:
            display_board(board)
            board = simulate(board)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

# ------------------------------
# CLI MENU
# ------------------------------
def menu():
    board = create_board()

    while True:
        display_board(board)
        print("Menu:")
        print("1. Toggle a cell")
        print("2. Seed a predefined pattern")
        print("3. Advance one step")
        print("4. Auto-run simulation")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                x = int(input("Enter X coordinate (0-indexed): "))
                y = int(input("Enter Y coordinate (0-indexed): "))
                toggle_cell(board, x, y)
            except ValueError:
                print("Invalid input!")
        elif choice == "2":
            print("Available patterns:", ", ".join(patterns.keys()))
            pattern = input("Enter pattern name: ")
            seed_pattern(board, pattern)
        elif choice == "3":
            board = simulate(board)
        elif choice == "4":
            auto_run(board)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

# ------------------------------
# RUN PROGRAM
# ------------------------------
if __name__ == "__main__":
    menu()


# ------------------------------
# add a feature to save/load 
# patterns from files, so you 
# could reuse or share your 
# configurations
# ------------------------------







