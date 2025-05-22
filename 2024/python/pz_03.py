import string
import re

with open("../../../aoc_inputs/day 3.txt") as file:
    data = file.read()

def mul_finder(lines):
    valid_muls = []
    for line in lines:
        # Pattern: mul followed by open parenthesis, then digits, comma, digits, and close parenthesis
        pattern = r'mul\((\d+),(\d+)\)'
        matches = re.findall(pattern, line)
        valid_muls.extend(matches)
    
    return valid_muls

def answer1(inp):
    lines = inp.splitlines()
    muls = mul_finder(lines)
    mul_sum = 0
    
    for mul in muls:
        num1_str, num2_str = mul
        num1 = int(num1_str)
        num2 = int(num2_str)
        mul_sum += num1 * num2
    
    return mul_sum



ans1 = answer1(data)
print(f"Answer 1: {ans1}")