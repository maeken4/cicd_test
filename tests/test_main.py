from main import is_even


def test_is_even() -> None:
    assert is_even(2)
    assert not is_even(3)
