import sqlite3
import random

DB = "dnd_tavern.db"

def setup():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS npcs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        race TEXT,
        trait TEXT,
        secret TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS quests (
        id INTEGER PRIMARY KEY,
        hook TEXT,
        reward TEXT,
        danger TEXT
    )
    """)

    if cur.execute("SELECT COUNT(*) FROM npcs").fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO npcs (name, race, trait, secret) VALUES (?, ?, ?, ?)",
            [
                ("Mira Ashbrew", "Dwarf", "laughs too loudly", "owes money to goblins"),
                ("Tovin Blackcap", "Halfling", "never blinks", "is a retired assassin"),
                ("Seraphine Vex", "Tiefling", "speaks in riddles", "knows where a cursed relic is"),
                ("Old Bren", "Human", "collects broken keys", "was once a royal spy"),
            ],
        )

    if cur.execute("SELECT COUNT(*) FROM quests").fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO quests (hook, reward, danger) VALUES (?, ?, ?)",
            [
                ("A cellar door screams every midnight.", "50 gold and free lodging", "a mimic nest"),
                ("A bard vanished after singing a forbidden song.", "a silver lute pick", "a jealous ghost"),
                ("Someone is stealing shadows from patrons.", "100 gold", "a fey debt collector"),
                ("A caravan arrived with no driver.", "a mysterious map", "undead horses"),
            ],
        )

    con.commit()
    con.close()

def random_row(table):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    rows = cur.execute(f"SELECT * FROM {table}").fetchall()
    con.close()
    return random.choice(rows)

def generate_scene():
    npc = random_row("npcs")
    quest = random_row("quests")

    print("\n=== THE VEILED TAVERN NOTICE ===")
    print(f"NPC: {npc[1]} the {npc[2]}")
    print(f"Trait: {npc[3]}")
    print(f"Secret: {npc[4]}")
    print()
    print(f"Quest Hook: {quest[1]}")
    print(f"Reward: {quest[2]}")
    print(f"Danger: {quest[3]}")
    print("===============================\n")

def main():
    setup()

    while True:
        print("1. Generate tavern quest")
        print("2. Exit")
        choice = input("> ")

        if choice == "1":
            generate_scene()
        elif choice == "2":
            break
        else:
            print("Pick 1 or 2, brave bard.")

if __name__ == "__main__":
    main()