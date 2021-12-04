from io import TextIOWrapper
from math import sqrt

class Node():
    x: int
    y: int
    checked: bool
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.checked = False

class Board():
    nodes: dict[int, Node]
    columnCounts: dict[int, int]
    rowCounts: dict[int, int]
    sideLength: int

    def __init__(self, values: list[list[int]]):
        self.columnCounts: dict[int, int] = {}
        self.rowCounts: dict[int, int] = {}
        self.nodes = self.initializeNodes(values)
        self.sideLength = sqrt(len(self.nodes))

    def initializeNodes(self, values: list[list[int]]):
        nodes: dict[int, Node] = {}
        for y in range(len(values)):
            row = values[y]
            for x in range(len(row)):
                nodes[row[x]] = Node(x, y)
        return nodes

    def updateCounts(self, value: int):
        if value in self.nodes:
            node = self.nodes[value]
            if not node.checked:
                if node.x in self.columnCounts:
                    self.columnCounts[node.x] += 1
                else:
                    self.columnCounts[node.x] = 1

                if node.y in self.rowCounts:
                    self.rowCounts[node.y] += 1
                else:
                    self.rowCounts[node.y] = 1
                node.checked = True
    
    def checkIfBoardComplete(self, value: int):
        if value in self.nodes:
            node = self.nodes[value]
            if self.columnCounts[node.x] == self.sideLength or self.rowCounts[node.y] == self.sideLength:
                return True
        return False

    def sumBoardUnmarked(self):
        sum = 0
        for val, node in self.nodes.items():
            if not node.checked:
                sum += val
        return sum

def initializeBoards(file: TextIOWrapper):
    twoBlankLineCount = 0
    boards: list[Board] = []
    currentBoardList: list[list[int]] = []
    while twoBlankLineCount != 2:
        line = file.readline().rstrip()
        if line == "":
            twoBlankLineCount += 1
            if len(currentBoardList) > 0:
                boards.append(Board(currentBoardList))
                currentBoardList = []
        else:
            twoBlankLineCount = 0
            currentBoardLine = list(map(int, line.replace("  ", " ").strip().split(" ")))
            currentBoardList.append(currentBoardLine)

    return boards

def playGame(filename: str):
    with open(filename, 'r') as file:
        bingoDrawsLine = file.readline().split(",")
        bingoDraws = list(map(int, bingoDrawsLine))
        boards: set[Board] = initializeBoards(file)
        for bingoDraw in bingoDraws:
            if len(boards) == 1:
                loser = boards.pop()
                loser.updateCounts(bingoDraw)
                if loser.checkIfBoardComplete(bingoDraw):
                    return loser.sumBoardUnmarked() * bingoDraw
                boards.append(loser)
            else:
                for board in list(boards):
                    board.updateCounts(bingoDraw)
                    if board.checkIfBoardComplete(bingoDraw):
                        boards.remove(board)

print(playGame('./crage/4/input.txt'))
    

        
