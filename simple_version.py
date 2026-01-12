# Simple Conway's Game of Life
# Beginner-friendly version

# Board size
WIDTH = 5
HEIGHT = 5

# Create an empty board
# def create_board():
#     return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
def create_board():
    board = []

    for row in range(HEIGHT):
        row_cells = []

        for col in range(WIDTH):
            row_cells.append('.')

        board.append(row_cells)

    return board


# Display the board
def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Count live neighbors
def count_live_neighbors(board, x, y):
    neighbors = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),         (0,1),
                 (1,-1), (1,0), (1,1)]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if board[ny][nx] == 'O':
                count += 1
    return count

# Compute next generation
def simulate(board):
    new_board = create_board()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            live_neighbors = count_live_neighbors(board, x, y)
            if board[y][x] == 'O':
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[y][x] = '.'
                else:
                    new_board[y][x] = 'O'
            else:
                if live_neighbors == 3:
                    new_board[y][x] = 'O'
    return new_board

# Main program
board = create_board()

# Manually set a few live cells
board[1][2] = 'O'
board[2][2] = 'O'
board[3][2] = 'O'

# Run 5 generations
for _ in range(5):
    display_board(board)
    board = simulate(board)
