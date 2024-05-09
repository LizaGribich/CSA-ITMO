from python.main import increment_numbers
from typing import Any
import pytest


@pytest.mark.golden_test("goldens/*.yml")
def test_increment_numbers(golden: Any) -> None:
    input_data = golden["in_data"]
    expected_output = golden["out_data"]

    result = increment_numbers(input_data)

    assert result == expected_output, "не работает как ожидается"
