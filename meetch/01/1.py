# from 1.1.py
with open('1.1.input.txt') as f:
    lines = f.readlines()


inputs = [int(x.replace("\n", "")) for x in lines]

counter = 0
i = 0
while i < (len(inputs)-1):
    i += 1
    if inputs[i] > inputs[i-1]:
        counter += 1
print(counter)


# from 1.2.py
with open('1.1.input.txt') as f:
    lines = f.readlines()


inputs = [int(x.replace("\n", "")) for x in lines]

counter = 0
i = 0
while i < (len(inputs)-3):

    j = i + 1
    windowB = inputs[j] + inputs[j+1] + inputs[j+2]
    windowA = inputs[i] + inputs[i+1] + inputs[i+2]
    i += 1
    if windowB > windowA:
        counter += 1

print(counter)
