# 📦 Dice Roller – Release Notes

## 🎲 Version 1.1 – Multi-Dice Support & CLI Upgrade
**Release Date:** [fill in date]

This update brings full support for various polyhedral dice using RPG-style notation (e.g. `2d8+1`) and unifies the visual output style across all dice types. It's a major step toward full tabletop utility.

### 🚀 New Features
- 🎲 **Support for any dice type** using standard notation: `NdX+M`  
  *(Examples: `3d20`, `1d8+2`, `4d4-1`)*
- ✅ **Uniform visual output** for all dice (number-centered ASCII faces)
- 🧰 **Command-line interface (CLI)** via `argparse` for cleaner usage
- 🖥️ Optional modifier display and total calculation
- 📦 Ready for packaging as a CLI tool with `dice-roller` entry point
- 🏷️ Version metadata added (`__version__ = "1.1"`)

### 🔧 Example Usage
```bash
$ dice-roller 3d10+2

~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~
┌─────┐ ┌─────┐ ┌─────┐
│  7  │ │  2  │ │ 10  │
└─────┘ └─────┘ └─────┘
Modifier: +2
Total: 19 +2 = 21
```

---

## 🎲 Version 1.0 – Initial Release
**Release Date:** [fill in date]

This is the first official release of the `dice-roller` project — a simple yet effective command-line tool written in Python for rolling six-sided dice (D6) with visual feedback.

### 🚀 Features
- Roll 1 to 6 six-sided dice
- Each roll displays as an ASCII-art D6 face
- Input validation for user-entered dice count
- Modular code structure for future extensibility
- Fully standalone, requires only the Python standard library

### 🧱 Example Usage
```bash
$ python dice_roller.py
How many dice do you want to roll? [1–6] 3

~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
┌─────────┐ ┌─────────┐ ┌─────────┐
│  ●   ●  │ │    ●    │ │  ●   ●  │
│         │ │         │ │         │
│  ●   ●  │ │    ●    │ │  ●   ●  │
└─────────┘ └─────────┘ └─────────┘
```

---

