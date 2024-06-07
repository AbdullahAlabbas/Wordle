
# Wordle Game Implementation

## Overview

This repository contains a Python implementation of a Wordle game. The game allows players to guess a secret word within a limited number of attempts. Each guess provides feedback on the correctness of the letters and their positions.

## Files

### 1. `letter_state.py`

This file contains the `LetterState` class, which is used to track the state of each letter in a guess.

```python
class LetterState:
    def __init__(self, character: str):
        self.character: str = character
        self.is_in_word: bool = False
        self.is_in_position: bool = False

    def __repr__(self):
        return f"[{self.character} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}]"
```

### 2. `wordle.py`

This file contains the `Wordle` class, which manages the game logic, including handling guesses and tracking attempts.

```python
from letter_state import LetterState

class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()
        result = []
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)

        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
```

### 3. `main.py`

This file contains the main function and additional helper functions to run the game. It handles user interaction, loads the word set, and displays the game results.

```python
from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random

def main():
    word_set = load_word_set("data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input("\nType your guess: ").upper()

        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} characters long!"
                + Fore.RESET
            )
            continue

        if not x in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word!"
                + Fore.RESET
            )
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The secret word was: {wordle.secret}")

def display_results(wordle: Wordle):
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)

def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)

if __name__ == "__main__":
    main()
```

## How to Run

1. Ensure you have Python installed (Python 3.6+ recommended).
2. Install required dependencies using `pip`:
   ```bash
   pip install colorama
   ```
3. Prepare your word list file at `data/wordle_words.txt`.
4. Run the game:
   ```bash
   python main.py
   ```

## Game Instructions

1. The game selects a secret word at random from the provided word list.
2. You have 6 attempts to guess the secret word.
3. After each guess, you will receive feedback:
   - Letters in the correct position will be highlighted in green.
   - Letters that are in the word but in the wrong position will be highlighted in yellow.
   - Incorrect letters will be displayed in white.
4. Keep guessing until you solve the word or run out of attempts.

Enjoy the game!
