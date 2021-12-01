from io import TextIOWrapper


def cycle(data, start=None):
    k = 0 if not start else start
    while True:
        yield data[k]
        k = (k + 1) % len(data)


def initializeWindow(file: TextIOWrapper, windowSize):
    window = []
    for _ in range(windowSize):
        window.append(int(file.readline()))
    return window


inputFile = open('./1/input.txt', 'r')
currentWindow = initializeWindow(inputFile, 3)
increaseCount = 0
previousSum = sum(currentWindow)
for i in cycle([0, 1, 2]):
    currentLine = inputFile.readline()
    if currentLine == '':
        break
    else:
        currentMeasurement = int(currentLine)
        currentSum = previousSum - currentWindow[i] + currentMeasurement
        if previousSum < currentSum:
            print("(increased)")
            increaseCount += 1
        else:
            print("(decreased)")

        previousSum = currentSum
        currentWindow[i] = currentMeasurement
        previousMeasurement = currentMeasurement

print(increaseCount)
