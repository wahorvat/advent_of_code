import numpy as np
import string

with open("../../../aoc_inputs/day1/day 1-1.txt") as file:
    data = file.read()

def process_lines(lines):
    left_list = []
    right_list = []

    for line in lines:
        left_val, right_val = map(int, line.split())
        left_list.append(left_val)
        right_list.append(right_val)

    left_list.sort()
    right_list.sort()
    left_array = np.array(left_list)
    right_array = np.array(right_list)

    return left_array, right_array


def answer1(inp):
    lines = inp.splitlines()
    left_array, right_array = process_lines(lines)
    diff_array = abs(left_array - right_array)
    diff_sum = np.sum(diff_array)
    return diff_sum

def answer2(inp):
    lines = inp.splitlines()
    left_array, right_array = process_lines(lines)

    left_unique = np.unique(left_array)
    counter_dict = {}
    for item in left_unique:
        counter_dict[item] = np.count_nonzero(right_array == item)
    
    sum_frequency_prod = 0
    for key in counter_dict.keys():
        sum_frequency_prod += (key * counter_dict[key])

    return sum_frequency_prod


ans1 = answer1(data)
ans2 = answer2(data)

print(ans1, ans2)


