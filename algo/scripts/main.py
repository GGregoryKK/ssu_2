import pathlib
import random
from glob import glob
from pathlib import Path
from typing import Generator
from time import perf_counter

from sort import bubble_sort, quick_sort, insertion_sort


def gen(quantity: int, sets: int) -> Generator[int, None, None]:
    """Generate random values in range [-sets, sets].

    Args:
        quantity: sample size.
        sets: range of values.
    """
    for _ in range(quantity):
        yield random.randint(-sets, sets)


def gen_to_file(f_name: Path, quantity: int, sets: int) -> None:
    """Write random values in range [-sets, sets] to file.

    Args:
        f_name: file name.
        quantity: sample size.
        sets: range of values.
    """
    with open(f_name, "w") as file:
        try:
            for numb in gen(quantity=quantity, sets=sets):
                file.write(f"{numb}\n")
        finally:
            file.close()


def create_data(dir_name: Path, list_quantity: list, sets: int) -> None:
    """Create files with random values.

    Args:
        dir_name: directory name.
        list_quantity: list of sample size for each file.
        sets: range of values.
    """
    for quantity in list_quantity:
        gen_to_file(f_name=Path(f"{dir_name}/{quantity}.txt"), quantity=quantity, sets=sets)


def read_data(paths: list) -> Generator[list, None, None]:
    """Read the sample from files.

    Args:
        paths: list of paths to files.
    """
    for path in paths:
        with open(Path(path)) as file:
            try:
                data = []
                for line in file:
                    for x in line.split():
                        data.append(int(x))
            finally:
                file.close()
        yield data


def collect_data(functions: list, dir_name: Path, list_quantity: list) -> Generator[str, None, None]:
    """Returns string of some calculations as iterator.

    Args:
        functions: list of some func to apply to data.
        dir_name: directory name.
        list_quantity: list of sample size for each file.
    """
    paths = glob(f"{dir_name}/*.txt")

    for data, quantity in zip(read_data(paths), list_quantity):
        for func in functions:
            start_time = perf_counter()
            func(data.copy())
            yield f"Python,{func.__name__},{quantity},{perf_counter() - start_time}\n"


if __name__ == "__main__":
    list_quantity = [q for q in range(20_000, 120_000, 20_000)]
    _dir = pathlib.Path("../data/")
    res_dir = pathlib.Path("../results/res.csv")
    create_data(dir_name=_dir, list_quantity=list_quantity, sets=100_000)
    functions = [quick_sort, insertion_sort, bubble_sort, ]
    with open(res_dir, "w") as f:
        try:
            f.write("Lang,Sort,Quantity,Time\n")
            for res in collect_data(functions, _dir, list_quantity):
                print(res)
                f.write(res)
        finally:
            f.close()
