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


def heapify_improved(values, root, size):
    chosen = values[root]
    while root * 2 + 1 < size:
        child = root * 2 + 1
        if child + 1 < size and values[child + 1] > values[child]:
            child += 1
        if chosen >= values[child]:
            break
        values[root] = values[child]
        root = child
    values[root] = chosen


def heap_sort_improved(values):
    size = len(values)
    for root in range(size // 2 - 1, -1, -1):
        heapify_improved(values, root, size)
    for last in range(size - 1, 0, -1):
        values[0], values[last] = values[last], values[0]
        heapify_improved(values, 0, last)
    return values



if __name__ == "__main__":
    perf.test(heap_sort, 1000000)
    perf.test(heap_sort_improved, 1000000)
