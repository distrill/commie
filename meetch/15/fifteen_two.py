import numpy as np
import time

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

    start_time = time.time()

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]
    lines = [list(line) for line in lines]

    path = []
    board = np.array(lines, dtype=int)

    # make the board 5x larger
    new_board = board[:]
    for i in range(1, 5):
        temp = board + i
        new_board = np.concatenate((new_board, temp), axis=1)
    second_new_board = new_board[:]
    for i in range(1, 5):
        temp = new_board + i
        second_new_board = np.concatenate((second_new_board, temp), axis=0)
    board = second_new_board[:]
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] > 9:
                board[i][j] -= 9
    board = np.pad(board, 1, pad_with, padder=9999)

    nodes = {}
    for i in range(1, board.shape[0]-1):
        for j in range(1, board.shape[1]-1):
            nodes.update(create_neighbors([i, j], board))

    m, n = board.shape[0]-2, board.shape[1]-2

    min_cost = dijkstra([1, 1], [m, n], nodes)
    print(min_cost)
    print("time taken : ", time.time() - start_time)
