import random
import os
import re
import argparse

__version__ = "1.1"

DIE_FACE_WIDTH = 7
DIE_FACE_HEIGHT = 3
DIE_FACE_SEPARATOR = " "

def parse_dice_notation(notation):
    """Parse dice notation like '2d6+1' into (num, sides, modifier)."""
    match = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", notation.strip())
    if not match:
        print("Invalid dice notation. Use NdX+M format like '2d6+1'.")
        raise SystemExit(1)
    num = int(match.group(1)) if match.group(1) else 1
    sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0
    return num, sides, modifier

def roll_dice(num, sides):
    """Roll `num` dice with `sides` sides."""
    return [random.randint(1, sides) for _ in range(num)]

def generate_number_face(value, width=DIE_FACE_WIDTH):
    """Generate a uniform dice face with centered number."""
    value_str = str(value)
    inner_width = width - 2
    padding_total = inner_width - len(value_str)
    left_padding = padding_total // 2
    right_padding = padding_total - left_padding
    top = "┌" + "─" * inner_width + "┐"
    middle = "│" + " " * left_padding + value_str + " " * right_padding + "│"
    bottom = "└" + "─" * inner_width + "┘"
    return [top, middle, bottom]

def generate_dice_faces_diagram(rolls):
    """Generate a diagram for multiple dice faces."""
    faces = [generate_number_face(value) for value in rolls]
    rows = [DIE_FACE_SEPARATOR.join(face[i] for face in faces) for i in range(DIE_FACE_HEIGHT)]
    header = " RESULTS ".center(len(rows[0]), "~")
    return "\n".join([header] + rows)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    parser = argparse.ArgumentParser(description="Roll dice using NdX+M notation (e.g. 2d6+1)")
    parser.add_argument("notation", type=str, help="Dice notation (e.g. 2d6+1)")
    args = parser.parse_args()

    clear_console()
    num, sides, modifier = parse_dice_notation(args.notation)
    rolls = roll_dice(num, sides)
    total = sum(rolls) + modifier
    diagram = generate_dice_faces_diagram(rolls)

    print(f"\n{diagram}")
    print(f"Modifier: {modifier:+}")
    print(f"Total: {sum(rolls)} {modifier:+} = {total}")

if __name__ == "__main__":
    main()
