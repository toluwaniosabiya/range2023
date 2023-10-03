from src.range_function import check_range
import pytest

def test_point():
    assert check_range([[13, 0], [0, 4.5]]) == [0, 0]