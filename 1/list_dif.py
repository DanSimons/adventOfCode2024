import numpy as np


def load_in(filename: str) -> list[list[int]]:
    arr = np.loadtxt(filename, dtype=int)

    return [arr[:, 0].tolist(), arr[:, 1].tolist()]


def list_dif(left: list[int], right: list[int]) -> int:

    left.sort()
    right.sort()

    total_dif = 0

    while left:
        total_dif += abs(left.pop(0) - right.pop(0))

    return total_dif


def similarity(left: list[int], right: list[int]) -> int:

    score = 0
    for i in left:
        score += i * right.count(i)

    return score


if __name__ == "__main__":
    input = load_in('in1.txt')
    left = input[0]
    right = input[1]
    print(similarity(left, right))
