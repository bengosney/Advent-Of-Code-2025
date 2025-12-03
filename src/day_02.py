from utils import no_input_skip, read_input


def part_1(puzzle: str) -> int:
    total = 0
    for pair in puzzle.split(","):
        lower, upper = map(int, pair.split("-"))
        for id in (str(i) for i in range(lower, upper + 1)):
            halfway = len(id) // 2
            if id[:halfway] == id[halfway:]:
                total += int(id)

    return total


def part_2(puzzle: str) -> int:
    pass


# -- Tests


def get_example_input() -> str:
    return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""  # noqa: E501


def test_part_1() -> None:
    test_input = get_example_input()
    assert part_1(test_input) == 1227775554


# def test_part_2() -> None:
#     test_input = get_example_input()
#     assert part_2(test_input) is not None


@no_input_skip
def test_part_1_real() -> None:
    real_input = read_input(__file__)
    assert part_1(real_input) == 44854383294


# @no_input_skip
# def test_part_2_real() -> None:
#     real_input = read_input(__file__)
#     assert part_2(real_input) is not None


# -- Main

if __name__ == "__main__":
    real_input = read_input(__file__)

    print(f"Part1: {part_1(real_input)}")
    print(f"Part2: {part_2(real_input)}")
