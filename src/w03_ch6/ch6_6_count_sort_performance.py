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


if __name__ == "__main__":
    perf.test(count_sort, 1000000)
