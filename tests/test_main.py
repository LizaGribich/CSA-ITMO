from python.main import increment_numbers

import pytest


@pytest.mark.golden_test("goldens/*.yml")
def test_increment_numbers(golden):
    input_data = golden["in_data"]
    expected_output = golden["out_data"]

    result = increment_numbers(input_data)

    assert result == expected_output, "increment_numbers не работает как ожидается"
