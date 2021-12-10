from collections import deque


def is_matching_closing(s1, s2):
    if (s1 == "(") and (s2 == ")"):
        return True
    if (s1 == "{") and (s2 == "}"):
        return True
    if (s1 == "[") and (s2 == "]"):
        return True
    if (s1 == "<") and (s2 == ">"):
        return True
    return False


def char_for_completion(s):
    if s == "(":
        return ")"
    if s == "{":
        return "}"
    if s == "[":
        return "]"
    if s == "<":
        return ">"


def check_line_for_corruption(line):
    stack = deque()
    opening = set(["(", "{", "[", "<"])
    for ch in line:
        if ch in opening:
            stack.append(ch)
        else:
            popped = stack.pop()
            if not is_matching_closing(popped, ch):
                return ch
    return None


def complete_lines(line):
    stack = deque()
    opening = set(["(", "{", "[", "<"])
    for ch in line:
        if ch in opening:
            stack.append(ch)
        else:
            popped = stack.pop()
    completion_chars = ""
    while len(stack) != 0:
        dangling_char = stack.pop()
        completion_chars += char_for_completion(dangling_char)
    return completion_chars


def autocomplete_score(completion_chars):
    total = 0
    for ch in completion_chars:
        total *= 5
        if ch == ")":
            total += 1
        if ch == "]":
            total += 2
        if ch == "}":
            total += 3
        if ch == ">":
            total += 4
    return(total)


if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

    stack = deque()
    point_lookup = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    corruption_removed_lines = []
    for line in lines:
        corrupted_ch = check_line_for_corruption(line)
        if not corrupted_ch:
            corruption_removed_lines.append(line)

    scores = []
    for line in corruption_removed_lines:
        completion_chars = complete_lines(line)
        score = autocomplete_score(completion_chars)
        scores.append(score)

    slicer = int((len(scores)-1)/2)
    print(sorted(scores)[slicer])
