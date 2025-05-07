import random
import os

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string, max_dice=6):
    """Validate user input: return an integer between 1 and `max_dice`."""
    if input_string.isdigit():
        value = int(input_string)
        if 1 <= value <= max_dice:
            return value
    print(f"Please enter a number from 1 to {max_dice}.")
    raise SystemExit(1)

def roll_dice(num_dice):
    """Roll `num_dice` D6 dice and return a list of integers."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def generate_dice_faces_diagram(dice_values):
    """Return a string ASCII diagram of the rolled dice."""
    dice_faces = [_get_dice_art(value) for value in dice_values]
    dice_rows = _generate_dice_rows(dice_faces)
    width = len(dice_rows[0])
    header = " RESULTS ".center(width, "~")
    return "\n".join([header] + dice_rows)

def _get_dice_art(value):
    return DICE_ART[value]

def _generate_dice_rows(dice_faces):
    return [
        DIE_FACE_SEPARATOR.join(die[row] for die in dice_faces)
        for row in range(DIE_HEIGHT)
    ]

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    clear_console()
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)
    roll_results = roll_dice(num_dice)
    diagram = generate_dice_faces_diagram(roll_results)
    print(f"\n{diagram}")
