import string
import parse
import math
from collections.abc import Iterator

with open("./input/input_02.txt") as file:
    data = file.read()
lines = data.splitlines()

type Line_Maxes = dict[str, int]

def find_color(line: str, color: str) -> Iterator[int]:
    return (match["num"] for match in parse.findall(f"{{num:d}} {color}", line))

def line_maxes(line: str) -> Line_Maxes:
   return {color: max(find_color(line, color)) for color in ("red", "green", "blue")}

def game_num(line: str) -> int:
    return parse.search("Game {game_num:d}", line)["game_num"]

result1 = 0
for line in lines:
    maxes = line_maxes(line)
    game_val = game_num(line)
    if (maxes['red'] > 12 or maxes['green'] > 13 or maxes['blue'] > 14):
        continue
    else:
        result1 += game_val


def set_power(maxes: dict) -> int:
    return math.prod(maxes.values())

result2 = 0
for line in lines:
    maxes = line_maxes(line)
    prod = set_power(maxes)
    result2 += prod

print(result1, result2)