from logic_utils import check_guess, parse_guess, get_range_for_difficulty


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go Lower!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go Higher!"


def test_parse_guess_empty():
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_parse_guess_not_number():
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_parse_guess_valid_number():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 50)