import perf
GAPS = [15, 7, 3, 1]


def gaps(count):
    for index, gap in enumerate(GAPS):
        if gap < count // 2:
            return GAPS[index:]
    return [1]


def shell_sort(values):
    for gap in gaps(len(values)):
        for position in range(gap, len(values)):
            chosen = values[position]
            cursor = position
            while cursor >= gap:
                previous = cursor - gap
                if values[previous] <= chosen:
                    break
                values[cursor] = values[previous]
                cursor -= gap
            values[cursor] = chosen
    return values
