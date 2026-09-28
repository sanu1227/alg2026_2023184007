import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("bubble_sort_vertical")


def bubble_sort(values):
    # 한 번의 순회마다 최댓값 하나가 오른쪽에 확정된다.
    length = len(values)
    for stop in range(length - 1, 0, -1):
        vis.start_pass(length - 1 - stop, stop + 1)
        for index in range(stop):
            vis.compare(index, index + 1)
            if values[index] > values[index + 1]:
                vis.swap(index, index + 1)
                values[index], values[index + 1] = values[index + 1], values[index]
        vis.mark_sorted(stop)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    vertical_array = list(data.array)

    vis.setup(data)
    print("정렬 전:", vertical_array)
    print("정렬 후:", bubble_sort(vertical_array))
    vis.finish()
    vis.wait()
