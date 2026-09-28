import pyvisalgo as va


DATA_FILE = "data/radix_lsd.json"

vis = va.visualizer("radix_lsd")


def digit_at(number, divisor):
    return number // divisor % 10


def counting_sort_by_digit(values, divisor):
    counts = [0] * 10
    vis.init_counts(counts)
    for index, number in enumerate(values):
        digit = digit_at(number, divisor)
        counts[digit] += 1
        vis.count_digit(index, number, digit, counts)
    vis.finish_counting()

    vis.start_accumulate()
    for digit in range(1, 10):
        counts[digit] += counts[digit - 1]
        vis.accumulate(digit - 1, digit, counts)
    vis.finish_accumulate(counts)

    result = [None] * len(values)
    vis.init_result(result)
    for index in range(len(values) - 1, -1, -1):
        number = values[index]
        digit = digit_at(number, divisor)
        counts[digit] -= 1
        target = counts[digit]
        result[target] = number
        vis.place_digit(index, number, digit, target, counts, result)
    vis.finish_result(result)
    vis.result_to_array(result)
    values[:] = result


def radix_sort_lsd(values):
    if not values:
        return values
    digit_count = len(str(max(values)))
    divisor = 1
    for pass_number in range(1):
        vis.start_digit(pass_number + 1, digit_count, divisor)
        counting_sort_by_digit(values, divisor)
        divisor *= 10
    return values


while va.running():
    data = va.next_data(__file__, data_file=DATA_FILE)
    array = list(data.array)

    vis.setup(data)
    print("정렬 전:", array)
    print("정렬 후:", radix_sort_lsd(array))
    vis.finish()
    vis.wait()
