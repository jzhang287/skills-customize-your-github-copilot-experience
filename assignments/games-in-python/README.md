
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game in Python to practice string manipulation, control flow, and user input handling.

## 📝 Tasks

### 🛠️ Task 1 — Core game (required)

#### Description
Implement the Hangman game loop that selects a secret word, accepts single-letter guesses from the player, and shows progress until the player wins or runs out of attempts.

#### Requirements
- Randomly select a word from a predefined list (in-memory or from a file).
- Accept single-letter input (case-insensitive) and ignore repeated guesses.
- Show current progress with unrevealed letters as underscores (e.g. A _ _ L E).
- Track incorrect guesses and limit attempts (suggested: 6).
- End the game with a clear win or lose message and reveal the correct word.
- Organize code into functions (e.g., `choose_word()`, `display_progress()`, `process_guess()`).

### 🛠️ Task 2 — Enhancements (optional)

#### Description
Add one or more improvements to make the game more polished or feature-rich.

#### Examples / Requirements
- Load words from an external file and handle larger lists.
- Add a hint system (reveal a letter) with a penalty.
- Draw ASCII-art hangman stages as attempts decrease.
- Keep a simple high-score table or save player stats.

## 🚀 Getting started

1. Open the starter code: `assignments/games-in-python/starter-code.py`.
2. Run the game locally:

```bash
python assignments/games-in-python/starter-code.py
```

3. Follow the task requirements above and add comments where you implement each feature.

## 📚 Resources

- Python `random` module for selecting words.
- Use `str` methods and list comprehensions for display and processing.

---

If you'd like, I can also update the `starter-code.py` to include skeleton functions matching the requirements. 
