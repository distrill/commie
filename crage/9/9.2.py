class Node():
    def __init__(self, val: int):
        self.val = val
        self.viable = False if val == 9 else True
        self.inBasin = False
        self.adjacents: list[Node] = []

def getBasins(filename: str):
    with open(filename, 'r') as file:
        nodeMap: list[list[Node]] = [[*map(lambda x: Node(int(x)), list(line.strip()))]  for line in file.readlines()]
        for y in range(len(nodeMap)):
            for x in range(len(nodeMap[y])):
                nodeMap[y][x].adjacents = getAdjacents(nodeMap, x, y)
        basins: dict[int, list[Node]] = {}
        basinCount = 0
        for y in range(len(nodeMap)):
            for x in range(len(nodeMap[y])):
                basin = getBasin(nodeMap[y][x])
                if len(basin) > 0:
                    basins[basinCount] = basin
                    basinCount += 1
        basinLengths = [len(basin) for _, basin in basins.items()]
        basinLengths.sort(reverse=True)
        return basinLengths[0] * basinLengths[1] * basinLengths[2]
        

def getBasin(node: Node):
    if node.viable and not node.inBasin:
        visited = [node]
        queue = [node]
        node.inBasin = True
        while len(queue) > 0:
            current = queue.pop()
            for adjacent in current.adjacents:
                if adjacent.viable == True and not adjacent.inBasin and adjacent not in visited:
                    adjacent.inBasin = True
                    queue.append(adjacent)
                    visited.append(adjacent)
        return visited
    else:
        return []

def getAdjacents(area: list[list[Node]], x: int, y: int):
    adjacentCoords = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    return [*filter(lambda n: n.val != -1, [area[adjacentY][adjacentX] if isValidCoord(area, adjacentX, adjacentY) else Node(-1) for adjacentX, adjacentY in adjacentCoords])]

def isValidCoord(area: list[list[Node]], x: int, y: int):
    if x < 0 or y < 0 or y >= len(area) or x >= len(area[y]):
        return False
    else:
        return True

print(getBasins('./crage/9/input.txt'))
