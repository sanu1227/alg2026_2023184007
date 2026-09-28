import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("selection_sort")


def selection_sort(values):
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", selection_sort(array))
    vis.finish()
    vis.wait()
