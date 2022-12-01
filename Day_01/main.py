def parse():
    elves = []
    inventory = []

    for line in open("input.txt", "r"):
        if line == "\n":
            elves.append(inventory)
            inventory = []
        else:
            calories = int(line)
            inventory.append(calories)
    if len(inventory) != 0:
        elves.append(inventory)

    return elves


def get_elves_total_calories_descending():
    elves = parse()
    elves_total_calories = []

    for elf in elves:
        total_calories = sum(elf)
        elves_total_calories.append(total_calories)
    elves_total_calories.sort(reverse=True)

    return elves_total_calories


def one():
    elves_total_calories_descending = get_elves_total_calories_descending()
    print(elves_total_calories_descending[0])


def two():
    elves_total_calories_descending = get_elves_total_calories_descending()
    print(sum(elves_total_calories_descending[0:3]))


if __name__ == '__main__':
    one()
    two()
