from five_two import *


def test_create_line_segment():

    test = "1,1 -> 1,4"
    line_seg = create_line_segment(test)
    assert line_seg == [[1, 1], [1, 2], [1, 3], [1, 4]]

    test = "4,1 -> 1,1"
    line_seg = create_line_segment(test)
    assert line_seg == [[1, 1], [2, 1], [3, 1], [4, 1]]

    test = "1,1 -> 4,4"
    line_seg = create_line_segment(test)
    assert line_seg == [[1, 1], [2, 2], [3, 3], [4, 4]]

    test = "4,4 -> 1,1"
    line_seg = create_line_segment(test)
    assert line_seg == [[1, 1], [2, 2], [3, 3], [4, 4]][::-1]

    test = "1,1 -> 4,1"
    line_seg = create_line_segment(test)
    assert line_seg == [[1, 1], [2, 1], [3, 1], [4, 1]]

    test = "1,1 -> 3,3"
    line_seg = create_line_segment(test)
    assert line_seg == [[1, 1], [2, 2], [3, 3]]

    test = "9,7 -> 7,9"
    line_seg = create_line_segment(test)
    assert line_seg == [[9, 7], [8, 8], [7, 9]]


if __name__ == "__main__":

    test_create_line_segment()
