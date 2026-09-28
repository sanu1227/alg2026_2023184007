import json
from pathlib import Path


FIRST_CHAR = "e"
LAST_CHAR = "o"
BUCKET_COUNT = ord(LAST_CHAR) - ord(FIRST_CHAR) + 2

DATA_FILE = Path(__file__).parent / "data/radix_msd_e_to_o_words.json"

def bucket_at(word, depth):
    if depth >= len(word):
        return 0
    return ord(word[depth]) - ord(FIRST_CHAR) + 1


def radix_sort_msd_range(values, left, right, depth, result):
    counts = [0] * BUCKET_COUNT
    for index in range(left, right + 1):
        bucket = bucket_at(values[index], depth)
        counts[bucket] += 1

    for bucket in range(1, BUCKET_COUNT):
        counts[bucket] += counts[bucket - 1]
    ends = list(counts)

    for index in range(left, right + 1):
        result[index] = None
    for index in range(right, left - 1, -1):
        bucket = bucket_at(values[index], depth)
        counts[bucket] -= 1
        target = left + counts[bucket]
        result[target] = values[index]
    values[left:right + 1] = result[left:right + 1]
    for index in range(left, right + 1):
        result[index] = None

    # 종료 bucket은 재귀 호출하지 않는다.
    for bucket in range(1, BUCKET_COUNT):
        start = left + ends[bucket - 1]
        stop = left + ends[bucket] - 1
        if start < stop:
            radix_sort_msd_range(values, start, stop, depth + 1, result)
    return ends


def radix_sort_msd(values):
    result = [None] * len(values)
    ends = radix_sort_msd_range(values, 0, len(values) - 1, 0, result)
    return values


def validate_words(words):
    for word in words:
        for character in word:
            if not FIRST_CHAR <= character <= LAST_CHAR:
                raise ValueError(f"범위 밖 문자: {character!r}, 단어: {word!r}")


if __name__ == "__main__":
    datasets = json.loads(DATA_FILE.read_text(encoding="utf-8"))["datasets"]
    words = list(datasets[0]["data"]["array"])
    validate_words(words)
    expected = sorted(words)
    print("정렬 전:", words)
    radix_sort_msd(words)
    print("정렬 후:", words)
    assert words == expected, "MSD 정렬 결과가 올바르지 않습니다."
    print("입력 범위와 사전순 정렬 검증 통과")
