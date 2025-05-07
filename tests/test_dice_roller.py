import re
import pytest
from dice_roller import parse_dice_notation, roll_dice, generate_number_face, generate_dice_faces_diagram

def test_parse_dice_notation_basic():
    assert parse_dice_notation("2d6") == (2, 6, 0)
    assert parse_dice_notation("d20") == (1, 20, 0)
    assert parse_dice_notation("3d8+2") == (3, 8, 2)
    assert parse_dice_notation("4d10-1") == (4, 10, -1)

def test_parse_dice_notation_invalid():
    with pytest.raises(SystemExit):
        parse_dice_notation("2d")

def test_roll_dice_range():
    rolls = roll_dice(10, 6)
    assert len(rolls) == 10
    assert all(1 <= roll <= 6 for roll in rolls)

def test_generate_number_face_format():
    face = generate_number_face(12)
    assert face[1].strip("│ ").isdigit()
    assert face[0].startswith("┌") and face[2].startswith("└")

def test_generate_dice_faces_diagram_structure():
    rolls = [3, 5, 7]
    diagram = generate_dice_faces_diagram(rolls)
    lines = diagram.split("\n")
    assert "RESULTS" in lines[0]
    assert len(lines) == 4
