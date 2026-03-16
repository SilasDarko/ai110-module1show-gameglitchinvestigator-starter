# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

This project started as an AI-generated number guessing game built with Streamlit. However, the original version of the game contained several bugs that made the gameplay inconsistent and confusing.

Some of the problems included:

- Incorrect hint logic that sometimes gave the wrong direction.
- The New Game button not properly resetting the game state.
- Difficulty ranges not always matching the actual game behavior.
- Game logic mixed directly inside the UI code, making it harder to test and debug.

The goal of this assignment was to investigate these problems, fix the broken logic, refactor the code into a cleaner structure, and verify the fixes using automated tests.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`

2. Run the application: `python -m streamlit run app.py`

3. Open the Streamlit link shown in the terminal (usually `http://localhost:8501`).

## 🕵️‍♂️ Your Mission

### 1. Play the game

The player attempts to guess a secret number within a limited number of attempts. The game provides hints indicating whether the guess is too high or too low.

Use the **Developer Debug Info** section to view internal game values during debugging.

### 2. Find the bugs

While testing the starter code, several issues were discovered:

- The hint logic sometimes told the player the wrong direction.
- The New Game button did not fully reset the game state.
- The displayed guessing range did not always match the selected difficulty.
- Game logic was tightly coupled with the Streamlit UI.

### 3. Fix the logic

The `check_guess()` function was corrected so that:

- If the guess is greater than the secret → the game says **Go Lower**
- If the guess is less than the secret → the game says **Go Higher**

### 4. Refactor and test

To make the code easier to maintain and test:

- Core game logic was moved into `logic_utils.py`
- `app.py` now focuses primarily on the Streamlit interface
- `pytest` was used to verify the logic functions

Tests were added for:

- winning guesses
- guesses that are too high
- guesses that are too low
- input parsing
- difficulty ranges

Run tests with: `pytest`

## 📝 Document Your Experience

This project involved debugging AI-generated code and improving its structure.

### Bugs Identified

The main issues discovered in the original code were:

1. **Reversed Hint Logic**  
   The hint messages did not always match the comparison between the guess and the secret number.

2. **Incomplete Game Reset**  
   The New Game button did not reset important session state variables such as attempts, score, status, and guess history.

3. **Mixed UI and Logic Code**  
   Game logic was originally written inside `app.py`, which made the code harder to test and debug.

### Fixes Applied

To fix these problems:

- Corrected the comparison logic in `check_guess()`
- Created a `reset_game()` function to properly reset session state
- Refactored logic functions into `logic_utils.py`
- Verified logic using `pytest`
- Tested gameplay manually in the Streamlit interface

### Working With AI

AI tools were used as a debugging assistant to help identify potential issues and suggest improvements. However, every suggestion was reviewed carefully and verified through testing before being applied.

The debugging process involved:

- examining the code
- testing the game behavior
- verifying results using the debug panel
- confirming functionality with automated tests

This approach ensured that the final fixes were reliable and that the AI suggestions were used effectively.

## 📸 Demo

Insert a screenshot of the fixed game running successfully.

Example screenshot should show:

- the Streamlit interface
- a correct hint or winning guess
- the debug panel or gameplay elements

## 🚀 Stretch Features

If any optional enhancements or additional tests were implemented, include screenshots or notes here.

Examples could include:

- improved UI elements
- additional edge-case tests
- expanded game features
