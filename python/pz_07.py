from collections import Counter

with open('./input/input_07.txt') as file:
    data_string = file.read()

test_string = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


type Hand = tuple[int]
type Bid = int

card_to_num = {val: i + 2 for i, val in enumerate("23456789TJQKA")}

def process_line(s: str) -> tuple[Hand, Bid]:
    """convert symbolic hands to numerics and package with bid"""
    hand_str, bid_str = s.split()
    numeric_hand = map(lambda x: card_to_num[x], hand_str)
    return tuple(numeric_hand), int(bid_str)


def process(s: str) -> list[tuple[Hand, Bid]]:
    """Split input string by \n and process each hand with process_line"""
    return list(map(process_line, s.splitlines()))


hand_score = {
    (): 10,
    (5, ): 10,
    (1, 4): 9,
    (2, 3): 8,
    (1, 1, 3): 7,
    (1, 2, 2): 6,
    (1, 1, 1, 2): 5,
    (1, 1, 1, 1, 1): 4,
}

def hand_grouping(hand: Hand) -> int:
    """Group singles, pairs, three-of-a-kind, ... with Counter to map with hand_score dict"""
    grouped = tuple(sorted(Counter(hand).values()))
    return hand_score[grouped]


def answer1(input) -> int:
    data = process(input)
    ranked = sorted((hand_grouping(hand), hand, bid) for (hand, bid) in data)
    winnings = sum(bid * (idx + 1) for (idx, (_, _, bid)) in enumerate(ranked))
    return winnings

"""
Part 2
------//-------
"""

def set_joker(hand: Hand) -> Hand:
    """Give all Js numeric value 0"""
    return tuple(0 if card == card_to_num["J"] else card for card in hand)


def joker_to_value(hand: Hand) -> Hand:
    """Replace joker by previous most common value"""
    valid_cards = filter(lambda card: card > 0, hand)
    most_common_card = (Counter(valid_cards).most_common(1) or [(0, 0)])[0][0]
    joker_replaced = tuple(most_common_card if card == 0 else card for card in hand)
    return joker_replaced


def answer2(input) -> int:
    data = process(input)
    jokered = ((set_joker(hand), bid) for (hand, bid) in data)
    ranked = sorted((hand_grouping(joker_to_value(hand)), hand, bid) for (hand, bid) in jokered)
    winnings = sum(bid * (idx + 1) for (idx, (_, _, bid)) in enumerate(ranked))
    return winnings

print(answer2(data_string))
