from dataclasses import dataclass
import itertools


def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


@dataclass
class Rucksack:
    left: set
    right: set
    total: set


def parse():
    rucksacks = []

    for line in open("input.txt", "r"):
        line = line.strip()
        left = line[slice(0, len(line)//2)]
        right = line[slice(len(line) // 2, len(line))]
        total = line
        rucksack = Rucksack(set(left), set(right), set(total))
        rucksacks.append(rucksack)

    return rucksacks


def get_item_type_priority(item_type: str):
    if item_type.isupper():
        return ord(item_type) - 38
    else:
        return ord(item_type) - 96


def get_overlap(rucksack):
    return list(rucksack.left & rucksack.right)[0]


def get_overlap_in_group(a, b, c):
    return list(a.total & b.total & c.total)[0]


def calculate_total_priority(item_types):
    return sum(map(lambda x: get_item_type_priority(x), item_types))


def one():
    overlaps = []

    for rucksack in parse():
        overlaps.append(get_overlap(rucksack))

    total_item_priority = calculate_total_priority(overlaps)
    print(total_item_priority)


def two():
    overlaps = []

    for group in chunked_iterable(parse(), size=3):
        overlap = get_overlap_in_group(group[0], group[1], group[2])
        overlaps.append(overlap)

    total_item_priority = calculate_total_priority(overlaps)
    print(total_item_priority)


if __name__ == '__main__':
    one()
    two()
