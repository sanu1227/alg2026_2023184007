import pyvisalgo as va


DATA_FILE = "data/count_sort.json"

vis = va.visualizer("count_sort")


def count_sort(values):
    if not values:
        return values
    counts = [0] * (max(values) + 1)
    vis.init_counts(counts)
    for index, value in enumerate(values):
        counts[value] += 1
        vis.count_value(index, value, counts)
    vis.finish_counting()
    vis.start_accumulate()
    for bucket in range(1, min(2, len(counts))):
        counts[bucket] += counts[bucket - 1]
        vis.accumulate(bucket - 1, bucket, counts)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", count_sort(array))
    vis.wait()
