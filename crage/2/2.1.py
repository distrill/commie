from enum import Enum


class Direction(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


def getDepth(filename: str):
    inputFile = open(filename, 'r')
    depth = 0
    horizontal = 0
    while True:
        currentLine = inputFile.readline()
        if currentLine == '':
            break
        commandAndDistance = currentLine.split()
        command = commandAndDistance[0].lower()
        distance = int(commandAndDistance[1])
        match command:
            case Direction.FORWARD.value:
                horizontal+=distance
            case Direction.DOWN.value:
                depth+=distance
            case Direction.UP.value:
                depth-=distance
            case _:
                print(f"weird command: {command} {distance}")
    return depth * horizontal



print(getDepth('./crage/2/input.txt'))
