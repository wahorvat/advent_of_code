import string

with open("../../../aoc_inputs/day 2.txt") as file:
    data = file.read()


def process_lines(line):
    line_list = [int(num) for num in line.split()]
    return line_list


def safe_monotone(nums):
    if len(nums) < 2:
        return 0
    
    safe = 0
    idx = 0
    
    if (nums[idx] > nums[idx + 1]) and (nums[idx] - nums[idx + 1] < 4):
        while idx < (len(nums) - 1):
            if idx + 1 < len(nums) and nums[idx] > nums[idx + 1] and (nums[idx] - nums[idx + 1] < 4):
                idx += 1
            else:
                return safe
        safe = 1
    elif (nums[idx] < nums[idx + 1]) and (nums[idx + 1] - nums[idx] < 4):
        while idx < (len(nums) - 1):
            if idx + 1 < len(nums) and nums[idx] < nums[idx + 1] and (nums[idx + 1] - nums[idx] < 4):
                idx += 1
            else:
                return safe
        safe = 1
    
    return safe

def safe_monotone_with_jump(nums):
    if len(nums) < 2:
        return 0
    
    if is_safe_sequence(nums, True) or is_safe_sequence(nums, False):
        return 1
    
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        if len(new_nums) >= 2 and (is_safe_sequence(new_nums, True) or is_safe_sequence(new_nums, False)):
            return 1
    
    return 0

def is_safe_sequence(nums, decreasing):
    if len(nums) < 2:
        return False
    
    for i in range(len(nums) - 1):
        if decreasing and nums[i] <= nums[i+1]:
            return False
        if not decreasing and nums[i] >= nums[i+1]:
            return False
    
        diff = abs(nums[i] - nums[i+1])
        if diff < 1 or diff > 3:
            return False
    
    return True



def answer1(inp):
    lines = inp.splitlines()
    safe_lines = 0
    for line in lines:
        line_list = process_lines(line)
        if line_list:
            safe_lines += safe_monotone(line_list)
    return safe_lines


def answer2(inp):
    lines = inp.splitlines()
    safe_lines = 0
    for line in lines:
        line_list = process_lines(line)
        if line_list:
            safe_lines += safe_monotone_with_jump(line_list)
    return safe_lines


ans1 = answer1(data)
ans2 = answer2(data)
print(f"Answer 1: {ans1}")
print(f"Answer 2: {ans2}")



