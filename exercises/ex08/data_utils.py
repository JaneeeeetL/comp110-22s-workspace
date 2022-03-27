"""Dictionary related utility functions."""

__author__ = "730401522"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # TODO: More work!

    # Open a handle to the data file

    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings

    csv_reader = DictReader(file_handle)

    # Read each row of the CSV file line-by-line.
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a singel column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Purpose: Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    if num_rows > len(column_table):
        num_rows = len(column_table)
        for key in column_table:
            ns: list[str] = []
            n: int = 0
            while n < num_rows:
                ns.append(column_table[key][n])
                n += 1
            result[key] = ns
    else:
        for key in column_table:
            nums: list[str] = []
            num: int = 0
            while num < num_rows:
                nums.append(column_table[key][num])
                num += 1
            result[key] = nums
    return result


def select(column_table: dict[str, list[str]], selected: list[str]) -> dict[str, list[str]]:
    """Purpose: Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in selected:
        result[item] = column_table[item]
    return result


def concat(dict_1: dict[str, int], dict_2: dict[str, int]) -> dict[str, int]:
    """Purpose: Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, int] = {}
    for item in dict_1:
        result[item] = dict_1[item]
    for item in dict_2:
        if item in result:
            result[item] += dict_2[item]
        else: 
            result[item] = dict_2[item]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in a:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result