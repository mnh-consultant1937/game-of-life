# persistence.py
import json
import os

SAVE_FILE = "game_save.json"

def save_game(board, generation):
    """Save the current board and generation to a JSON file"""
    data = {"board": board, "generation": generation}
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
        print(f"Game saved to {SAVE_FILE}")
    except Exception as e:
        print("Error saving game:", e)

def load_game():
    """Load the board and generation from a JSON file"""
    if not os.path.exists(SAVE_FILE):
        print("No saved game found.")
        return None, 1  # default empty board and generation
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        print(f"Game loaded from {SAVE_FILE}")
        return data["board"], data["generation"]
    except Exception as e:
        print("Error loading game:", e)
        return None, 1
