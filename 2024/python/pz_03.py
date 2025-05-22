import string
import re

with open("../../../aoc_inputs/day 3.txt") as file:
    data = file.read()


def answer1(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    matches = re.findall(pattern, text)
    total = 0
    
    for x, y in matches:
        result = int(x) * int(y)
        total += result
    
    return total


def answer2(text):
    # Pattern to match mul(X,Y), do(), or don't()
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    
    matches = re.findall(pattern, text)
    total = 0
    enabled = True
    
    for match in matches:
        instruction = match[0]
        
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul(") and enabled:
            x, y = int(match[1]), int(match[2])
            result = x * y
            total += result
    
    return total


ans1 = answer1(data)
print(f"Answer 1: {ans1}")

ans2 = answer2(data)  
print(f"Answer 2: {ans2}")