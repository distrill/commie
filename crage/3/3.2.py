from enum import Enum
from io import TextIOWrapper
from typing import Set

def getIntegerSet(file: TextIOWrapper):
    integerSet: set[int] = set()
    while True:
        currentLine = file.readline().rstrip()
        if currentLine == '':
            break
        integerSet.add(int(currentLine, 2))
    return integerSet


def average(ns: set[int]):
    return sum(ns) / len(ns)

def getGreatestBitCriteria(integerSet: set[int], start: int):
    currentSet = integerSet
    currentCeiling = start
    currentFloor = 0
    currentMiddle = average([currentFloor, currentCeiling])
    while currentCeiling - currentFloor > 1:
        lessThan = [n for n in currentSet if n < currentMiddle]
        greaterThan = [n for n in currentSet if n >= currentMiddle]
        if len(lessThan) > len(greaterThan):
            currentSet = lessThan
            currentCeiling = currentMiddle
        else:
            currentSet = greaterThan
            currentFloor = currentMiddle
        currentMiddle = average([currentFloor, currentCeiling])
        
    return currentSet

def getSmallestBitCriteria(integerSet: set[int], start: int):
    currentSet = integerSet
    currentCeiling = start
    currentFloor = 0
    currentMiddle = average([currentFloor, currentCeiling])
    while currentCeiling - currentFloor > 1 and len(currentSet) != 1:
        lessThan = [n for n in currentSet if n < currentMiddle]
        greaterThan = [n for n in currentSet if n >= currentMiddle]
        if len(lessThan) <= len(greaterThan):
            currentSet = lessThan
            currentCeiling = currentMiddle
        else:
            currentSet = greaterThan
            currentFloor = currentMiddle
        currentMiddle = average([currentFloor, currentCeiling])
        
    return currentSet

def getLifeSupportRating(filename: str):
    inputFile = open(filename, 'r')
    integerSet: set[int]= getIntegerSet(inputFile)
    inputFile.close()
    inputFile = open(filename, 'r')
    currentLine = inputFile.readline().rstrip()
    maximum = 2 ** len(currentLine)
    greaterOccurrenceSet = getGreatestBitCriteria(integerSet, maximum) # oxygen generator rating
    smallestOccurrenceSet = getSmallestBitCriteria(integerSet, maximum) # 
    return greaterOccurrenceSet.pop() * smallestOccurrenceSet.pop()

print(getLifeSupportRating('./crage/3/input.txt'))