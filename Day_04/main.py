from dataclasses import dataclass
import re


@dataclass
class Elf:
    left: int
    right: int


@dataclass
class Pair:
    a: Elf
    b: Elf


def parse():
    pairs: list[Pair] = []

    for line in open("input.txt"):
        matches = re.findall("\d+", line)
        matches = list(map(int, matches))

        pair = Pair(
            Elf(matches[0], matches[1]),
            Elf(matches[2], matches[3])
        )

        pairs.append(pair)

    return pairs


def does_elf_contain_elf(a: Elf, b: Elf):
    return a.left >= b.left and a.right <= b.right


def does_pair_have_containment(pair: Pair):
    return does_elf_contain_elf(pair.a, pair.b) or does_elf_contain_elf(pair.b, pair.a)


def does_elf_overlap_elf(a: Elf, b: Elf):
    return a.left >= b.left and not a.left > b.right


def does_pair_have_overlap(pair: Pair):
    return does_elf_overlap_elf(pair.a, pair.b) or does_elf_overlap_elf(pair.b, pair.a)


def one():
    containment = sum(map(lambda pair: 1 if does_pair_have_containment(pair) else 0, parse()))
    print(containment)


def two():
    overlaps = sum(map(lambda pair: 1 if does_pair_have_overlap(pair) else 0, parse()))
    print(overlaps)


if __name__ == '__main__':
    one()
    two()
