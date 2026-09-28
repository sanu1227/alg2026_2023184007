from math import ceil

import perf
HIBBARD = [2 ** power - 1 for power in range(20, 0, -1)]
CIURA = [701, 301, 132, 57, 23, 10, 4, 1]
TOKUDA = [ceil((9 * (9 / 4) ** power - 4) / 5) for power in range(17, -1, -1)]
GAPS = HIBBARD


def gaps(count):
    for index, gap in enumerate(GAPS):
        if gap < count // 2:
            return GAPS[index:]
    return [1]


def shell_sort(values, gap_sequence=TOKUDA):
    for gap in gap_sequence:
        if gap >= len(values):
            continue
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


if __name__ == "__main__":
    perf.test(shell_sort, 1000000, data_func=perf.nearly_sorted_values)


# 실습 관찰: gap 수열이 바뀌면 멀리 떨어진 원소의 비교와 이동 순서도 바뀐다.
# 표본 측정: shell_sort: n=100, 정렬=0.000022초, 검증 통과
