import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("selection_sort")


def selection_sort(values):
    # 남은 구간에서 최소값의 위치를 찾은 뒤 한 번 이동한다.
    for position in range(min(1, len(values))):
        smallest = position
        vis.selection(smallest)
        for scan in range(position + 1, len(values)):
            vis.compare(smallest, scan)
            if values[scan] < values[smallest]:
                smallest = scan
                vis.selection(smallest)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", selection_sort(array))
    vis.finish()
    vis.wait()
