from typing import Counter
def minimizeCrabFuel(filename: str):
    with open(filename, 'r') as file:
        positionCounts = Counter([*map(int, file.readlines()[0].split(","))])
        maxCrabPosition = max(positionCounts.keys())
        currentMinDistance = float('inf')
        currentTotal = 0
        for i in range(min(positionCounts.keys()), maxCrabPosition + 1):
            for j in range(maxCrabPosition + 1):
                if j in positionCounts:
                    distance = abs(j - i)
                    fuelUsedAtPosition = (distance) * (distance + 1) / 2
                    currentTotal += abs(positionCounts[j] * fuelUsedAtPosition)
            if currentTotal < currentMinDistance:
                currentMinDistance = currentTotal
            currentTotal = 0
        return currentMinDistance



print(minimizeCrabFuel('./crage/7/input.txt'))