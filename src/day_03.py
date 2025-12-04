from utils import no_input_skip, read_input


def part_1(puzzle: str) -> int:
    total = 0
    for line in puzzle.splitlines():
        battries = [int(x) for x in line.strip()]
        first = max(battries[:-1])
        second = max(battries[battries.index(first) + 1 :])
        total += int(f"{first}{second}")

    return total


def part_2(puzzle: str) -> int:
    total = 0
    for line in puzzle.splitlines():
        battries = [int(x) for x in line.strip()]
        battries.append(0)  # [:-0] causes issues in python slicing
        jolts = []

        idx = 0
        while len(jolts) < 12:
            offset = 12 - len(jolts)
            try:
                current = max(battries[idx:-offset])
            except ValueError:
                break
            idx = battries.index(current, idx) + 1
            jolts.append(current)

        total += int("".join(map(str, jolts)))

    return total


# -- Tests


def get_example_input() -> str:
    return """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part_1() -> None:
    test_input = get_example_input()
    assert part_1(test_input) == 357


def test_part_2() -> None:
    test_input = get_example_input()
    assert part_2(test_input) == 3121910778619


@no_input_skip
def test_part_1_real() -> None:
    real_input = read_input(__file__)
    assert part_1(real_input) == 17432


@no_input_skip
def test_part_2_real() -> None:
    real_input = read_input(__file__)
    assert part_2(real_input) == 173065202451341


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
