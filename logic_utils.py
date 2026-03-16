def get_range_for_difficulty(difficulty: str):
    """Return the inclusive range for the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse the user's guess into an integer.

    Returns:
        tuple: (ok, guess_int, error_message)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# FIX: Refactored from app.py and corrected reversed hint logic with AI assistance.
def check_guess(guess, secret):
    """
    Compare guess to secret and return a result tuple.

    Returns:
        tuple: (outcome, message)
    """
    try:
        guess = int(guess)
        secret = int(secret)
    except (ValueError, TypeError):
        return "Error", "Invalid input. Guess and secret must be numbers."

    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go Lower!"
    else:
        return "Too Low", "📈 Go Higher!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.
    """
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
