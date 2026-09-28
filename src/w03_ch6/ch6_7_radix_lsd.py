import pyvisalgo as va


DATA_FILE = "data/radix_lsd.json"

vis = va.visualizer("radix_lsd")


def radix_sort_lsd(values):
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", radix_sort_lsd(array))
    vis.finish()
    vis.wait()
