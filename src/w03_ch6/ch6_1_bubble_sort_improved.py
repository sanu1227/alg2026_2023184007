import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("bubble_sort")


def bubble_sort_improved(values):
    # 마지막 교환 뒤쪽은 다음 반복에서 제외한다.
    stop = len(values)
    pass_number = 0
    while stop > 1:
        next_stop = 0
        vis.start_pass(pass_number, stop)
        for index in range(stop - 1):
            vis.compare(index, index + 1)
            if values[index] > values[index + 1]:
                vis.swap(index, index + 1)
                values[index], values[index + 1] = values[index + 1], values[index]
                next_stop = index + 1
        vis.mark_sorted(next_stop)
        stop = next_stop
        pass_number += 1
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", bubble_sort_improved(array))
    vis.finish()
    vis.wait()
