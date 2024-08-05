import re

with open("./input/input_04.txt") as file:
    data = file.read()

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def card_to_list(s: str) -> list:
    """Remove game id and convert string to ints"""
    winning_list = []
    card_list = []
    for line in s.splitlines():
        if match := re.match(r"Card\s+(\d+): ([ \d]+)\|([ \d]+)", line):
            groups = match.groups()
            winning_list.append(map(int, groups[1].split()))
            card_list.append(map(int, groups[2].split()))
    return winning_list, card_list



def set_generate_intersect(winners: list[int], card: list[int]) -> list:
    intersections = []
    for idx in range(len(winners)):
        winners_set = set(winners[idx])
        card_set = set(card[idx])
        intersections.append(len(winners_set.intersection(card_set)))
    return intersections



def points(intersect: list[int]) -> int:
    points = []
    for val in intersect:
        if val > 0:
            points.append(2 ** (val - 1))
        else:
            points.append(0)
    return points


def answer1(data: str) -> int:
    winners, yours = card_to_list(data)
    intersections = set_generate_intersect(winners, yours)
    return sum(points(intersections))



assert answer1(test_data) == 13

#print(answer1(data))



def multiplicity(matches: list[int]) -> list:
    multiplicity = [1] * len(matches)
    for i, val in enumerate(matches):
        for j in range(i + 1, i + 1 + val):
            multiplicity[j] += multiplicity[i]
    return multiplicity 



def answer2(data: str) -> int:
    winners, yours = card_to_list(data)
    intersections = set_generate_intersect(winners, yours)
    point_array = points(intersections)
    print(point_array)
    multiplicity_array = multiplicity(intersections)
    return sum(multiplicity_array)

assert answer2(test_data) == 30

print(answer2(data))