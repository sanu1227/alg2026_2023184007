import pyvisalgo as va


DATA_FILE = "data/radix_msd_words.json"

vis = va.visualizer("radix_msd_words")


def bucket_at(word, depth):
    if depth >= len(word):
        return 0
    return ord(word[depth]) - ord("a") + 1


def radix_sort_msd_range(values, left, right, depth):
    vis.push(left, right, depth)
    counts = [0] * 27
    vis.init_counts(counts)
    for index in range(left, right + 1):
        bucket = bucket_at(values[index], depth)
        counts[bucket] += 1
        vis.scan(index, bucket, counts)
    vis.finish_counting()

    vis.start_accumulate()
    for bucket in range(1, 27):
        counts[bucket] += counts[bucket - 1]
        vis.accumulate_bucket(bucket - 1, bucket, counts)
    vis.finish_accumulate(counts)
    ends = list(counts)

    result = [None] * len(values)
    vis.init_result(result)
    for index in range(right, left - 1, -1):
        bucket = bucket_at(values[index], depth)
        counts[bucket] -= 1
        target = left + counts[bucket]
        result[target] = values[index]
        vis.place(index, bucket, target, counts, result)
    vis.finish_result(result)
    values[left:right + 1] = result[left:right + 1]
    vis.copy_back(result)

    # 종료 bucket은 재귀 호출하지 않는다.
    for bucket in range(1, 27):
        start = left + ends[bucket - 1]
        stop = left + ends[bucket] - 1
        if start < stop:
            radix_sort_msd_range(values, start, stop, depth + 1)
    vis.pop()
    return ends


def radix_sort_msd(values):
    vis.line_up()
    ends = radix_sort_msd_range(values, 0, len(values) - 1, 0)
    vis.finish()
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", radix_sort_msd(array))
    vis.wait()
