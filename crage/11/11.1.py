class Octopus():
    def __init__(self, val: int):
        self.val: int = val
        self.flashedThisIteration: bool = False
        self.adjacents: list[Octopus] = []

def getAdjacents(area: list[list[Octopus]], x: int, y: int):
    adjacentCoords = [(adjX, adjY) for adjX in range(x - 1, x + 2) for adjY in range(y - 1, y + 2) if not (adjX == x and adjY == y)]
    return [area[adjacentY][adjacentX] for adjacentX, adjacentY in adjacentCoords if isValidCoord(area, adjacentX, adjacentY)]

def isValidCoord(area: list[list[Octopus]], x: int, y: int):
    if x < 0 or y < 0 or y >= len(area) or x >= len(area[y]):
        return False
    else:
        return True

def energizeOctopi(octopiSets: list[set[Octopus]]):
    for y in range(len(octopiSets) - 2, -1, -1):
        octopiSet = octopiSets[y]
        for octopus in octopiSet:
            octopus.val += 1

        octopiSets[y + 1].update(octopiSet)
        octopiSets[y] = set([])

def resetFlashedOctopi(flashedOctopi: set[Octopus]):
    for octopus in flashedOctopi:
        octopus.flashedThisIteration = False

def getOctopiFlashCount(filename: str):
    with open(filename, 'r') as file:
        octopiSets: list[set[Octopus]] = [set([]) for _ in range(10)]
        octopiMap: list[list[Octopus]] = [[*map(lambda x: Octopus(int(x)), list(line.strip()))]  for line in file.readlines()]
        for y in range(len(octopiMap)):
            for x in range(len(octopiMap[y])):
                currentOctopus = octopiMap[y][x]
                octopiSets[currentOctopus.val].add(currentOctopus)
                octopiMap[y][x].adjacents = getAdjacents(octopiMap, x, y)
        
        flashes = 0
        for _ in range(100):
            flashedZeroes: set[Octopus] = set([])
            while len(octopiSets[9]) > 0:
                nineEnergyOctopus = octopiSets[9].pop()
                nineEnergyOctopus.flashedThisIteration = True
                flashedZeroes.add(nineEnergyOctopus)
                nineEnergyOctopus.val = 0
                flashes += 1
                for adjacent in nineEnergyOctopus.adjacents:
                    if adjacent.val != 9 and not adjacent.flashedThisIteration:
                        octopiSets[adjacent.val].remove(adjacent)
                        octopiSets[adjacent.val + 1].add(adjacent)
                        adjacent.val += 1
            energizeOctopi(octopiSets)
            resetFlashedOctopi(flashedZeroes)
            octopiSets[0] = flashedZeroes

        return flashes

print(getOctopiFlashCount('./crage/11/input.txt'))
