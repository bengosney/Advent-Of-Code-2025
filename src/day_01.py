from collections import deque

from utils import no_input_skip, read_input


def part_1(puzzle: str) -> int:
    dial = deque(range(100))
    dial.rotate(50)

    zeros = 0
    for line in puzzle.splitlines():
        turn = line[0]
        steps = int(line[1:])
        if turn == "L":
            dial.rotate(steps)
        elif turn == "R":
            dial.rotate(-steps)

        zeros += int(dial[0] == 0)
    return zeros


def part_2(puzzle: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_part_1() -> None:
    test_input = get_example_input()
    assert part_1(test_input) == 3


# def test_part_2() -> None:
#     test_input = get_example_input()
#     assert part_2(test_input) is not None


@no_input_skip
def test_part_1_real() -> None:
    real_input = read_input(__file__)
    assert part_1(real_input) == 1150


# @no_input_skip
# def test_part_2_real() -> None:
#     real_input = read_input(__file__)
#     assert part_2(real_input) is not None


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
