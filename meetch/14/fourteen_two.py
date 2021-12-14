from collections import Counter
from collections import defaultdict

if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

    template = lines[0]
    rules = lines[2:]

    rule_dict = {}
    poly_dict = {}
    step_dict = {}
    for item in rules:
        left, right = item.split(" -> ")
        rule_dict[left] = right
        poly_dict[left] = 0
        step_dict[left] = 0

    character_counter = defaultdict(int)
    for i in range(len(template)-1):
        pair = ("").join([template[i], template[i+1]])
        poly_dict[pair] += 1
        character_counter[template[i]] += 1
    character_counter[template[i+1]] += 1

    for _ in range(40):
        step_dict = dict.fromkeys(step_dict, 0)
        for key, value in poly_dict.items():
            new_value = rule_dict[key]
            left_split = ("").join([key[0], new_value])
            right_split = ("").join([new_value, key[1]])
            character_counter[new_value] += value
            step_dict[left_split] += value
            step_dict[right_split] += value
        poly_dict = step_dict

    print(max(character_counter.values()) - min(character_counter.values()))
