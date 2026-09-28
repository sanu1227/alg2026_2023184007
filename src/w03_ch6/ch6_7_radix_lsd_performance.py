import perf
def digit_at(number, divisor):
    return number // divisor % 10


def counting_sort_by_digit(values, divisor):
    counts = [0] * 10
    for index, number in enumerate(values):
        digit = digit_at(number, divisor)
        counts[digit] += 1

    for digit in range(1, 10):
        counts[digit] += counts[digit - 1]

    result = [None] * len(values)
    for index in range(len(values) - 1, -1, -1):
        number = values[index]
        digit = digit_at(number, divisor)
        counts[digit] -= 1
        target = counts[digit]
        result[target] = number
    values[:] = result


def radix_sort_lsd(values):
    if not values:
        return values
    digit_count = len(str(max(values)))
    divisor = 1
    for pass_number in range(digit_count):
        counting_sort_by_digit(values, divisor)
        divisor *= 10
    return values


if __name__ == "__main__":
    perf.test(radix_sort_lsd, 1000000)
