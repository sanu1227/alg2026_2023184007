import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("insertion_sort")


def insertion_sort(values):
    for position in range(1, len(values)):
        cursor = position
        # 후보를 보관하고 큰 값만 오른쪽으로 민다.
        chosen = values[position]
        vis.mark_end(position, pick=True)
        while cursor > 0:
            previous = cursor - 1
            vis.compare(previous, cursor)
            if values[previous] <= chosen:
                break
            vis.shift(previous, cursor)
            values[cursor] = values[previous]
            cursor -= 1
        vis.shift(position, cursor, pick=True)
        values[cursor] = chosen
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", insertion_sort(array))
    vis.finish()
    vis.wait()
