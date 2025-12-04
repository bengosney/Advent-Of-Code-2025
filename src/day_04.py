from collections import defaultdict

from utils import no_input_skip, read_input


def draw_grid(grid: dict[tuple[int, int], str]) -> None:
    min_x = min(x for x, y in grid.keys())
    max_x = max(x for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += grid[(x, y)]
        print(row)


def part_1(puzzle: str) -> int:
    grid = defaultdict(lambda: ".")

    for y, line in enumerate(puzzle.splitlines()):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = char

    max_x = max(x for x, _ in grid.keys())
    max_y = max(y for _, y in grid.keys())
    total = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if grid[(x, y)] == "@":
                adjacent = [
                    grid[(x, y + 1)],
                    grid[(x, y - 1)],
                    grid[(x + 1, y)],
                    grid[(x - 1, y)],
                    grid[(x - 1, y + 1)],
                    grid[(x - 1, y - 1)],
                    grid[(x + 1, y + 1)],
                    grid[(x + 1, y - 1)],
                ]
                if adjacent.count("@") < 4:
                    total += 1

    return total


def part_2(puzzle: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_part_1() -> None:
    test_input = get_example_input()
    assert part_1(test_input) == 13


# def test_part_2() -> None:
#     test_input = get_example_input()
#     assert part_2(test_input) is not None


@no_input_skip
def test_part_1_real() -> None:
    real_input = read_input(__file__)
    assert part_1(real_input) == 1587


# @no_input_skip
# def test_part_2_real() -> None:
#     real_input = read_input(__file__)
#     assert part_2(real_input) is not None


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
