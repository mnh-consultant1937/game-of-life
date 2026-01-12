from graphics import *
import random
import tkinter as tk

############################################################
# GLOBAL VARIABLES
############################################################
BLOCK_SIZE = 40
BLOCK_OUTLINE_WIDTH = 2
BOARD_WIDTH = 12
BOARD_HEIGHT = 12

neighbor_test_blocklist = [(0, 0), (1, 1)]
toad_blocklist = [(4,4), (3,5), (3,6), (5,7), (6,5), (6,6)]
beacon_blocklist = [(2,3), (2,4), (3,3), (3,4), (4,5), (4,6), (5,5), (5,6)]
glider_blocklist = [(1,2), (2,3), (3,1), (3,2), (3,3)]
pulsar_blocklist = [(2,4), (2,5), (2,6), (4,2), (4,7), (5,2), (5,7),
                   (6,2), (6,7), (7,4), (7,5), (7,6)]
diehard_blocklist = [(5,7), (6,7), (6,8), (10,8), (11,8), (12,8), (11,6)]

############################################################
# BLOCK CLASS
############################################################
class Block:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.status = 'dead'
        self.new_status = None
        self.canvas = canvas
        self.rect = canvas.drawRect(
            x * BLOCK_SIZE, y * BLOCK_SIZE,
            (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE,
            fill="white"
        )

    def get_coords(self):
        return (self.x, self.y)

    def set_live(self):
        self.status = 'live'
        self.canvas.canvas.itemconfig(self.rect, fill="green")

    def set_dead(self):
        self.status = 'dead'
        self.canvas.canvas.itemconfig(self.rect, fill="white")

    def toggle(self):
        if self.status == 'live':
            self.set_dead()
        else:
            self.set_live()

    def is_live(self):
        return self.status == 'live'

    def reset_status(self):
        if self.new_status == 'live':
            self.set_live()
        elif self.new_status == 'dead':
            self.set_dead()

############################################################
# BOARD CLASS
############################################################
class Board:
    def __init__(self, root):
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.root = root
        self.canvas = CanvasFrame(root, width=self.width*BLOCK_SIZE, height=self.height*BLOCK_SIZE)
        self.canvas.setBackground("white")
        self.delay = 500  # milliseconds

        # Create blocks
        self.block_list = {}
        for x in range(self.width):
            for y in range(self.height):
                block = Block(x, y, self.canvas)
                self.block_list[(x, y)] = block

        # Bind mouse click
        self.canvas.bindMouse(self.on_click)

    def on_click(self, event):
        x = event.x // BLOCK_SIZE
        y = event.y // BLOCK_SIZE
        if (x, y) in self.block_list:
            self.block_list[(x, y)].toggle()

    def seed(self, block_coords):
        for (x, y) in block_coords:
            if (x, y) in self.block_list:
                self.block_list[(x, y)].set_live()

    def get_block_neighbors(self, block):
        neighbors = []
        x, y = block.get_coords()
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbors.append(self.block_list[(nx, ny)])
        return neighbors

    def simulate(self):
        # Step 1: compute new status
        for block in self.block_list.values():
            neighbors = self.get_block_neighbors(block)
            live_neighbors = sum(1 for n in neighbors if n.is_live())
            if block.is_live():
                if live_neighbors < 2 or live_neighbors > 3:
                    block.new_status = 'dead'
                else:
                    block.new_status = 'live'
            else:
                if live_neighbors == 3:
                    block.new_status = 'live'
                else:
                    block.new_status = 'dead'
        # Step 2: apply new status
        for block in self.block_list.values():
            block.reset_status()

    def animate(self):
        self.simulate()
        self.root.after(self.delay, self.animate)

############################################################
# RUNNING THE SIMULATION
############################################################
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conway's Game of Life")
    board = Board(root)

    # Seed initial pattern
    board.seed(toad_blocklist)

    # Start continuous animation
    board.animate()

    root.mainloop()
