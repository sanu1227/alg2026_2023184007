import perf
def insertion_sort(values):
    for position in range(1, len(values)):
        cursor = position
        # 후보를 보관하고 큰 값만 오른쪽으로 민다.
        chosen = values[position]
        while cursor > 0:
            previous = cursor - 1
            if values[previous] <= chosen:
                break
            values[cursor] = values[previous]
            cursor -= 1
        values[cursor] = chosen
    return values


if __name__ == "__main__":
    perf.test(insertion_sort, 50000, data_func=perf.nearly_sorted_values)


# 실습 관찰: 거의 정렬된 입력에서는 삽입할 위치가 가까워 이동이 줄어든다.
# 표본 측정: insertion_sort: n=100, 정렬=0.000011초, 검증 통과
