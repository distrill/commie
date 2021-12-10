import functools

pointTable = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def getBadParenthesesScore(filename: str):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        stack: list[str] = []
        points: list[int] = []
        isCorrupted = False
        for line in lines:
            for char in line:
                if not isCorrupted:
                    if char == ')':
                        val = stack.pop()
                        if val != '(':
                            isCorrupted = True
                    elif char == ']':
                        val = stack.pop()
                        if val != '[':
                            isCorrupted = True
                    elif char == '}':
                        val = stack.pop()
                        if val != '{':
                            isCorrupted = True
                    elif char == '>':
                        val = stack.pop()
                        if val != '<':
                            isCorrupted = True
                    elif char == '(' or char == '[' or char == '{' or char == '<':
                        stack.append(char)
            if not isCorrupted:
                stack.reverse()
                points.append(functools.reduce(lambda total, char: total * 5 + pointTable[char] , stack, 0))
            isCorrupted = False
            stack = []
        return sorted(points)[(len(points) / 2).__floor__()]

print(getBadParenthesesScore('./crage/10/input.txt'))
