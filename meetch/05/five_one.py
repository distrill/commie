import numpy as np


def create_line_segment(points):
    p1, p2 = points.split("->")
    x1, y1 = [int(x) for x in p1.split(",")]
    x2, y2 = [int(x) for x in p2.split(",")]
    if (x1 != x2) and (y1 != y2):
        return None
    if (x1 != x2):
        if x2 < x1:
            x1, x2 = x2, x1
        r = np.arange(x1, x2 + 1, 1)
        pts = [[x, y1] for x in r]
    else:
        if y2 < y1:
            y1, y2 = y2, y1
        r = np.arange(y1, y2 + 1, 1)
        pts = [[x1, y] for y in r]
    return pts


def fill_board(lines):
    board = {}
    for line in lines:
        for point in line:
            p = ",".join(map(str, point))
            if p in board:
                board[p] += 1
            else:
                board[p] = 1
    return board


def count_intersections(board):
    intersections = []
    for point, count in board.items():
        if count > 1:
            intersections.append(point)
    return intersections


if __name__ == "__main__":

    with open('5.input.txt') as f:
        lines = f.readlines()

    lines = [x.replace("\n", "")for x in lines]

    # TODO combine into one list comprehension?
    line_segements = [create_line_segment(x) for x in lines]
    line_segements = [x for x in line_segements if x is not None]

    board = fill_board(line_segements)

    num_ints = len(count_intersections(board))

    print(num_ints)
