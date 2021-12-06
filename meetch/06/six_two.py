class School:
    def __init__(self):
        self.school = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    def add_fish(self, timer, number):
        self.school[timer] += number
    
    def pass_day(self):
        reproducing_fish = self.school[0]
        for i in range(1, 9):
            self.school[i-1] = self.school[i]
        self.school[6] += reproducing_fish
        self.school[8] = reproducing_fish


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[0].split(",")))

    fish_count = [numbers.count(i) for i in range(0, 6)]

    school = School()

    for i in range(len(fish_count)):
        school.add_fish(i, fish_count[i])

    for _ in range(256):
        school.pass_day()

    print(school.school)
    print(sum(school.school.values()))