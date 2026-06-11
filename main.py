import dice
import dnd


def main():
    while True:
        print("\n=== VEILED SOCIETY TOOLKIT ===")
        print("1. Roll Dice")
        print("2. Generate Tavern Quest")
        print("3. Exit")

        choice = input("> ").strip()

        if choice == "1":
            dice.main()

        elif choice == "2":
            dnd.generate_scene()

        elif choice == "3":
            print("The tavern fades into the mist...")
            break

        else:
            print("Pick 1, 2, or 3, brave adventurer.")


if __name__ == "__main__":
    main()