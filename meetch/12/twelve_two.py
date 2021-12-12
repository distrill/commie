from collections import deque
from collections import Counter


def can_do_second_small_cave(path):
    count_dict = Counter(path)
    for key, value in count_dict.items():
        if key.islower():
            if value > 1:
                return False
    return True


def search_save_paths(caves, start, end, q):
    q.append([start])
    paths = []
    while len(q) != 0:
        path = q.popleft()
        if path[-1] == end:
            paths.append(path)
        else:
            for cave in caves[path[-1]]:
                if cave.islower() and cave in path:
                    if can_do_second_small_cave(path):
                        if cave in [start, end]:
                            continue
                    else:
                        continue
                q.append(path + [cave])
    return paths


if __name__ == "__main__":

    with open('test_input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

    # populate caves dict
    caves = {}
    for line in lines:
        for i in range(2):
            if i == 0:
                n1, n2 = line.split("-")
            else:
                n2, n1 = line.split("-")
            if n1 not in caves:
                caves[n1] = [n2]
            else:
                caves[n1].append(n2)

    path_queue = deque()

    small_cave_counter = 0
    paths = search_save_paths(caves, "start", "end", path_queue)
    print(len(paths))
