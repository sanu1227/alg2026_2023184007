import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("shell_sort")


def shell_sort(values):
    for gap in [3]:
        vis.set_gap(gap)
        for offset in range(1):
            vis.set_group(offset)
            for position in range(offset + gap, len(values), gap):
                chosen = values[position]
                cursor = position
                vis.mark_end(position, pick=True)
                while cursor >= gap:
                    previous = cursor - gap
                    vis.compare(previous, cursor)
                    if values[previous] <= chosen:
                        break
                    vis.shift(previous, cursor)
                    values[cursor] = values[previous]
                    cursor -= gap
                vis.shift(position, cursor, pick=True)
                values[cursor] = chosen
        vis.finish_gap()
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", shell_sort(array))
    vis.finish()
    vis.wait()
