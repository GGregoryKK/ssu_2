import random

from ssu_2.algo.scripts.merge import merge
from ssu_2.algo.scripts.conversion import snake, spiral
from ssu_2.algo.scripts.sort import bubble_sort, quick_sort, insertion_sort


def test_merge() -> None:
    a, b = [1, 2, 3], [4, 5, 6]
    assert merge(a, b) == [1, 2, 3, 4, 5, 6]

    a, b = [0, 3, 5], [1, 2, 4]
    assert merge(a, b) == [0, 1, 2, 3, 4, 5]

    a, b = [1], [0, 2]
    assert merge(a, b) == [0, 1, 2]

    a, b = [0, 2], [1]
    assert merge(a, b) == [0, 1, 2]

    a, b = [0, 1], [0, 1]
    assert merge(a, b) == [0, 0, 1, 1]

    a, b = [0, 1], [0, 1, 2]
    assert merge(a, b) == [0, 0, 1, 1, 2]

    a, b = [3, 2, 1], [6, 5, 4]
    assert merge(a, b, reverse=True) == [6, 5, 4, 3, 2, 1]

    a, b = [5, 3, 0], [4, 2, 1]
    assert merge(a, b, reverse=True) == [5, 4, 3, 2, 1, 0]

    a, b = [1], [2, 0]
    assert merge(a, b, reverse=True) == [2, 1, 0]

    a, b = [2, 0], [1]
    assert merge(a, b, reverse=True) == [2, 1, 0]

    a, b = [1, 0], [1, 0]
    assert merge(a, b, reverse=True) == [1, 1, 0, 0]

    a, b = [1, 0], [2, 1, 0]
    assert merge(a, b, reverse=True) == [2, 1, 1, 0, 0]


def test_sort() -> None:
    n = 5
    gen_set = 100
    arr = [random.randint(-gen_set, gen_set) for _ in range(n)]
    expected = sorted(arr)
    expected_reverse = sorted(arr, reverse=True)

    assert expected == bubble_sort(arr) == quick_sort(arr) == insertion_sort(arr)
    assert expected_reverse == bubble_sort(arr, reverse=True) == quick_sort(arr, reverse=True) == \
           insertion_sort(arr, reverse=True)


def test_conversion() -> None:
    vector = [i for i in range(1, 10)]
    vector1 = [i for i in range(1, 17)]
    vector2 = [i for i in range(1, 26)]

    matrix = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]
    matrix1 = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    matrix2 = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]

    assert matrix == spiral(vector)
    assert spiral(matrix) == vector
    assert matrix1 == spiral(vector1)
    assert spiral(matrix1) == vector1
    assert matrix2 == spiral(vector2)
    assert spiral(matrix2) == vector2

    matrix = [
        [1, 2, 6],
        [3, 5, 7],
        [4, 8, 9],
    ]

    matrix1 = [
        [1, 2, 6, 7],
        [3, 5, 8, 13],
        [4, 9, 12, 14],
        [10, 11, 15, 16],
    ]

    matrix2 = [
        [1, 2, 6, 7, 15],
        [3, 5, 8, 14, 16],
        [4, 9, 13, 17, 22],
        [10, 12, 18, 21, 23],
        [11, 19, 20, 24, 25]
    ]

    assert matrix == snake(vector)
    assert snake(matrix) == vector
    assert matrix1 == snake(vector1)
    assert snake(matrix1) == vector1
    assert matrix2 == snake(vector2)
    assert snake(matrix2) == vector2


if __name__ == "__main__":
    test_merge()
    test_sort()
    test_conversion()
