import numpy as np
from queue import Queue

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


class Basin():
    def __init__(self, min_value, min_value_coords, map):
        self.min_value = min_value
        self.points_within = []
        self.min_value_coords = min_value_coords
        self.map = map
        self.search()

    def search(self):
        q = Queue()
        q.put(self.min_value_coords)

        while not q.empty():
            node = q.get()
            if node in self.points_within:
                continue
            self.points_within.append(node)

            x, y = node[0], node[1]

            if self.map[x][y+1] != 9:
                q.put([x, y+1])
            if self.map[x][y-1] != 9:
                q.put([x, y-1])
            if self.map[x+1][y] != 9:
                q.put([x+1, y])
            if self.map[x-1][y] != 9:
                q.put([x-1, y])

    def get_size(self):
        return len(self.points_within)





if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.replace("\n", "")for x in lines]
    lines = [list(x) for x in lines]
    lines = [list(map(int, i)) for i in lines]

    lines = np.pad(lines, 1, pad_with, padder=9)

    basins = []
    for j in range(1, len(lines[0])-1):
        for i in range(1, len(lines) - 1):
            zone = lines[i][j]
            if zone < lines[i + 1][j] and zone < lines[i-1][j]:
                if zone < lines[i][j-1] and zone < lines[i][j+1]:
                    basins.append(Basin(zone, [i,j], lines))

    basin_sizes = [basins[i].get_size() for i in range(len(basins))]
    top_three = sorted(basin_sizes, reverse=True)[:3]

    results = np.prod(top_three)
    print(results)
