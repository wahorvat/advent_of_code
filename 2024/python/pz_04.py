import string
import re

with open("../../../aoc_inputs/day 4.txt") as file:
    data = file.read()

def data_to_lists(inp):
    lines = inp.splitlines()
    data_lists = []
    for line in lines:
        data_lists.append([char for char in line])
    return data_lists

def xmas_search(mat):
    """
    Search for all instances of XMAS in all 8 directions:
    - Horizontal (left-to-right and right-to-left)
    - Vertical (top-to-bottom and bottom-to-top)
    - Diagonal (4 directions, both forwards and backwards)
    """
    if not mat or not mat[0]:
        return 0
    
    rows = len(mat)
    cols = len(mat[0])
    target = "XMAS"
    count = 0
    
    # All 8 directions: right, left, down, up, down-right, up-left, down-left, up-right
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]
    
    def check_word(start_row, start_col, dr, dc):
        """Check if XMAS exists starting from (start_row, start_col) in direction (dr, dc)"""
        for i in range(len(target)):
            r = start_row + i * dr
            c = start_col + i * dc
            
            # Check bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            # Check character match
            if mat[r][c] != target[i]:
                return False
        
        return True
    
    # Check every position as a potential starting point
    for row in range(rows):
        for col in range(cols):
            # Try all 8 directions from this position
            for dr, dc in directions:
                if check_word(row, col, dr, dc):
                    count += 1
    
    return count

def answer1(inp):
    search_mat = data_to_lists(inp)
    return xmas_search(search_mat)

ans1 = answer1(data)
print(f"Answer 1: {ans1}")