def arg_sort(a: list, reverse=False) -> list[int]:
    """Takes a list and retuns a list contains argmunt sort

    :param a: list that need to be sorted
    :type a: list
    :param reverse: if True the result will be in descending order, defaults to False
    :type reverse: bool, optional
    :return: a list of sorted arguments
    :rtype: list[int]
    """
    return sorted(range(len(a)), key=a.__getitem__, reverse=reverse)
