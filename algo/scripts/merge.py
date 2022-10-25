def merge(first: list[int | float], second: list[int | float], reverse: bool = False) -> list[int | float]:
    """Merge the pair of lists in ascending order and return them.

    Args:
        first: first list.
        second: second list.
        reverse: if true merge in descending order.
    """
    merged: list = []
    f_count: int = 0
    s_count: int = 0
    i: int = 0

    while i < len(first) + len(second):
        if not (reverse is (first[f_count] < second[s_count])):
            merged.append(first[f_count])
            f_count += 1
        elif not (reverse is (first[f_count] > second[s_count])):
            merged.append(second[s_count])
            s_count += 1
        else:
            merged.append(second[s_count])
            merged.append(first[f_count])
            f_count += 1
            s_count += 1
        if f_count == len(first):
            for elem in second[s_count:]:
                merged.append(elem)
                s_count += 1
            break
        if s_count == len(second):
            for elem in first[f_count:]:
                merged.append(elem)
                f_count += 1
            break
        i = f_count + s_count
    return merged
