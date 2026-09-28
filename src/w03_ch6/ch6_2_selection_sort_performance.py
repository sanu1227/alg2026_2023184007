import perf
def selection_sort(values):
    # 남은 구간에서 최소값의 위치를 찾은 뒤 한 번 이동한다.
    for position in range(len(values)):
        smallest = position
        for scan in range(position + 1, len(values)):
            if values[scan] < values[smallest]:
                smallest = scan
        values[position], values[smallest] = values[smallest], values[position]
    return values


if __name__ == "__main__":
    perf.test(selection_sort, 50000, data_func=perf.nearly_sorted_values)
