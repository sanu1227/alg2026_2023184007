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
