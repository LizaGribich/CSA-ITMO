import pytest
from python import increment_numbers


def test_increment_numbers():
    input_data = [1, 2, 3]
    expected_output = [2, 3, 4]
    result = increment_numbers(input_data)
    assert result == expected_output, "The increment function should correctly increment each element by 1"