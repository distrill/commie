import numpy as np


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.replace("\n", "")for x in lines]
    lines = [list(x) for x in lines]
    lines = [list(map(int, i)) for i in lines]

    lines = np.pad(lines, 1, pad_with, padder=9)

    min_zone_sum = 0
    for j in range(1, len(lines[0])-1):
        for i in range(1, len(lines) - 1):
            zone = lines[i][j]
            if zone < lines[i + 1][j] and zone < lines[i-1][j]:
                if zone < lines[i][j-1] and zone < lines[i][j+1]:
                    min_zone_sum += 1 + zone
    print(min_zone_sum)
