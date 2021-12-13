import numpy as np


def get_board_size(points):
    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])
    return max_x, max_y


def create_game_board(points):
    max_x, max_y = get_board_size(points)
    game_board = np.zeros((max_y+1, max_x+1))
    for point in points:
        game_board[point[1], point[0]] = 1
    return game_board


def make_fold_up(board, index):
    first_half = board[:int(index)]
    second_half = board[int(index)+1:]
    xs, ys = np.where(second_half == 1)
    # mirror the x points
    xs = [first_half.shape[0] - 1 - x for x in xs]
    # add 2nd half's points to first
    for x, y in zip(xs, ys):
        first_half[x][y] = 1
    return first_half


def make_fold_left(board, index):
    first_half = board[:, :int(index)]
    second_half = board[:, int(index)+1:]
    xs, ys = np.where(second_half == 1)
    # mirror the y points
    ys = [first_half.shape[1] - 1 - y for y in ys]
    # add 2nd half's points to first
    for x, y in zip(xs, ys):
        first_half[x][y] = 1
    return first_half


def make_fold(board, fold):
    fold_direction, fold_index = fold.split("=")
    if fold_direction == "y":
        return make_fold_up(board, fold_index)
    else:
        return make_fold_left(board, fold_index)


if __name__ == "__main__":

    # test_param = "test_"
    test_param = ""

    with open('{}input.txt'.format(test_param)) as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]
    points = [x.split(",") for x in lines]
    points = [list(map(int, i)) for i in points]

    with open('{}folds.txt'.format(test_param)) as f:
        folds = f.readlines()
    folds = [x.replace("\n", "") for x in folds]
    folds = [x.split(" ")[2] for x in folds]

    game_board = create_game_board(points)

    for fold in folds:
        game_board = make_fold(game_board, fold)
        break

    print(int(sum(sum(game_board))))
