class Cave():
    def __init__(self, isSmall: bool, val: str):
        self.adjacents: set[Cave] = set([])
        self.isSmall = isSmall
        self.val = val

class Path():
    def __init__(self, path: list[Cave]):
        self.nodes: list[Cave] = [*path]

def getUniquePaths(filename: str):
    with open(filename, 'r') as file:
        caveStartsAndEnds = [line.strip() for line in file.readlines()]
        caveMap: dict[str, Cave] = initializeCaves(caveStartsAndEnds)
        pathQueue: list[Path] = []
        startPath = Path([caveMap["start"]])
        pathQueue.append(startPath)
        paths: set[Path] = set()

        while len(pathQueue) > 0:
            currentPath = pathQueue.pop()
            currentPathEnd = currentPath.nodes[-1]
            for adjacent in currentPathEnd.adjacents:
                if not adjacent.isSmall or (adjacent.isSmall and adjacent not in currentPath.nodes):
                    newPath = Path(list(currentPath.nodes))
                    newPath.nodes.append(adjacent)

                    if adjacent.val == 'end':
                        paths.add(newPath)
                    else:
                        pathQueue.append(newPath)
        return len(paths)

def initializeCaves(startEnds: list[str]) -> dict[str, Cave]:
    caveMap: dict[str, Cave] = {}
    
    for startEnd in startEnds:
        start, end = startEnd.split("-")
        startCave = Cave(isSmallCave(start), start)
        endCave = Cave(isSmallCave(end), end)
        if start not in caveMap:
            caveMap[start] = startCave
        else:
            startCave = caveMap[start]
        if end not in caveMap:
            caveMap[end] = endCave
        else:
            endCave = caveMap[end]
        caveMap[start].adjacents.add(endCave)
        caveMap[end].adjacents.add(startCave)
    return caveMap

def isSmallCave(caveStr: str) -> bool:
    return all([True if not char.isupper() else False for char in caveStr])

print(getUniquePaths('./crage/12/input.txt'))
