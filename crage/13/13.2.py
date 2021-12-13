from io import TextIOWrapper


def getCoords(filename: str):
    with open(filename, 'r') as file:
        coords: set[tuple[int, int]] = initializeCoords(file)
        flipInstructions: list[tuple[str, int]] = initializeFlips(file)
        for axis, lineNumber in flipInstructions:
            for coord in set(coords):
                x, y = coord
                if axis == 'y' and y > lineNumber:
                    coords.remove((x, y))
                    shift = y - lineNumber
                    newY = lineNumber - shift
                    coords.add((x, newY))
                elif axis == 'x' and x > lineNumber:
                    coords.remove((x, y))
                    shift = abs(x - lineNumber)
                    newX = lineNumber - shift
                    coords.add((newX, y))
        return coords

def initializeCoords(file: TextIOWrapper) -> set[tuple[int, int]]:
    coords: set[tuple[int, int]] = set([])
    line = file.readline().strip()
    while line != "":
        x, y = line.split(",")
        coords.add((int(x), int(y)))
        line = file.readline().strip()
    return coords

def initializeFlips(file: TextIOWrapper) -> list[tuple[str, int]]:
    flipInstructions: list[tuple[str, int]] = []
    line = file.readline().strip()
    while line != "":
        instruction = line.split(" ")[2]
        axis, lineNumber = instruction.split("=")
        flipInstructions.append((axis, int(lineNumber)))
        line = file.readline().strip()
    return flipInstructions

def printCoords(coords: set[tuple[int, int]]):
    maxX = max([x for x, _ in coords])
    maxY = max([y for _, y in coords])
    for y in range(maxY + 1):
        line = ""
        for x in range(maxX + 1):
            if (x, y) in coords:
                line += " # "
            else:
                line += " . "
        print(line)

printCoords(getCoords('./crage/13/input.txt'))
