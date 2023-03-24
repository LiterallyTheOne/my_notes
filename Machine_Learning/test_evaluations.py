from evaluations import mae


def test_mae_1():
    y = [1, 2, 3, 4]
    p = [2, 4, 3, 4]

    assert mae(y, p) == 3 / 4
