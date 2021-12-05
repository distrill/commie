from io import TextIOWrapper

class Point():
    x: int
    y: int
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line():
    start: Point
    end: Point
    points: list[Point]
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.points = []

    def getPoints(self) -> list[Point]:
        if len(self.points) > 0:
            return self.points

        if self.start.x == self.end.x:
            #vertical
            x = self.start.x
            points: list[Point] = []
            smallerY = self.start.y
            largerY = self.end.y
            if self.start.y > self.end.y:
                largerY = self.start.y
                smallerY = self.end.y
            for y in range(smallerY, largerY + 1):
                points.append(Point(x, y))
            self.points = points
            return points

        elif self.start.y == self.end.y:
            #horizontal
            y = self.start.y
            points: list[Point] = []
            smallerX = self.start.x
            largerX = self.end.x
            if self.start.x > self.end.x:
                largerX = self.start.x
                smallerX = self.end.x
            for x in range(smallerX, largerX + 1):
                points.append(Point(x, y))
            self.points = points
            return points

        elif self.end.y - self.end.x == self.start.y - self.start.x:
            #diagonal up right
            points: list[Point] = []
            smallerX = self.start.x
            largerX = self.end.x
            if self.start.x > self.end.x:
                largerX = self.start.x
                smallerX = self.end.x
            smallerY = self.start.y
            largerY = self.end.y
            if self.start.y > self.end.y:
                largerY = self.start.y
                smallerY = self.end.y
            for x, y in zip(range(smallerX, largerX + 1), range(smallerY, largerY + 1)):
                points.append(Point(x, y))
            self.points = points
            return points

        elif self.end.y - self.start.y == self.start.x - self.end.x:
            #diagonal down right
            points: list[Point] = []
            smallerX = self.start.x
            largerX = self.end.x
            if self.start.x > self.end.x:
                largerX = self.start.x
                smallerX = self.end.x
            smallerY = self.start.y
            largerY = self.end.y
            if self.start.y > self.end.y:
                largerY = self.start.y
                smallerY = self.end.y
            x = smallerX
            y = largerY
            while x <= largerX and y >= smallerY:
                points.append(Point(x, y))
                x += 1
                y -= 1
            self.points = points
            return points 
        else:
            points: list[Point] = []
            return points

def getPointCounts(lines: list[Line]):
    pointCounts: dict[tuple[int, int], int] = {}
    for line in lines:
        for point in line.getPoints():
            tuplePoint: tuple[int, int] = (point.x, point.y)
            if tuplePoint in pointCounts:
                pointCounts[tuplePoint] += 1
            else:
                pointCounts[tuplePoint] = 1
    return pointCounts

def populateLines(file: TextIOWrapper):
    lines: list[Line] = []
    while True:
        # 503,977 -> 843,637
        fileLine = file.readline().rstrip()
        if fileLine == '':
            break
        splitOnArrowLine = fileLine.split(" -> ")
        start = splitOnArrowLine[0].split(",")
        end = splitOnArrowLine[1].split(",")
        startX = int(start[0])
        startY = int(start[1])
        endX = int(end[0])
        endY = int(end[1])
        if startX == endX or startY == endY or endY - endX == startY - startX or endY - startY == startX - endX:
            line = Line(Point(startX, startY), Point(endX, endY))
            lines.append(line)
    return lines

def findIntersections(filename: str):
    point: tuple[int, int] = (1, 1)
    pointCounts: dict[tuple[int, int], int] = {}
    pointCounts[point] = 1
    pointCounts[point] = 1

    with open(filename, 'r') as file:
        lines = populateLines(file)
        pointCounts = getPointCounts(lines)
        intersections = 0
        for _, count in pointCounts.items():
            if count > 1:
                intersections+=1
        return intersections
        
print(findIntersections('./crage/5/input.txt'))