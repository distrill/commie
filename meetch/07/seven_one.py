
if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    pos = [int(x) for x in lines[0].split(",")]

    fuel_costs = [0] * max(pos)

    for i in range(len(fuel_costs)):
        fuel_cost = 0
        for p in pos:
            fuel_cost += abs(p - i)
        fuel_costs[i] = fuel_cost
    print(min(fuel_costs))
