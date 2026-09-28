import sys
from time import perf_counter

from sort_data import nearly_sorted_values, random_values


PERFORMANCE_COUNTS = [100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]


def test(sort_func, max_count=50000, data_func=None):
    if data_func is None:
        data_func = nearly_sorted_values if "--nearly" in sys.argv else random_values
    for count in PERFORMANCE_COUNTS:
        if count > max_count:
            break
        values = data_func(count)
        expected = sorted(values)
        started = perf_counter()
        result = sort_func(values)
        elapsed = perf_counter() - started
        assert (values if result is None else result) == expected
        print(f"{sort_func.__name__}: n={count}, 정렬={elapsed:.6f}초, 검증 통과")
