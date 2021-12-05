import numpy as np


def stamp_board(board, number):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                board[i][j] = -1


def board_checker(board):
    has_won = True
    columns = board.sum(axis=0)
    rows = board.sum(axis=1)
    if (-5 in columns) or (-5 in rows):
        return True
    return False


def stamp_and_check(boards, numbers):
    for cn in called_numbers:
        print(cn)
        for board in boards:
            stamp_board(board, cn)
            has_won = board_checker(board)
            print(board)
            if has_won:
                return board, cn


def process_winning_board(board, called_number):
    flat = board.reshape(-1)
    sum_unmarked = flat[flat != -1].sum()
    return (sum_unmarked * called_number)


if __name__ == "__main__":

    with open('numbers.txt') as f:
        called_numbers = f.readlines()
    called_numbers = [int(x) for x in called_numbers[0].split(",")]

    with open('boards.txt') as f:
        boards = f.readlines()

    numbers = []
    for line in boards:
        l = line.replace("\n", "")
        if l != "":
            numbers.append(l)

    numbers = [x.split(" ") for x in numbers]

    flat_numbers = []

    for n in numbers:
        for m in n:
            if m != "":
                flat_numbers.append(int(m))

    numbers = np.array(flat_numbers)
    boards = np.reshape(numbers, (-1, 5, 5))

    winning_board, winning_number = stamp_and_check(boards, called_numbers)

    print(winning_board, winning_number)

    print(process_winning_board(winning_board, winning_number))
