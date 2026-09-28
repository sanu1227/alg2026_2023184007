import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("bubble_sort")


def bubble_sort(values):
    # 한 번의 순회마다 최댓값 하나가 오른쪽에 확정된다.
    length = len(values)
    for stop in range(length - 1, 0, -1):
        vis.start_pass(length - 1 - stop, stop + 1)
        for index in range(stop):
            vis.compare(index, index + 1)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", bubble_sort(array))
    vis.finish()
    vis.wait()
