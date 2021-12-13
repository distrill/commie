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
            return len(coords)

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

print(getCoords('./crage/13/input.txt'))
