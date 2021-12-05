from five_one import *


def test_create_line_segment():

    test1 = "1,1 -> 1,4"
    line_seg = create_line_segment(test1)
    assert line_seg == [[1, 1], [1, 2], [1, 3], [1, 4]]

    test1 = "4,1 -> 1,1"
    line_seg = create_line_segment(test1)
    assert line_seg == [[1, 1], [2, 1], [3, 1], [4, 1]]

    test1 = "1,1 -> 4,4"
    line_seg = create_line_segment(test1)
    assert line_seg == None

    test1 = "1,1 -> 4,1"
    line_seg = create_line_segment(test1)
    assert line_seg == [[1, 1], [2, 1], [3, 1], [4, 1]]


def test_fill_board():

    lines = [[[1, 1], [1, 2], [1, 3], [1, 4]],
             [[1, 1], [2, 1], [3, 1], [4, 1]]]

    result = fill_board(lines)
    expected = {'1,1': 2, '1,2': 1, '1,3': 1,
                '1,4': 1, '2,1': 1, '3,1': 1, '4,1': 1}

    assert result == expected


def test_count_intersections():

    test_board = {'1,1': 2, '1,2': 1, '1,3': 1,
                  '1,4': 1, '2,1': 1, '3,1': 1, '4,1': 1}
    intersections = count_intersections(test_board)
    assert len(intersections) == 1


if __name__ == "__main__":

    test_create_line_segment()
    test_fill_board()
    test_count_intersections()
