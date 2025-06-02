with open("../../../aoc_inputs/day 6.txt") as file:
    data = file.read()
 
def input_to_matrix(text):
    grid = []
    for line in text.strip().split('\n'):  # Split into actual lines
        list_line = list(line)
        grid.append(list_line)
    return grid

def find_caret(grid):
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            if char == '^':
                return (row_idx, col_idx)
    return None


def count_guard_positions(grid):
    """
    Count positions visited by guard during patrol.
    Returns the number of distinct positions visited (including start).
    """
    # Find starting position
    start_pos = find_caret(grid)
    if not start_pos:
        return 0
    
    # Direction vectors: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_idx = 0  # Start facing up
    
    row, col = start_pos
    visited = set()
    visited.add((row, col))
    
    # Track states to detect infinite loops
    states = set()
    
    while True:
        current_state = (row, col, direction_idx)
        if current_state in states:
            # Infinite loop detected - guard won't leave
            break
        states.add(current_state)
        
        # Calculate next position
        dr, dc = directions[direction_idx]
        next_row, next_col = row + dr, col + dc
        
        # Check if next position is out of bounds
        if (next_row < 0 or next_row >= len(grid) or 
            next_col < 0 or next_col >= len(grid[0])):
            break
        
        # Check if next position is an obstacle
        if grid[next_row][next_col] == '#':
            # Turn right 90 degrees
            direction_idx = (direction_idx + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col
            visited.add((row, col))
    
    return len(visited)

def answer1(inp):
    puzzle_grid = input_to_matrix(inp)
    path_length = count_guard_positions(puzzle_grid)
    return path_length

ans1 = answer1(data)
print(f"Answer 1: {ans1}")