# persistence.py
import sqlite3
import json
from game import WIDTH, HEIGHT

DB_FILE = "game_save.db"

def init_db():
    """Create the database and table if not exists"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS saves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            board TEXT,
            generation INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_game(board, generation, slot_name="default"):
    """Save the current board and generation to a named slot"""
    init_db()
    board_json = json.dumps(board)  # convert 2D list to JSON
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        INSERT INTO saves (name, board, generation)
        VALUES (?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
            board=excluded.board,
            generation=excluded.generation
    """, (slot_name, board_json, generation))
    conn.commit()
    conn.close()
    print(f"Game saved to slot '{slot_name}'.")

def load_game(slot_name="default"):
    """Load a saved game by slot name"""
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT board, generation FROM saves WHERE name=?", (slot_name,))
    row = c.fetchone()
    conn.close()
    if row:
        board_json, generation = row
        board = json.loads(board_json)
        print(f"Game loaded from slot '{slot_name}'.")
        return board, generation
    else:
        print(f"No saved game found in slot '{slot_name}'.")
        return None, 1

def list_slots():
    """List all saved slots"""
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT name FROM saves")
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]
