with open('3.input.txt') as f:
    lines = f.readlines()

lines = [x.replace("\n", "") for x in lines]


counter = [0] * len(lines[0])

for line in lines:
    for i in range(0, len(line)):
        counter[i] += int(line[i])

counter = [x/len(lines) for x in counter]

gamma_rate = ["1" if x >= 0.5 else "0" for x in counter]

beta_rate = ["0" if x >= 0.5 else "1" for x in counter]

gamma_rate = "".join(gamma_rate)
beta_rate = "".join(beta_rate)

g = int(gamma_rate, 2)
b = int(beta_rate, 2)

print(g * b)
