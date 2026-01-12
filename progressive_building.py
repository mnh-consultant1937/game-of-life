# # Step 1: Simple board creation and display

# # Board size
# WIDTH = 5
# HEIGHT = 5

# # 1️⃣ Create the board
# def create_board():
#     board = []

#     for row in range(HEIGHT):
#         row_cells = []

#         for col in range(WIDTH):
#             row_cells.append('.')

#         board.append(row_cells)

#     return board

# # 2️⃣ Display the board
# def display_board(board):
#     for row in board:
#         print(' '.join(row))  # join elements with space for nicer look
#     print()

# # Main
# board = create_board()
# display_board(board)



# STEP 2: Add live cells and count neighbors

# WIDTH = 5
# HEIGHT = 5

# def create_board():
#     return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def display_board(board):
#     for row in board:
#         print(' '.join(row))
#     print()

# # NEW: Count live neighbors
# def count_live_neighbors(board, x, y):
#     # All 8 possible neighbor directions
#     directions = [
#         (-1, -1), (-1, 0), (-1, 1),
#         ( 0, -1),          ( 0, 1),
#         ( 1, -1), ( 1, 0), ( 1, 1)
#     ]

#     count = 0

#     for dx, dy in directions:
#         nx = x + dx
#         ny = y + dy

#         # Boundary check (don’t go outside the board)
#         if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
#             if board[ny][nx] == 'O':
#                 count += 1

#     return count

# # MAIN PROGRAM
# board = create_board()

# # Manually activate some cells (a vertical line)
# # board[1][2] = 'O'
# # board[2][2] = 'O'
# # board[3][2] = 'O'
# board[0][0] = 'O'
# board[1][1] = 'O'
# board[2][2] = 'O'


# display_board(board)

# # Test neighbor count
# # print("Live neighbors of center cell:",
# #       count_live_neighbors(board, 2, 2))
# print("Live neighbors of center cell:",
#       count_live_neighbors(board, 1, 1))




# STEP 3: Simulate the next generation

# WIDTH = 5
# HEIGHT = 5

# def create_board():
#     return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def display_board(board):
#     for row in board:
#         print(' '.join(row))
#     print()

# def count_live_neighbors(board, x, y):
#     directions = [
#         (-1, -1), (-1, 0), (-1, 1),
#         ( 0, -1),          ( 0, 1),
#         ( 1, -1), ( 1, 0), ( 1, 1)
#     ]

#     count = 0
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
#             if board[ny][nx] == 'O':
#                 count += 1
#     return count

# # 🔹 NEW: simulate one generation
# def simulate(board):
#     new_board = create_board()  # IMPORTANT: fresh board

#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             neighbors = count_live_neighbors(board, x, y)

#             if board[y][x] == 'O':  # cell is alive
#                 if neighbors < 2 or neighbors > 3:
#                     new_board[y][x] = '.'
#                 else:
#                     new_board[y][x] = 'O'
#             else:  # cell is dead
#                 if neighbors == 3:
#                     new_board[y][x] = 'O'

#     return new_board

# # MAIN PROGRAM
# board = create_board()

# # Vertical line (oscillator)
# board[1][2] = 'O'
# board[2][2] = 'O'
# board[3][2] = 'O'

# print("Generation 1:")
# display_board(board)

# board = simulate(board)

# print("Generation 2:")
# display_board(board)



# STEP 4: Interactive CLI loop

# WIDTH = 5
# HEIGHT = 5

# def create_board():
#     return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def display_board(board):
#     for row in board:
#         print(' '.join(row))
#     print()

# def count_live_neighbors(board, x, y):
#     directions = [
#         (-1, -1), (-1, 0), (-1, 1),
#         ( 0, -1),          ( 0, 1),
#         ( 1, -1), ( 1, 0), ( 1, 1)
#     ]

#     count = 0
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
#             if board[ny][nx] == 'O':
#                 count += 1
#     return count

# def simulate(board):
#     new_board = create_board()

#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             neighbors = count_live_neighbors(board, x, y)

#             if board[y][x] == 'O':
#                 if neighbors < 2 or neighbors > 3:
#                     new_board[y][x] = '.'
#                 else:
#                     new_board[y][x] = 'O'
#             else:
#                 if neighbors == 3:
#                     new_board[y][x] = 'O'

