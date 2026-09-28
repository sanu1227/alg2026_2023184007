import random


def random_values(count):
    return [random.randrange(count or 1) for _ in range(count)]


def nearly_sorted_values(count):
    values = list(range(count))
    for _ in range(count // 100):
        first = random.randrange(count)
        second = random.randrange(count)
        values[first], values[second] = values[second], values[first]
    return values
