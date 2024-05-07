from python.main import increment_numbers


def test_increment_numbers():
    input_data = [3, 2, 3]
    expected_output = [5, 4, 5]
    result = increment_numbers(input_data)
    assert result == expected_output, "The increment function should correctly increment each element by 2"
