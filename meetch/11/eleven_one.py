import numpy as np
from collections import deque


def get_adjacencies(data):
    adjacencies = []
    for point in data:
        x, y = point[0], point[1]
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                new_point = [x + i, y + j]
                if new_point != point:
                    adjacencies.append(new_point)
    return adjacencies


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


class Octopuses:
    def __init__(self, game_board):
        self.game_board = game_board
        self.num_flashes = 0
        self.find_nines()
        self.already_flashed = []

    def find_nines(self):
        nines = []
        lines = self.game_board
        for j in range(1, len(lines[0])-1):
            for i in range(1, len(lines) - 1):
                if lines[i][j] == 9:
                    nines.append([i, j])
        self.nines = nines

    def check_for_all_zeros(self):
        for j in range(1, len(self.game_board[0])-1):
            for i in range(1, len(self.game_board) - 1):
                if self.game_board[i][j] != 0:
                    return False
        return True
                         

    def make_step(self):
        if self.check_for_all_zeros():
            return True
        self.already_flashed = []
        self.find_nines()
        lines = self.game_board
        for j in range(1, len(lines[0])-1):
            for i in range(1, len(lines) - 1):
                if lines[i][j] == 9:
                    lines[i][j] = 0
                    self.num_flashes += 1
                    self.already_flashed.append([i,j])
                else:
                    lines[i][j] += 1
        self.make_flashes()
        return False

    def make_flashes(self):
        adjs = get_adjacencies(self.nines)
        q = deque()
        if adjs:
            [q.append(adj) for adj in adjs]
        while len(q) != 0:
            coord = q.pop()
            x, y = coord[0], coord[1]
            if [x, y] in self.already_flashed:
                continue
            if self.game_board[x][y] == 9:
                self.game_board[x][y] = 0
                self.num_flashes += 1
                self.already_flashed.append([x,y])
                adjs = get_adjacencies([[x, y]])
                [q.append(adj) for adj in adjs]
            else:
                self.game_board[x][y] += 1


if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

    lines = [x.replace("\n", "")for x in lines]
    lines = [list(x) for x in lines]
    lines = [list(map(int, i)) for i in lines]

    lines = np.pad(lines, 1, pad_with, padder=100)

    ocs = Octopuses(lines)
    steps = list(range(100))
    for step in steps:
        is_all_zeros = ocs.make_step()
        if is_all_zeros:
            print(step)
            break
        print(ocs.game_board)
        print(ocs.num_flashes)
