
def is_in_set(n):
    numbers_to_count = set([2, 4, 3, 7])
    if n in numbers_to_count:
        return 1
    else:
        return 0

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.replace("\n", "") for x in lines]
    lines = [x.split(" | ") for x in lines]

    number_counts = 0
    for line in lines:
        output = line[1].split(" ")
        output_lens = [*map(len, output)]
        counts = [*map(is_in_set, output_lens)]
        number_counts += sum(counts)
    print(number_counts)
        

    
