from typing import Counter


def findLaternfishCount(filename: str, iterations: int):
    with open(filename, 'r') as file:
        fishAges = [*map(int, file.readlines()[0].rstrip().split(","))]
        fishAgeCounts: dict[int, int] = Counter(fishAges)
        rebirthAge = 6
        birthAge = 8
        for _ in range(iterations):
            newFishAgeCounts: dict[int, int] = {}
            for age, count in fishAgeCounts.items():
                if age == 0:
                    newFishAgeCounts[birthAge] = count if birthAge not in newFishAgeCounts else newFishAgeCounts[birthAge] + count
                    newFishAgeCounts[rebirthAge] = count if rebirthAge not in newFishAgeCounts else newFishAgeCounts[rebirthAge] + count
                else:
                    newFishAgeCounts[age - 1] = count if age - 1 not in newFishAgeCounts else newFishAgeCounts[age - 1] + count
            fishAgeCounts = newFishAgeCounts
    return sum([count for _, count in fishAgeCounts.items()])

print(findLaternfishCount('./crage/6/input.txt', 80))
print(findLaternfishCount('./crage/6/input.txt', 256))