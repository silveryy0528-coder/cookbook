from src.mul import mul


def test_typical():
    assert mul(1, 2) == 2
    assert mul(-1, 1) == -1
    assert mul(1, 0) == 0
    assert mul(1.5, 2.5) == 3.75

