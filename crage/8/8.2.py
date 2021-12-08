def initializeValues(patternStrings: list[str]) -> dict[frozenset[str], int]:
    values: dict[int, set[str]] = {}
    for patternString in patternStrings:
        if len(patternString) == 2:
            values[1] = set(patternString)
        elif len(patternString) == 3:
            values[7] = set(patternString)
        elif len(patternString) == 4:
            values[4] = set(patternString)
        elif len(patternString) == 7:
            values[8] = set(patternString)
    for patternString in patternStrings:
        if len(patternString) == 5:
            # 2, 3, 5
            if len(set(patternString) - values[1]) == 3:
                values[3] = set(patternString)
            elif len(set(patternString) - values[4]) == 3:
                values[2] = set(patternString)
            elif len(set(patternString) - values[4]) == 2:
                values[5] = set(patternString)
    middleBarSet = (values[3] - values[7]).intersection(values[4])
    middleBarLetter = middleBarSet.pop()
    middleBarSet.add(middleBarLetter)
    for patternString in patternStrings:
        if len(patternString) == 6:
            # 0, 6, 9
            if (values[8] - set(patternString)).pop() == middleBarLetter:
                values[0] = set(patternString)
            elif len(set(patternString) - values[1] - middleBarSet) == 3:
                values[9] = set(patternString)
            elif len(set(patternString) - values[4] - middleBarSet) == 3:
                values[6] = set(patternString)
                
        
    return {frozenset(patternString):amount for amount, patternString in values.items()}

def decodeNumbers(filename: str):
    with open(filename, 'r') as file:
        patternOutputs: list[list[str]] = [line.split("|") for line in file.readlines()]
        numbers: list[int] = []
        for pattern, output in patternOutputs:
            patternStrings = pattern.strip().split(" ")
            values = initializeValues(patternStrings)
            outputStrings = output.strip().split(" ")
            current = ""
            for outputString in outputStrings:
                current = f"{current}{values[frozenset(outputString)]}"
            numbers.append(int(current))
        return sum(numbers)

print(decodeNumbers('./crage/8/input.txt'))
