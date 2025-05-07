from setuptools import setup

setup(
    name="dice-roller",
    version="1.1",
    py_modules=["dice_roller"],
    entry_points={{
        "console_scripts": [
            "dice-roller=dice_roller:main",
        ],
    }},
    author="mattyhakin",
    description="A flexible dice rolling tool for tabletop games and simulations.",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
    python_requires=">=3.6",
)
