import math

with open('./input/input_08.txt') as file:
    data_string = file.read()


test_string = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

right_left_to_idx = {'L': 0, 'R': 1}

def process(input: str) -> dict:
    lines = input.splitlines()
    directions = list(right_left_to_idx[inst] for inst in lines[0])
    ins_outs = list(mapping.split(' = ') for mapping in lines[2:])
    return directions, ins_outs


def dict_form(ins_outs: list[str]):
    dict = {}
    for mapping in ins_outs:
        dict[mapping[0]] = mapping[1][1:9].split(', ')
    return dict

def traverse(direct: dict, mapping: dict):
    position = 'AAA'
    idx = 0
    steps = 0
    while position != 'ZZZ':
        position = mapping[position][direct[idx]]
        steps += 1
        if idx < len(direct) - 1:
            idx += 1
        else:
            idx = 0
    return steps

def traverse2(direct: dict, mapping: dict):
    keys = mapping.keys()
    positions = [key for key in keys if key[2] == 'A']
    idx = 0
    steps = [0] * len(positions)
    for i, position in enumerate(positions):
        while position[-1] != 'Z':
            position = mapping[position][direct[idx]]
            steps[i] += 1
            if idx < len(direct) - 1:
                idx += 1
            else:
                idx = 0
    return steps

left_right, test_data = process(data_string)
dict_mapping = dict_form(test_data)
test = traverse2(left_right, dict_mapping)
common_path = math.lcm(*test)

print(common_path)

