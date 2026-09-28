import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("insertion_sort")


def insertion_sort(values):
    if len(values) > 1:
        vis.mark_end(1)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", insertion_sort(array))
    vis.finish()
    vis.wait()
