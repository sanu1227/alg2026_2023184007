import perf
def count_sort(values):
    if not values:
        return values
    counts = [0] * (max(values) + 1)
    for index, value in enumerate(values):
        counts[value] += 1
    for bucket in range(1, len(counts)):
        counts[bucket] += counts[bucket - 1]
    result = [None] * len(values)
    for index in range(len(values) - 1, -1, -1):
        value = values[index]
        counts[value] -= 1
        target = counts[value]
        result[target] = value
    values[:] = result
    return values


from sort_data import limited_random_values

COUNTS = [1000000, 10000000, 50000000]

if __name__ == "__main__":
    perf.test_generated(
        count_sort, COUNTS,
        lambda count: limited_random_values(count, max(1, count // 100)),
        lambda count: max(1, count // 100),
    )


# 실습 관찰: 배열 길이와 함께 값 범위만큼 counts 메모리가 필요하다. 실습은 100개 표본으로 확인했다.
# 표본 측정: count_sort: n=100, 값 종류=10000, 생성=0.000036초, 정렬=0.000430초, 검증 통과
