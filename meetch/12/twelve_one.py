from collections import deque


def search_cave_paths(caves, start, end, q):
    q.append([start])
    paths = []
    while len(q) != 0:
        path = q.popleft()
        if path[-1] == end:
            paths.append(path)
        else:
            for cave in caves[path[-1]]:
                if cave.isupper() or cave not in path:
                    q.append(path + [cave])
    return paths


if __name__ == "__main__":

    with open('input.txt') as f:
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
    paths = search_cave_paths(caves, "start", "end", path_queue)
    small_cave_counter = 0
    for path in paths:
        if any([*map(lambda x:x.islower(), path[1:-1])]):
            small_cave_counter += 1
    print(small_cave_counter)
