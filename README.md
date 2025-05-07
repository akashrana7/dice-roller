<p align="center">
    <img src="https://github.com/mattyhakin/dice-roller/blob/main/dice-roller-header.png?raw=true" alt="Dice Roller"/>

# 🎲 Dice Roller

[![Build Status](https://img.shields.io/github/actions/workflow/status/mattyhakin/dice-roller/test.yml?branch=main&label=tests)](https://github.com/mattyhakin/dice-roller/actions/workflows/test.yml)
[![Version](https://img.shields.io/github/v/release/mattyhakin/dice-roller?label=version)](https://github.com/mattyhakin/dice-roller/releases)
[![License](https://img.shields.io/github/license/mattyhakin/dice-roller)](https://github.com/mattyhakin/dice-roller/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Commitizen Friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen-tools.github.io/commitizen/)

A lightweight and flexible Python tool for simulating dice rolls. Perfect for tabletop RPGs, board games, and quick probability testing.

...

(Hint: this includes the previous README plus the badges)


![Test Status](https://github.com/mattyhakin/dice-roller/actions/workflows/test.yml/badge.svg)

A lightweight and flexible Python tool for simulating dice rolls. Perfect for tabletop RPGs, board games, and quick probability testing.

## 🔧 Features

- Roll any standard or custom dice using NdX+M notation (e.g., d6, d20, 3d8+2)
- Uniform number-based ASCII output for all dice types
- CLI tool with argparse support
- Ready for packaging and publishing on PyPI
- Automatic testing via GitHub Actions

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

Install locally:
```bash
pip install .
```

## 🚀 Usage

Run from the command line:

```bash
dice-roller 3d6+1
```

Example output:
```
~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~
┌─────┐ ┌─────┐ ┌─────┐
│  2  │ │  5  │ │  6  │
└─────┘ └─────┘ └─────┘
Modifier: +1
Total: 13 +1 = 14
```

## 📁 Project Structure

```
dice-roller/
├── dice_roller.py
├── tests/
│   └── test_dice_roller.py
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        ├── publish.yml
        └── test.yml
```

## ✅ To Do

- [x] Add support for flexible dice types
- [x] Uniform visual display for all rolls
- [x] CLI interface with argparse
- [x] PyPI publishing automation
- [x] Automated testing with GitHub Actions
- [ ] Add extended CLI flags (e.g. verbose, JSON output)
- [ ] Internationalization/localization support

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue to discuss what you'd like to change.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
