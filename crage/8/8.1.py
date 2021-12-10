def decodeNumbers(filename: str):
    with open(filename, 'r') as file:
        numberLines: list[list[int]] = [line.split("|")[1].strip().split(" ")  for line in file.readlines()]
        validNumbers = set([2, 3, 4, 7])
        return sum(len([*filter(lambda x: x, [True if len(stringNumber) in validNumbers else False for stringNumber in numberLine])]) for numberLine in numberLines)
print(decodeNumbers('./crage/8/input.txt'))
