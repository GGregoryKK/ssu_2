def insertion_sort(arr: list[int | float], reverse: bool = False) -> list[int | float]:
    """Sort the list in ascending order and return them.

    Args:
        arr: list.
        reverse: if true sort the arr in descending order.
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and reverse is (arr[i] < key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def bubble_sort(arr: list[int | float], reverse: bool = False) -> list[int | float]:
    """Sort the list in ascending order and return them.

    Args:
        arr: list.
        reverse: if true sort the arr in descending order.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if reverse is (arr[j] > arr[j - 1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def quick_sort(arr: list[int | float], reverse: bool = False) -> list[int | float]:
    """Sort the list in ascending order and return them.

    Args:
        arr: list.
        reverse: if true sort the arr in descending order.
    """
    if len(arr) < 2:
        return arr
    left, right = [], []
    ind = (len(arr) - 1)
    ind_val = arr[ind]
    arr = arr[:ind]
    for i in range(len(arr)):
        if reverse is (arr[i] > ind_val):
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = quick_sort(left, reverse=reverse)
    right = quick_sort(right, reverse=reverse)
    return left + [ind_val] + right