#     return new_board

# # 🔹 MAIN PROGRAM (CLI LOOP)
# board = create_board()

# # Initial pattern (blinker)
# board[1][2] = 'O'
# board[2][2] = 'O'
# board[3][2] = 'O' 

# generation = 1

# while True:
#     print(f"Generation {generation}")
#     display_board(board)

#     user_input = input("Press ENTER for next generation or Q to quit: ")

#     if user_input.lower() == 'q':
#         print("Exiting simulation.")
#         break

#     board = simulate(board)
#     generation += 1






# STEP 5: Menu-driven CLI with cell toggling

# WIDTH = 5
# HEIGHT = 5

# def create_board():
#     return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# def display_board(board):
#     print("\nCurrent Board:")
#     for row in board:
#         print(' '.join(row))
#     print()

# def count_live_neighbors(board, x, y):
#     directions = [
#         (-1, -1), (-1, 0), (-1, 1),
#         ( 0, -1),          ( 0, 1),
#         ( 1, -1), ( 1, 0), ( 1, 1)
#     ]

#     count = 0
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
#             if board[ny][nx] == 'O':
#                 count += 1
#     return count

# def simulate(board):
#     new_board = create_board()

#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             neighbors = count_live_neighbors(board, x, y)

#             if board[y][x] == 'O':
#                 if neighbors < 2 or neighbors > 3:
#                     new_board[y][x] = '.'
#                 else:
#                     new_board[y][x] = 'O'
#             else:
#                 if neighbors == 3:
#                     new_board[y][x] = 'O'

#     return new_board

# # 🔹 NEW: Toggle a cell
# def toggle_cell(board, x, y):
#     if 0 <= x < WIDTH and 0 <= y < HEIGHT:
#         if board[y][x] == 'O':
#             board[y][x] = '.'
#         else:
#             board[y][x] = 'O'
#     else:
#         print("Coordinates out of range!")

# # 🔹 MENU SYSTEM
# def menu():
#     board = create_board()
#     generation = 1

#     while True:
#         display_board(board)
#         print(f"Generation: {generation}")
#         print("1. Toggle a cell")
#         print("2. Next generation")
#         print("3. Quit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             try:
#                 x = int(input("Enter X (column): "))
#                 y = int(input("Enter Y (row): "))
#                 toggle_cell(board, x, y)
#             except ValueError:
#                 print("Please enter numbers only.")

#         elif choice == '2':
#             board = simulate(board)
#             generation += 1

#         elif choice == '3':
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid choice.")

# # RUN PROGRAM
# menu()




# STEP 6: Auto-run simulation

import time

WIDTH = 5
HEIGHT = 5
DELAY = 0.5  # seconds between generations

def create_board():
    return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

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
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if board[ny][nx] == 'O':
                count += 1
    return count

def simulate(board):
    new_board = create_board()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_live_neighbors(board, x, y)

            if board[y][x] == 'O':
                if neighbors < 2 or neighbors > 3:
                    new_board[y][x] = '.'
                else:
                    new_board[y][x] = 'O'
            else:
                if neighbors == 3:
                    new_board[y][x] = 'O'

    return new_board

def toggle_cell(board, x, y):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        board[y][x] = 'O' if board[y][x] == '.' else '.'
    else:
        print("Coordinates out of range!")

# 🔹 NEW: Auto-run function
def auto_run(board, generation):
    try:
        while True:
            print(f"Generation: {generation}")
            display_board(board)
            board = simulate(board)
            generation += 1
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("\nAuto-run stopped.")
        return board, generation

def menu():
    board = create_board()
    generation = 1

    while True:
        display_board(board)
        print(f"Generation: {generation}")
        print("1. Toggle a cell")
        print("2. Next generation")
        print("3. Auto-run")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                x = int(input("Enter X (column): "))
                y = int(input("Enter Y (row): "))
                toggle_cell(board, x, y)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == '2':
            board = simulate(board)
            generation += 1

        elif choice == '3':
            board, generation = auto_run(board, generation)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

# RUN PROGRAM
menu()

