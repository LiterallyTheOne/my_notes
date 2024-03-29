from ..src.evaluations import mae,mse


def test_mae_1():
    y = [1, 2, 3, 4]
    p = [2, 4, 3, 4]

    assert mae(y, p) == 3 / 4


def test_mse_1():
    y = [1, 2, 3, 4]
    p = [2, 4, 3, 4]

    assert mse(y, p) == 5 / 4
