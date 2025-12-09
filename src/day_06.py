import re
from collections import defaultdict
from math import prod

from utils import no_input_skip, read_input


def part_1(puzzle: str) -> int:
    puzzle = re.sub(r" +", " ", puzzle)
    numbers = defaultdict(list)
    symbols = []
    for line in puzzle.splitlines():
        for i, val in enumerate(line.strip().split(" ")):
            if val in ("*", "+"):
                symbols.append(val)
            else:
                numbers[i].append(int(val))

    total = 0
    for i in range(len(symbols)):
        if symbols[i] == "*":
            total += prod(numbers[i])
        elif symbols[i] == "+":
            total += sum(numbers[i])
    return total


def part_2(puzzle: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """


def test_part_1() -> None:
    test_input = get_example_input()
    assert part_1(test_input) == 4277556


# def test_part_2() -> None:
#     test_input = get_example_input()
#     assert part_2(test_input) is not None


@no_input_skip
def test_part_1_real() -> None:
    real_input = read_input(__file__)
    assert part_1(real_input) == 4771265398012


# @no_input_skip
# def test_part_2_real() -> None:
#     real_input = read_input(__file__)
#     assert part_2(real_input) is not None


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
