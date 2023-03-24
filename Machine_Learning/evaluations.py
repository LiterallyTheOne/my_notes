def mae(y: list, predictions: list) -> float:
    """return mean absolute error

    :param y: ground truth labels
    :type y: list
    :param predictions: _description_
    :type predictions: list
    :return: _description_
    :rtype: float
    """

    return sum(
        [abs(y_i - prediction) for y_i, prediction in zip(y, predictions)]
    ) / len(y)
