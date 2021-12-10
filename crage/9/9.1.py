def getLocalMinima(filename: str):
    with open(filename, 'r') as file:
        numberLines: list[list[int]] = [[*map(int, list(line.strip()))]  for line in file.readlines()]
        minima: list[int] = [*filter(lambda x: x >= 0, [numberLines[y][x] if validateMinimum(numberLines, x, y) else -1 for y in range(len(numberLines)) for x in range(len(numberLines[y]))])]
        return sum(minima) + len(minima)

def validateMinimum(area: list[list[int]], x: int, y: int):
    candidate = area[y][x]
    if candidate < getIndexedOrInf(area, x - 1, y) and candidate < getIndexedOrInf(area, x + 1, y) and candidate < getIndexedOrInf(area, x, y - 1) and candidate < getIndexedOrInf(area, x, y + 1):
            return True
    return False

def getIndexedOrInf(area: list[list[int]], x: int, y: int):
    try:
        return area[y][x]
    except IndexError:
        return float('inf')

print(getLocalMinima('./crage/9/input.txt'))
