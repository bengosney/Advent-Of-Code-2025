from utils import no_input_skip, read_input


def part_1(puzzle: str) -> int:
    raw_ranges, ids = puzzle.split("\n\n")
    ingredient_ranges: list[range] = []

    for r in raw_ranges.splitlines():
        l, h = map(int, r.split("-"))
        ingredient_ranges.append(range(l, h + 1))

    total = 0
    for id in map(int, ids.splitlines()):
        for ingredient_range in ingredient_ranges:
            if id in ingredient_range:
                total += 1
                break

    return total


def part_2(puzzle: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part_1() -> None:
    test_input = get_example_input()
    assert part_1(test_input) == 3


# def test_part_2() -> None:
#     test_input = get_example_input()
#     assert part_2(test_input) is not None


@no_input_skip
def test_part_1_real() -> None:
    real_input = read_input(__file__)
    assert part_1(real_input) == 756


# @no_input_skip
# def test_part_2_real() -> None:
#     real_input = read_input(__file__)
#     assert part_2(real_input) is not None


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
