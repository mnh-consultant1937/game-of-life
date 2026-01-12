import time
import os



WIDTH = 5
HEIGHT = 5
DELAY = 0.1

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

# Step 1: Simple board creation and display
def create_board():
  board = []

  for row in range(HEIGHT):
    row_cells = []

    for col in range(WIDTH):
      row_cells.append('.')

    board.append(row_cells)

  return board

def display_board(board):
  print("\nCurrent Board:")
  for row in board:
    print(' '.join(row))
  print()

def count_live_neighbors(board, x, y):

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    count = 0

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
          if board[ny][nx] == 'O':
            count += 1

    return count

# ------------------------------
# SEED PATTERN
# ------------------------------
def seed_pattern(board, pattern_name):
    if pattern_name in patterns:
        for x, y in patterns[pattern_name]:
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                board[y][x] = 'O'
    else:
        print("Pattern not found!")

def simulate(board):
    new_board = create_board()  # IMPORTANT: fresh board

    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_live_neighbors(board, x, y)

            if board[y][x] == 'O':  # cell is alive
                if neighbors < 2 or neighbors > 3:
                    new_board[y][x] = '.'
                else:
                    new_board[y][x] = 'O'
            else:  # cell is dead
                if neighbors == 3:
                    new_board[y][x] = 'O'

    return new_board

def toggle_cell(board, x, y):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        if board[y][x] == 'O':
            board[y][x] = '.'
        else:
            board[y][x] = 'O'
    else:
        print("Coordinates out of range!")

def clear_screen():
    if os.name == 'nt':          # Windows
        os.system('cls')
    else:                        # Linux / macOS
        os.system('clear')

def auto_run(board, generation):
    try:
        while True:
            clear_screen()
            print(f"Generation: {generation}")
            display_board(board)
            board = simulate(board)
            generation += 1
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("\nAuto-run stopped.")
        return board, generation

# # Vertical line (oscillator)
# board[1][2] = 'O'
# board[2][2] = 'O'
# board[3][2] = 'O'

def menu():
    board = create_board()
    generation = 1

    while True:
        display_board(board)
        print(f"Generation: {generation}")
        print("1. Toggle a cell")
        print("2. Seed a predefined pattern")
        print("3. Next generation")
        print("4. Auto-run")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                x = int(input("Enter X (column): "))
                y = int(input("Enter Y (row): "))
                toggle_cell(board, x, y)
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == "2":
            print("Available patterns:", ", ".join(patterns.keys()))
            pattern = input("Enter pattern name: ")
            seed_pattern(board, pattern)

        elif choice == '3':
            board = simulate(board)
            generation += 1

        elif choice == '4':
            board, generation = auto_run(board, generation)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

# RUN PROGRAM
menu()

# if __name__ == "__main__":
#     menu()

# Possible upgrade:
# Make the grid bigger

# Add random initialization

# Add edge wrapping

# Refactor into a class-based design

# Add edge wrapping 🌍

# Add random seeding 🎲

# Move this to Pygame for real graphics 🖥️

# Optimize with NumPy ⚡



