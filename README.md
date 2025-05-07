<p align="center">
    <img src="https://github.com/mattyhakin/dice-roller/blob/main/dice-roller-header.png?raw=true" alt="Dice Roller"/>

# 🎲 Dice Roller

A lightweight and flexible Python tool for simulating dice rolls. Perfect for tabletop RPGs, board games, and quick probability testing.

## 🔧 Features

- Roll any standard or custom dice (e.g., d6, d20, d100)
- Support for multiple dice (e.g., 3d6)
- Optional modifiers (e.g., 2d8 + 3)
- CLI interface for quick access
- Extensible for future GUI or API versions

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mattyhakin/dice-roller.git
cd dice-roller
```

(Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Install requirements if needed:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the CLI tool from the terminal:

```bash
python dice_roller.py 2d6
```

With modifiers:

```bash
python dice_roller.py 3d8+4
```

You can also import it as a module:

```python
from dice_roller import roll

result = roll("4d10+2")
print(f"Rolled: {result}")
```

## 📁 Project Structure (Planned)

```
dice-roller/
├── dice_roller.py
├── tests/
│   └── test_dice_roller.py
├── README.md
├── LICENSE
└── requirements.txt
```

## ✅ To Do

- [ ] Add unit tests
- [ ] Add input validation and error messages
- [ ] Expand CLI options (e.g., verbosity, statistics)
- [ ] (Optional) Add GUI version

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Happy rolling!
