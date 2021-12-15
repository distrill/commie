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

def outputNewGrid(inputFileName: str, outputFileName: str):
    gridLines: list[str] = []
    with open(inputFileName, 'r') as inputFile:
        for i in range(100):
            line = inputFile.readline().strip()
            gridLines.append(line)
            for _ in range(4):
                additionalLine = "".join([*map(str, [*map(lambda c: int(c) + 1 if int(c) < 9 else 1, line)])])
                gridLines[i] += additionalLine
                line = additionalLine
        iterations = len(gridLines)
        for i in range(4):
            for j in range(iterations):
                line = gridLines[i * 100 + j]
                additionalLine = "".join([*map(str, [*map(lambda c: int(c) + 1 if int(c) < 9 else 1, line)])])
                gridLines.append(additionalLine)
    with open(outputFileName, 'w') as outputFile:
        for line in gridLines:
            outputFile.write(f'{line}\n')

outputNewGrid('./crage/15/input.txt', './crage/15/newinput.txt')
print(getShortestPath('./crage/15/newinput.txt'))
