with open('3.input.txt') as f:
    lines = f.readlines()

lines = [x.replace("\n", "") for x in lines]
for i in range(len(lines[0])):
    counter = 0
    for line in lines:
        counter += int(line[i])
    most_common = counter/len(lines)
    if most_common >= 0.5:
        most_common = "1"
    else:
        most_common = "0"

    kept = []
    for line in lines:
        if line[i] == most_common:
            kept.append(line)

    lines = kept[:]
o_g_rating = lines[0]
print(o_g_rating)


with open('3.input.txt') as f:
    lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]
for i in range(len(lines[0])):
    if len(lines) == 1:
        break
    counter = 0
    for line in lines:
        counter += int(line[i])
    least_common = counter/len(lines)
    if least_common < 0.5:
        least_common = "1"
    else:
        least_common = "0"

    kept = []
    for line in lines:
        if line[i] == least_common:
            kept.append(line)
    lines = kept[:]
c_s_rating = lines[0]
print(c_s_rating)


o = int(o_g_rating, 2)
c = int(c_s_rating, 2)

print(o * c)
