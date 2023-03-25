from ..src.some_functions import *


def test_arg_sort_with_integers():
    a = [30, 20, 11, 15, 12]
    input_a = a.copy()
    expected_result = [2, 4, 3, 1, 0]

    result = arg_sort(input_a)

    # check to make sure a is not changed
    assert a == input_a

    # check the result
    assert result == expected_result


def test_arg_sort_reverse():
    a = [30, 20, 11, 15, 12]
    input_a = a.copy()
    expected_result = [0, 1, 3, 4, 2]

    result = arg_sort(input_a, reverse=True)

    # check to make sure a is not changed
    assert a == input_a

    # check the result
    assert result == expected_result


def test_arg_sort_chars():
    a = list("ramin")
    input_a = a.copy()
    expected_result = [1, 3, 2, 4, 0]

    result = arg_sort(input_a)

    # check to make sure a is not changed
    assert a == input_a

    # check the result
    assert result == expected_result
