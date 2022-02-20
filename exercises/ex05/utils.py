"""Program for ex05."""
__author__: str = "730401522"


def only_evens(xs: list[int]) -> list[int]:
    """A list of integers, containing only the even elements of the input parameter."""
    i: int = 0
    list_even: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            list_even.append(xs[i])
        i += 1
    return list_even


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """A List which is a subset of the given list, between the specified start index and the end index - 1."""
    sub_list: list[int] = []
    if len(a_list) == 0 or start_index > len(a_list) or end_index <= 0:
        emp_list: list[int] = []
        return emp_list
    if start_index < 0:
        start_index = 0
    if end_index > len(a_list):
        end_index = len(a_list)
    i: int = start_index
    while i < end_index:
        sub_list.append(a_list[i])
        i += 1
    return sub_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """A list containing all elements of the first list, followed by all elements of the second list."""
    new_list: list[int] = []
    for num in list_one:
        new_list.append(num)
    for num in list_two:
        new_list.append(num)
    return new_list