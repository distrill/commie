from typing import Counter
from collections import defaultdict

def getPolymerCount(filename: str, iterations: int):
    with open(filename, 'r') as file:
        template = file.readline().strip()
        templatePortionMap = createTemplatePortionMap(template)
        commands = [line.strip().split(" -> ") for line in file.readlines() if line.strip() != ""]
        matchInserts = {match:insert for (match, insert) in commands}
        letterCounts = defaultdict(lambda: 0, Counter(template))
        for _ in range(iterations):
            temporaryMap = defaultdict(lambda: 0, templatePortionMap)
            for match, insert in matchInserts.items():
                if match in temporaryMap and temporaryMap[match] > 0:
                    amount = temporaryMap[match]
                    templatePortionMap[match] -= amount
                    templatePortionMap[f"{match[0]}{insert}"] += amount
                    templatePortionMap[f"{insert}{match[1]}"] += amount
                    letterCounts[insert] += amount
        counts = [count for _, count in letterCounts.items()]
        leastCommon = min(counts)
        mostCommon = max(counts)
        return mostCommon - leastCommon
                

def createTemplatePortionMap(template: str) -> defaultdict[str, int]:
    templatePortionMap: defaultdict[str, int] = defaultdict(lambda: 0)
    for i in range(len(template) - 1):
        portion = f"{template[i]}{template[i + 1]}"
        templatePortionMap[portion] += 1
    return templatePortionMap

print(getPolymerCount('./crage/14/input.txt', 10))
print(getPolymerCount('./crage/14/input.txt', 40))
