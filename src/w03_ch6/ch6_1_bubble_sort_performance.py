import perf
def bubble_sort_improved(values):
    # 마지막 교환 뒤쪽은 다음 반복에서 제외한다.
    stop = len(values)
    pass_number = 0
    while stop > 1:
        next_stop = 0
        for index in range(stop - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                next_stop = index + 1
        stop = next_stop
        pass_number += 1
    return values
