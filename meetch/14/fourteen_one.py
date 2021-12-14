from collections import Counter

if __name__ == "__main__":

    with open('input.txt') as f:
        lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

    template = lines[0]
    rules = lines[2:]

    rule_dict = {}
    for item in rules:
        left, right = item.split(" -> ")
        rule_dict[left] = right

    new_word = ""
    for _ in range(10):
        new_letters = []
        for i in range(len(template)-1):
            pair = "".join([template[i], template[i+1]])
            new_letters.append(rule_dict[pair])
        new_word = list(template) + list(new_letters)
        new_word[::2] = list(template)
        new_word[1::2] = list(new_letters)
        new_word = ("").join(new_word)
        template = new_word

    counter_dict = Counter(list(template))
    max_value = max(counter_dict.values())
    min_value = min(counter_dict.values())

    print(max_value - min_value)
