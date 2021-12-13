class Cave():
    def __init__(self, isSmall: bool, val: str):
        self.adjacents: set[Cave] = set([])
        self.isSmall = isSmall
        self.val = val

class Path():
    def __init__(self, path: list[Cave], visitedSmallCaveCounts: dict[str, int] = {}, visitedSmallTwice: bool = False):
        self.nodes: list[Cave] = [*path]
        self.visitedSmallCaveCounts: dict[str, int] = visitedSmallCaveCounts
        self.visitedSmallTwice = visitedSmallTwice

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
                if adjacent.val != "start":
                    if not currentPath.visitedSmallTwice or not adjacent.isSmall or (adjacent.isSmall and adjacent.val not in currentPath.visitedSmallCaveCounts):
                        newVisitedSmallCaveCounts = dict(currentPath.visitedSmallCaveCounts)
                        newPathVisitedTwice = currentPath.visitedSmallTwice
                        if adjacent.val not in currentPath.visitedSmallCaveCounts and adjacent.isSmall and adjacent.val != 'end':
                            newVisitedSmallCaveCounts[adjacent.val] = 1
                        elif adjacent.isSmall and adjacent.val != 'end' and adjacent.val in currentPath.visitedSmallCaveCounts:
                            newPathVisitedTwice = True
                        newPath = Path(list(currentPath.nodes), newVisitedSmallCaveCounts, newPathVisitedTwice)
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
