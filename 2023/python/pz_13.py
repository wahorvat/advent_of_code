import numpy as np


f = open('./input/input_13.txt')
data = f.read().split('\n\n')


def mirrorpos(arr, axis=0, diff=0):
    m = np.array(arr, dtype=int)
    if axis == 1:
        m = m.T
    for i in range(m.shape[0] - 1):
        upper_flipped = np.flip(m[: i + 1], axis=0)
        lower = m[i + 1 :]
        rows = min(upper_flipped.shape[0], lower.shape[0])
        if np.count_nonzero(upper_flipped[:rows] - lower[:rows]) == diff:
            return i + 1
    return 0


for i in range(2):
    total = 0
    for puzzle in data:
        arr = []
        for line in puzzle.splitlines():
            arr.append([*line.strip().replace(".", "0").replace("#", "1")])
        total += 100 * mirrorpos(arr, axis=0, diff=i) + mirrorpos(arr, axis=1, diff=i)
    print(total)

