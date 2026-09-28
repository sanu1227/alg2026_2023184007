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


if __name__ == "__main__":
    perf.test(bubble_sort_improved, 50000, data_func=perf.nearly_sorted_values)


# 실습 관찰: 마지막 교환 뒤쪽을 제외해 정렬된 입력의 비교를 줄인다.
# 표본 측정: bubble_sort_improved: n=100, 정렬=0.000059초, 검증 통과
