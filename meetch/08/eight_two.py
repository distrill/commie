import numpy as np


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.replace("\n", "") for x in lines]
    lines = [x.split(" | ") for x in lines]
    total = 0
    for line in lines:
        output = line[1].split(" ")
        input = line[0].split(" ")

        print(input)

        input_lens = [*map(len, input)]

        print(input_lens)

        # find seven
        seven = input[input_lens.index(3)]
        # find one
        one = input[input_lens.index(2)]
        # find four
        four = input[input_lens.index(4)]
        # find eight
        eight = input[input_lens.index(7)]
        # find six
        for idx in [i for i, val in enumerate(input_lens) if val == 6]:
            if len(list((set(input[idx]) - set(one)))) == 5:
                six = input[idx]
        # find three
        for idx in [i for i, val in enumerate(input_lens) if val == 5]:
            if len(list((set(input[idx]) - set(one)))) == 3:
                three = input[idx]
        # find nine
        nine = "".join(list(set(four).union(set(three))))
        # find two
        for idx in [i for i, val in enumerate(input_lens) if val == 5]:
            if len(list((set(input[idx]).union(set(four))))) == 7:
                two = input[idx]
        # find five
        for idx in [i for i, val in enumerate(input_lens) if val == 5]:
            if len(list((set(input[idx]) - (set(two))))) == 2:
                five = input[idx]
        # find zero
        for idx in [i for i, val in enumerate(input_lens) if val == 6]:
            if (sorted(input[idx]) != sorted(nine)) and (sorted(input[idx]) != sorted(six)):
                zero = input[idx]

        # was this even necessary??
        a = list(set(seven) - set(one))[0]
        b = list(set(nine) - set(three))[0]
        c = list(set(one) - set(six))[0]
        d = list(set(eight) - set(zero))[0]
        e = list(set(eight) - set(nine))[0]
        g = list(set(nine) - set(seven).union(set(four)))[0]
        all_letters = ["a", "b", "c", "d", "e", "f", "g"]
        for letter in all_letters:
            if letter not in set([a, b, c, d, e, g]):
                f = letter

        all_decodes = [one, two, three, four,
                       five, six, seven, eight, nine, zero]
        decode_lookup = {one: "1", two: "2", three: "3", four: "4",
                         five: "5", six: "6", seven: "7", eight: "8", nine: "9", zero: "0"}
        all_letters = []
        decoded_output = []
        for code in output:
            for f in all_decodes:
                if set(code) == set(f):
                    decoded_output.append(decode_lookup[f])
        total += int("".join(decoded_output))
    print(total)
