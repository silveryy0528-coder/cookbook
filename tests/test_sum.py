from src.sum import sum
import pytest


def test_typical():
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0
    assert sum(1.5, 2.5) == 4.0
