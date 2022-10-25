def __dim_selection(arr: list, size: int) -> tuple[list, int, bool]:
    result, to_matrix = None, None
    if isinstance(arr, list) and isinstance(arr[0], list):
        result = [0 for _ in range(size * size)]
        to_matrix = False
    elif isinstance(arr, list) and isinstance(arr[0], int | float):
        size = int(size ** .5)
        result = [[0 for _ in range(size)] for _ in range(size)]
        to_matrix = True
    return result, size, to_matrix


def spiral(list_obj: list | list[list]) -> list[list] | list:
    """Convert 2 dimensional matrix to array or array to 2 dimensional matrix by spiral transformation.

    Args:
        list_obj: 2 dimensional matrix or 1 dimensional array.
    """
    result, size, to_matrix = __dim_selection(list_obj, len(list_obj))

    k, j = 0, 0

    for i in range(size * size):
        if to_matrix:
            result[k][j] = list_obj[i]
        else:
            result[i] = list_obj[k][j]

        if k < j and k + j >= size - 1:
            k += 1
        elif k <= j + 1 and k + j < size - 1:
            j += 1
        elif k >= j and k + j > size - 1:
            j -= 1
        else:
            k -= 1
    return result


def snake(list_obj: list | list[list]) -> list[list] | list:
    """Convert 2 dimensional matrix to array or array to  2 dimensional  matrix by snake transformation.

    Args:
        list_obj: 2 dimensional matrix or 1 dimensional array.
    """
    result, size, to_matrix = __dim_selection(list_obj, len(list_obj))

    k, j = 0, 0
    to_left = direct = False

    for i in range(size * size):
        if to_matrix:
            result[k][j] = list_obj[i]
        else:
            result[i] = list_obj[k][j]

        if to_left:
            k += 1
            j -= 1
            if k >= size:
                k -= 1
                j += 2
                direct = True
            else:
                if j < 0:
                    j += 1
                    direct = True
        if not to_left:
            k -= 1
            j += 1
            if j >= size:
                j -= 1
                k += 2
                direct = True
            else:
                if k < 0:
                    k += 1
                    direct = True
        if direct:
            to_left = not to_left
        direct = False
    return result
