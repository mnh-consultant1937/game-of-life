import tkinter as tk

# ------------------------------
# Game configuration
# ------------------------------
WIDTH = 5
HEIGHT = 5
DELAY = 300  # milliseconds

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
# Game logic
# ------------------------------
def create_board():
  board = []

  for row in range(HEIGHT):
    row_cells = []

    for col in range(WIDTH):
      row_cells.append('.')

    board.append(row_cells)

  return board

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
                new_board[y][x] = 'O' if neighbors in (2, 3) else '.'
            else:
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

def seed_pattern(board, pattern_name):
    if pattern_name in patterns:
        for x, y in patterns[pattern_name]:
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                board[y][x] = 'O'



# ------------------------------
# GUI setup
# ------------------------------
root = tk.Tk()
root.title("Game of Life")

board = create_board()
buttons = []
running = False
generation = 0

# ------------------------------
# GUI functions
# ------------------------------
def draw_board():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = "black" if board[y][x] == 'O' else "white"
            buttons[y][x].config(bg=color)
    gen_label.config(text=f"Generation: {generation}")

def on_cell_click(x, y):
    toggle_cell(board, x, y)
    draw_board()

def next_generation():
    global board, generation
    board = simulate(board)
    generation += 1
    draw_board()

def auto_run():
    global board, generation
    if running:
        board = simulate(board)
        generation += 1
        draw_board()
        root.after(DELAY, auto_run)

def toggle_auto_run():
    global running
    running = not running
    if running:
        auto_run()
    auto_btn.config(text="Stop" if running else "Auto Run")

def seed_selected_pattern():
    pattern = pattern_var.get()
    seed_pattern(board, pattern)
    draw_board()

# ------------------------------
# Create board buttons
# ------------------------------
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        btn = tk.Button(
            root,
            width=4,
            height=2,
            bg="white",
            command=lambda x=x, y=y: on_cell_click(x, y)
        )
        btn.grid(row=y, column=x)
        row.append(btn)
    buttons.append(row)

# ------------------------------
# Controls
# ------------------------------
# Generation label
gen_label = tk.Label(root, text=f"Generation: {generation}")
gen_label.grid(row=HEIGHT, column=0, columnspan=WIDTH)

# Next generation button
next_btn = tk.Button(root, text="Next Generation", command=next_generation)
next_btn.grid(row=HEIGHT+1, column=0, columnspan=WIDTH, sticky="we")

# Auto-run button
auto_btn = tk.Button(root, text="Auto Run", command=toggle_auto_run)
auto_btn.grid(row=HEIGHT+2, column=0, columnspan=WIDTH, sticky="we")

# Pattern selection
pattern_var = tk.StringVar(root)
pattern_var.set(list(patterns.keys())[0])  # default
pattern_menu = tk.OptionMenu(root, pattern_var, *patterns.keys())
pattern_menu.grid(row=HEIGHT+3, column=0, columnspan=WIDTH, sticky="we")

seed_btn = tk.Button(root, text="Seed Pattern", command=seed_selected_pattern)
seed_btn.grid(row=HEIGHT+4, column=0, columnspan=WIDTH, sticky="we")

# Initial draw
draw_board()

root.mainloop()


