from enum import Enum
from io import TextIOWrapper
class Values:
    zeroes: int
    ones: int

    def __init__(self, zero=0, one=0):
        self.zeroes = zero
        self.ones = one

class eValues(Enum):
    ZERO = '0'
    ONE = '1'

def getBinaryCounts(file: TextIOWrapper):
    binaryCounts: dict[int, Values] = {}
    while True:
        currentLine = file.readline().rstrip()
        if currentLine == '':
            break
        for i in range(len(currentLine)):
            if i not in binaryCounts:
                match currentLine[i]:
                    case eValues.ZERO.value:
                        binaryCounts[i] = Values(zero=1)
                    case eValues.ONE.value:
                        binaryCounts[i] = Values(one=1)
            else:
                match currentLine[i]:
                    case eValues.ZERO.value:
                        binaryCounts[i].zeroes += 1
                    case eValues.ONE.value:
                        binaryCounts[i].ones += 1
    return binaryCounts

def getGreaterOccurrenceBinary(binaryCounts: dict[int, Values]):
    greaterOccurrenceBinary: str = ""
    for _, binaries in binaryCounts.items():
        if binaries.zeroes < binaries.ones:
            greaterOccurrenceBinary += eValues.ONE.value
        else:
            greaterOccurrenceBinary += eValues.ZERO.value
    return greaterOccurrenceBinary

def getPowerConsumption(filename: str):
    inputFile = open(filename, 'r')
    binaryCounts: dict[int, Values] = getBinaryCounts(inputFile)
    greaterOccurrenceBinary = getGreaterOccurrenceBinary(binaryCounts)
    greaterOccurrenceInt = int(greaterOccurrenceBinary, 2) # gamma
    inverseInt = 2 ** len(greaterOccurrenceBinary) - 1 - greaterOccurrenceInt # epsilon
    return greaterOccurrenceInt * inverseInt

print(getPowerConsumption('./crage/3/input.txt'))