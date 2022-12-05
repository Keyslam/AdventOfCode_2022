from dataclasses import dataclass
import re


@dataclass
class Step:
    amount: int
    from_stack: int
    to_stack: int


Crate_Stack = list[str]


def parse_crates(crate_amount: int = 9):
    crates: list[Crate_Stack] = list()

    for i in range(0, crate_amount):
        crate_stack = Crate_Stack()
        crates.append(crate_stack)

    for line in open("crates.txt"):
        for i in range(0, crate_amount):
            char_index = i * 4 + 1
            if char_index > len(line):
                continue
            char = line[char_index]
            if not char.isspace():
                crate_stack = crates[i]
                crate_stack.append(char)

    for i in range(0, crate_amount):
        crate_stack = crates[i]
        crate_stack.reverse()

    return crates


def parse_steps():
    steps: list[Step] = list()
    for line in open("steps.txt"):
        matches = re.findall("move (\d+) from (\d+) to (\d+)", line)[0]
        step = Step(
            int(matches[0]),
            int(matches[1]) - 1,
            int(matches[2]) - 1
        )
        steps.append(step)
    return steps


def parse():
    crates = parse_crates()
    steps = parse_steps()
    return crates, steps


def perform_step_9000(crates: list[Crate_Stack], step: Step):
    for i in range(0, step.amount):
        crate = crates[step.from_stack].pop()
        crates[step.to_stack].append(crate)


def perform_steps_9000(crates: list[Crate_Stack], steps: list[Step]):
    for step in steps:
        perform_step_9000(crates, step)


def perform_step_9001(crates: list[Crate_Stack], step: Step):
    from_stack = crates[step.from_stack]
    pick_index = len(from_stack) - step.amount
    for i in range(0, step.amount):
        crate = crates[step.from_stack].pop(pick_index)
        crates[step.to_stack].append(crate)


def perform_steps_9001(crates: list[Crate_Stack], steps: list[Step]):
    for step in steps:
        perform_step_9001(crates, step)


def get_top_string(crates: list[Crate_Stack]):
    result = ""
    for crate_stack in crates:
        char = crate_stack[-1]
        result += char
    return result


def one():
    crates, steps = parse()
    perform_steps_9000(crates, steps)
    result = get_top_string(crates)
    print(result)


def two():
    crates, steps = parse()
    perform_steps_9001(crates, steps)
    result = get_top_string(crates)
    print(result)


if __name__ == '__main__':
    one()
    two()
