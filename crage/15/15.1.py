class Node():
    def __init__(self, val: int):
        self.val: int = val
        self.cost = float('inf')
        self.adjacents: list[Node] = []
        self.visited = False

def getAdjacents(area: list[list[Node]], x: int, y: int):
    adjacentCoords = [(adjX, y) for adjX in range(x - 1, x + 2) if not adjX == x] + [(x, adjY) for adjY in range(y - 1, y + 2) if not adjY == y]
    return [area[adjacentY][adjacentX] for adjacentX, adjacentY in adjacentCoords if isValidCoord(area, adjacentX, adjacentY)]

def isValidCoord(area: list[list[Node]], x: int, y: int):
    if x < 0 or y < 0 or y >= len(area) or x >= len(area[y]):
        return False
    else:
        return True

def getShortestPath(filename: str):
    with open(filename, 'r') as file:
        grid = [[*map(lambda x: Node(int(x)), list(line.strip()))] for line in file.readlines()]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                node = grid[y][x]
                node.adjacents = getAdjacents(grid, x, y)

        startNode = grid[0][0]
        startNode.cost = 0
        endNode = grid[len(grid) - 1][len(grid[0]) - 1]
        unvisited: set[Node] = set({})
        unvisited.add(startNode)
        while len(unvisited) > 0:
            nearestMinimum = min(unvisited, key=lambda n: n.cost)
            nearestMinimum.visted = True
            unvisited.remove(nearestMinimum)
            for adjacent in [*filter(lambda n: not n.visited, nearestMinimum.adjacents)]:
                if nearestMinimum.cost + adjacent.val < adjacent.cost:
                    adjacent.cost = nearestMinimum.cost + adjacent.val
                    unvisited.add(adjacent)
        return endNode.cost



print(getShortestPath('./crage/15/input.txt'))
