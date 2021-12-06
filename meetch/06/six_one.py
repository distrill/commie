class Fish:
    def __init__(self, timer=8):
        self.timer = timer
    def pass_day(self):
        self.timer -= 1
        if self.timer == -1:
            self.timer = 6
            return True
        return False


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    numbers = map(int, lines[0].split(","))

    fishes = [Fish(x) for x in numbers]

    for i in range(80):
        new_fish_counter = 0
        for fish in fishes:
            if fish.pass_day():
                new_fish_counter += 1
        new_fishes = [Fish() for _ in range(new_fish_counter)]
        fishes = fishes + new_fishes
    
    print(len(fishes))
            