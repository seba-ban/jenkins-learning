import pytest
from utils.strings import StringAdder

@pytest.mark.parametrize(
        ["x", "y", "expected"],
        [
            ("1", "2", 3),
            ("1", 2, 3),
            (1, "2", 3),
            (1, 2, 3),
        ]
)
def test_string_adder(x, y, expected):
    assert StringAdder().add(x, y) == expected
