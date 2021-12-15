import numpy as np


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


def create_neighbors(coord, board):
    n = {}
    nl = []
    x, y = coord[0], coord[1]
    for i in range(-1, 2, 1):
        nl.append([x, y+i])
    for j in range(-1, 2, 1):
        nl.append([x+j, y])
    temp = {}
    for neighbor in nl:
        if neighbor != coord:
            temp[tuple(neighbor)] = board[neighbor[0]][neighbor[1]]
    n[tuple(coord)] = temp
    return n


def dijkstra(start, end, nodes):

    unvisited = {n: float("inf") for n in nodes.keys()}
    unvisited[tuple(start)] = 0
    visited = {}
    parent = {}

    while unvisited:
        min_node = min(unvisited, key=unvisited.get)
        for neighbor in nodes[min_node]:
            if neighbor not in visited:
                if nodes[min_node][neighbor] == 9999:
                    continue
                new_distance = unvisited[min_node] + nodes[min_node][neighbor]
                if new_distance < unvisited[neighbor]:
                    unvisited[neighbor] = new_distance
                    parent[neighbor] = min_node
        visited[min_node] = unvisited[min_node]
        unvisited.pop(min_node)
    return visited[tuple(end)]


if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]
    lines = [list(line) for line in lines]

    path = []
    board = np.array(lines, dtype=int)
    board = np.pad(board, 1, pad_with, padder=9999)

    nodes = {}
    for i in range(1, board.shape[0]-1):
        for j in range(1, board.shape[1]-1):
            nodes.update(create_neighbors([i, j], board))

    m, n = board.shape[0]-2, board.shape[1]-2

    min_cost = dijkstra([1, 1], [m, n], nodes)
    print(min_cost)
