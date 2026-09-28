import pyvisalgo as va


DATA_FILE = "data/radix_msd_words.json"

vis = va.visualizer("radix_msd_words")


def bucket_at(word, depth):
    if depth >= len(word):
        return 0
    return ord(word[depth]) - ord("a") + 1


def radix_sort_msd(values):
    vis.line_up()
    left = 0
    right = len(values) - 1
    vis.push(left, right, 0)
    counts = [0] * 27
    vis.init_counts(counts)
    for index in range(left, right + 1):
        bucket = bucket_at(values[index], 0)
        counts[bucket] += 1
        vis.scan(index, bucket, counts)
    vis.finish_counting()
    vis.start_accumulate()
    for bucket in range(1, len(counts)):
        counts[bucket] += counts[bucket - 1]
        vis.accumulate_bucket(bucket - 1, bucket, counts)
    vis.finish_accumulate(counts)
    ends = list(counts)
    result = [None] * len(values)
    vis.init_result(result)
    for index in range(right, left - 1, -1):
        bucket = bucket_at(values[index], 0)
        counts[bucket] -= 1
        target = left + counts[bucket]
        result[target] = values[index]
        vis.place(index, bucket, target, counts, result)
    vis.finish_result(result)
    values[left:right + 1] = result[left:right + 1]
    vis.copy_back(result)
    e_start = ends[4]
    e_stop = ends[5] - 1
    if e_start < e_stop:
        left = e_start
        right = e_stop
        vis.push(left, right, 1)
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", radix_sort_msd(array))
    vis.wait()
