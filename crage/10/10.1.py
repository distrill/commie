pointTable = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def getBadParenthesesScore(filename: str):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        stack: list[str] = []
        points: list[int] = []
        for line in lines:
            for char in line:
                if char == ')':
                    val = stack.pop()
                    if val != '(': 
                        points.append(pointTable[char])
                elif char == ']':
                    val = stack.pop()
                    if val != '[': 
                        points.append(pointTable[char])
                elif char == '}':
                    val = stack.pop()
                    if val != '{': 
                        points.append(pointTable[char])
                elif char == '>':
                    val = stack.pop()
                    if val != '<': 
                        points.append(pointTable[char])
                elif char == '(' or char == '[' or char == '{' or char == '<':
                    stack.append(char)
            stack = []
        return sum(points)

print(getBadParenthesesScore('./crage/10/input.txt'))
