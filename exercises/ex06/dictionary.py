"""Exercise 06 -- dictinary utilities."""
__author__: str = "730401522"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    result: dict[str, str]
    result = dict()
    
    for key in a:
        result[a[key]] = key
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Gives the color liked by most people in the dictionary."""
    result: dict[str, int]
    result = dict()
    for key in b:
        if key in result:
            result[b[key]] += 1
        else:
            result[b[key]] = 1
    max_value: int = 0
    max_key: str = ""
    for key in result:
        if result[key] > max_value:
            max_value = result[key]
            max_key = key
    return max_key


def count(c: list[str]) -> dict[str, int]:
    """Count the times that a key appears in a list."""
    new_dict: dict[str, int]
    new_dict = {}
    for item in c:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict