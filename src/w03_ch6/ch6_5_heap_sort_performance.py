import perf
def heapify(values, root, size):
    left_child = root * 2 + 1
    if left_child >= size:
        return
    larger = left_child
    right_child = left_child + 1
    if right_child < size:
        if values[right_child] > values[left_child]:
            larger = right_child
    if values[root] < values[larger]:
        values[root], values[larger] = values[larger], values[root]
        heapify(values, larger, size)


def heap_sort(values):
    size = len(values)
    for root in range(size // 2 - 1, -1, -1):
        heapify(values, root, size)
    for last in range(size - 1, 0, -1):
        values[0], values[last] = values[last], values[0]
        heapify(values, 0, last)
    return values


if __name__ == "__main__":
    perf.test(heap_sort, 1000000)
