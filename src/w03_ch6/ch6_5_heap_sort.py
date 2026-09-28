import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("heap_sort")


def heapify(values, root, size):
    left_child = root * 2 + 1
    if left_child >= size:
        return
    larger = left_child
    right_child = left_child + 1
    if right_child < size:
        vis.compare(left_child, right_child)
        if values[right_child] > values[left_child]:
            larger = right_child
    vis.compare(root, larger)
    if values[root] < values[larger]:
        vis.swap(root, larger)
        values[root], values[larger] = values[larger], values[root]
        heapify(values, larger, size)


def heap_sort(values):
    vis.build_tree()
    size = len(values)
    if size > 1:
        root = 0
        vis.set_root(root)
        heapify(values, root, size)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", heap_sort(array))
    vis.finish()
    vis.wait()
