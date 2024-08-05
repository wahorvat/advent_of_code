import math
from dataclasses import dataclass
from typing import NamedTuple
from collections.abc import Generator
import re

with open("./input/input_03.txt") as file:
    data = file.read()

test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

digits = set("1234567890")


def is_symbol(char: str) -> bool:
    return (char != ".") and (char not in digits)


class Coord(NamedTuple):
    row: int
    col: int


@dataclass
class Board:
    syms: dict[Coord, str]
    nums: dict[Coord, int]


def process_data(data: str) -> Board:
    """Convert the string to a Board with syms and nums, coords are complex."""
    syms = {
        Coord(row, col): char
        for row, line in enumerate(data.splitlines())
        for col, char in enumerate(line)
        if is_symbol(char)
    }

    nums = {
        Coord(row, match.span()[0]): int(match.group())
        for row, line in enumerate(data.splitlines())
        for match in re.finditer(r"\d+", line)
    }

    return Board(syms, nums)


def neighbors(loc: Coord, num: int) -> Generator[Coord, None, None]:
    """Return the neighbors of a word."""
    n = len(str(num))
    yield from (Coord(loc.row - 1, loc.col + i) for i in range(-1, n + 1))
    yield from (Coord(loc.row + 1, loc.col + i) for i in range(-1, n + 1))
    yield from (Coord(loc.row, loc.col - 1), Coord(loc.row, loc.col + n))


def part1(data: str) -> int:
    board = process_data(data)
    nums = board.nums
    part_nums = (
        num
        for coord, num in nums.items()
        if any(y in board.syms for y in neighbors(coord, num))
    )
    return sum(part_nums)


def part2(data: str) -> int:
    """Find the gear ratios."""
    board = process_data(data)
    # start with the star symbols
    stars = (coord for coord, sym in board.syms.items() if sym == "*")
    # we need to find the ones with two numbers nearby,
    # let's speed this up a bit by searching in a window around
    # each star, let's figure out the maximum number length we need to worry about.
    max_num_length = max(map(lambda x: len(str(x)), board.nums.values()))

    def nearby_nums(star):
        """Return the nums that are next to a star."""
        for row in range(-1, 2):
            for col in range(-max_num_length, 2):
                coord = Coord(star.row + row, star.col + col)
                if num := board.nums.get(coord):
                    yield coord, num

    # replace each star with a list of the nums they touch
    num_neighbors = (
        [num for coord, num in nearby_nums(star) if star in set(neighbors(coord, num))]
        for star in stars
    )
    # Gears only touch two nums
    gears = filter(lambda x: len(x) == 2, num_neighbors)
    # their gear ratio is the product of the nums
    ratios = (math.prod(nums) for nums in gears)
    return sum(ratios)

print(part1(data), part2(data))
