# 2.1

def clean_lines(x):
    x = x.replace("\n", "")
    x = x.split(" ")
    x[1] = int(x[1])
    return x

with open('2.1.input.txt') as f:
    lines = f.readlines()

directions = [clean_lines(x) for x in lines]

horiz = 0
vert = 0
aim = 0

for dir in directions:
    if dir[0] == "forward":
        horiz += dir[1]
        vert += (aim * dir[1])
    elif dir[0] == "up":
        aim -= dir[1]
    else:
        aim += dir[1]

print(horiz, vert)
print(horiz * vert)
