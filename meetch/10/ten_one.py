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



def check_line(line):
    stack = deque()
    stack.clear()
    opening = set(["(", "{", "[", "<"]) 
    for ch in line:
        if ch in opening:
            stack.append(ch)
        else:
            popped = stack.pop()
            if not is_matching_closing(popped, ch):
                return ch
    return None


if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

    point_lookup = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    illegal_score = 0
    for line in lines:
        invalid_char = check_line(line)
        # print(line, "    ", invalid_char, len(line))
        illegal_score += point_lookup.get(invalid_char, 0)

    print(illegal_score)
