import random
import re


def roll_die(sides: int) -> int:
    return random.randint(1, sides)


def roll_dice(expression: str):
    """
    Supports:
    d20
    1d20
    2d6
    4d6+2
    1d20-1
    adv
    dis
    """
    expression = expression.lower().strip()

    if expression == "adv":
        rolls = [roll_die(20), roll_die(20)]
        return {
            "type": "advantage",
            "rolls": rolls,
            "total": max(rolls),
        }

    if expression == "dis":
        rolls = [roll_die(20), roll_die(20)]
        return {
            "type": "disadvantage",
            "rolls": rolls,
            "total": min(rolls),
        }

    pattern = r"^(\d*)d(\d+)([+-]\d+)?$"
    match = re.match(pattern, expression)

    if not match:
        raise ValueError("Use formats like d20, 2d6, 4d6+2, adv, or dis.")

    count = int(match.group(1)) if match.group(1) else 1
    sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    rolls = [roll_die(sides) for _ in range(count)]
    total = sum(rolls) + modifier

    return {
        "type": "dice",
        "expression": expression,
        "rolls": rolls,
        "modifier": modifier,
        "total": total,
    }


def print_roll(result):
    if result["type"] in ["advantage", "disadvantage"]:
        print(f"{result['type'].title()}: {result['rolls']} → {result['total']}")
    else:
        print(f"{result['expression']}: {result['rolls']} + {result['modifier']} → {result['total']}")


def main():
    print("=== DND Dice Roller ===")
    print("Examples: d20, 2d6, 4d6+2, 1d20-1, adv, dis")
    print("Type q to quit.")

    while True:
        choice = input("\nRoll > ")

        if choice.lower() in ["q", "quit", "exit"]:
            break

        try:
            result = roll_dice(choice)
            print_roll(result)
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()