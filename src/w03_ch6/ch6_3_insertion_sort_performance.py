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
