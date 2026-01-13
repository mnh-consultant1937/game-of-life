# main.py
import time
from game import create_board, display_board, toggle_cell, seed_pattern, simulate, clear_screen, patterns, DELAY
from persistence import save_game, load_game

def auto_run(board, generation):
    """Run simulation continuously until KeyboardInterrupt"""
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
        print("5. Save game")
        print("6. Load game")
        print("7. Quit")

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
            save_game(board, generation)

        elif choice == '6':
            loaded_board, loaded_generation = load_game()
            if loaded_board:
                board = loaded_board
                generation = loaded_generation

        elif choice == '7':
            save_game(board, generation)  # optional auto-save on exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
