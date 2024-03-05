import itertools

FILENAME = "./input/input_14.txt"
ROUNDED = "O"
SQUARED = "#"
CYCLE_COUNT = 1_000_000_000


def transpose(matrix: tuple[str, ...]) -> tuple[str, ...]:
    return tuple("".join(row) for row in zip(*matrix))


def tilt_row(row: str, reverse_sort: bool) -> str:
    return SQUARED.join(
        "".join(sorted(fragment, reverse=reverse_sort))
        for fragment in row.split(SQUARED)
    )


def tilt_matrix(matrix: tuple[str, ...], reverse_sort: bool) -> tuple[str, ...]:
    return tuple(tilt_row(row, reverse_sort) for row in matrix)


def calculate_load(matrix: tuple[str, ...]) -> int:
    return sum(
        sum(len(row) - i for i, char in enumerate(row) if char == ROUNDED)
        for row in matrix
    )


def perform_cycle(matrix: tuple[str, ...]) -> tuple[str, ...]:
    for reverse_sort in [True, True, False, False]:
        matrix = transpose(matrix)
        matrix = tilt_matrix(matrix, reverse_sort)
    return matrix


def find_key_by_value(dictionary: dict, value: int, default=None) -> tuple[str]:
    return next((key for key, val in dictionary.items() if val == value), default)


def perform_cycles(matrix: tuple[str, ...]):
    memo = {}
    for counter in itertools.count(1):
        matrix = perform_cycle(matrix)
        if matrix in memo:
            second_appearance, first_appearance = counter, memo[matrix]
            cycle_range = second_appearance - first_appearance
            index = (CYCLE_COUNT - first_appearance) % cycle_range + first_appearance
            return transpose(find_key_by_value(memo, index))
        memo[matrix] = counter


def main():
    with open(FILENAME) as f:
        matrix = tuple(f.read().split("\n"))

    tilted_part_one = tilt_matrix(transpose(matrix), True)
    print(calculate_load(tilted_part_one))

    tilted_part_two = perform_cycles(matrix)
    print(calculate_load(tilted_part_two))


if __name__ == "__main__":
    main()
