inputFile = open('./1/input.txt', 'r')
readFlag = True
increaseCount = 0
previousMeasurement = int(inputFile.readline())
while readFlag == True:
    currentLine = inputFile.readline()
    if currentLine == '':
        readFlag = False
    else:
        currentMeasurement = int(currentLine)
        if previousMeasurement < currentMeasurement:
            print("(increased)")
            increaseCount += 1
        else:
            print("(decreased)")
        previousMeasurement = currentMeasurement

print(increaseCount)
