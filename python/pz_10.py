"""NEED TO CLEAN UP"""

with open('./input/input_10.txt') as file:
    data_string = file.read()

test_string = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

# Direction options to each piece 
direction_dict = {
    '|': ['n', 's'], # north and south
    '-': ['e', 'w'], # east and west
    'L': ['n', 'e'], # north and east
    'J': ['n', 'w'], # north and west
    '7': ['s', 'w'], # south and west
    'F': ['s', 'e'], # south and east
    '.': []  # nothing
}

"""Opposite direction of movement to match pipe opening"""
opposite_directs = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

shifts = {
    'n': [-1, 0],
    's': [1, 0],
    'e': [0, 1],
    'w': [0, -1],
}

directions = ['n', 's', 'e', 'w']


def process_data(input: str):
    """Make 2D array to traverse and find starting location 'S' """
    board = list(list(string) for string in input.splitlines())
    start_row, start_col = divmod([pos for pos, char in enumerate(input) if char == 'S'][0], len(board[0]))
    return board, [start_row - 1, start_col - 1]


# Process triplets of pipe openings and opposite of movement(opposite of previous triplet result)
def triplet(movement: str, pipe_piece: str):
    openings = direction_dict[pipe_piece]
    matching_char = opposite_directs[movement]
    if matching_char == openings[0]:
        return openings[1]
    if matching_char == openings[1]:
        return openings[0]


_map, _ = process_data(data_string)
s_loc = [107, 110]
current_loc = s_loc

neighbor = ''
previous_move_opp = ''
# to start iterate through directions and make first move, start direction-opening process
for way in directions:
    move = shifts[way]
    neighbor_row = current_loc[0] + move[0]
    neighbor_col = current_loc[1] + move[1]
    if neighbor_row < len(_map) and neighbor_col < len(_map[0]):
        neighbor = _map[neighbor_row][neighbor_col]
    move_dir = triplet(way, neighbor) # direction to move where opening(neighbor) accepts way
    common_piece = move_dir
    if move_dir:
        current_loc[0] += shifts[move_dir][0]
        current_loc[1] += shifts[move_dir][1]
        break

#want opening opposite of matched opening from move direction
def answer1(move_dir, _map, current_loc, neighbor):
    steps = 1
    while neighbor != 'S':
        move_dir = triplet(move_dir, _map[current_loc[0]][current_loc[1]])
        neighbor = _map[current_loc[0] + shifts[move_dir][0]][current_loc[1] + shifts[move_dir][1]] 
        current_loc[0] += shifts[move_dir][0]
        current_loc[1] += shifts[move_dir][1]
        steps += 1
        #print(move_dir, current_loc, neighbor, steps//2)
    return steps
        


def answer2(move_dir, _map, current_loc, neighbor):
    steps = 1
    while neighbor != 'S':
        move_dir = triplet(move_dir, _map[current_loc[0]][current_loc[1]])
        neighbor = _map[current_loc[0] + shifts[move_dir][0]][current_loc[1] + shifts[move_dir][1]] 
        _map[current_loc[0]][current_loc[1]] = 'X'
        current_loc[0] += shifts[move_dir][0]
        current_loc[1] += shifts[move_dir][1]
        steps += 1
        print(move_dir, current_loc, neighbor, steps)
    return _map, steps



def traverse_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    spaces = 0

    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 'X'

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    stack = [(0, 0)]  # Start traversal from the top-left corner
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) not in visited and is_valid_move(x, y):
            spaces += 1
            #print(grid[x][y])  # Process the character at the current position
            visited.add((x, y))

            # Add neighboring positions to the stack
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                stack.append((new_x, new_y))
    
    return spaces
# Example usage:
grid = [
    ['A', 'X', 'X', 'X'],
    ['E', 'X', 'F', 'X'],
    ['H', 'X', 'D', 'X'],
    ['.', 'X', 'X', 'X'],
    ['A', '.', 'c', 't']
]

print(traverse_grid(grid))




updated_map, steps = answer2(move_dir, _map, current_loc, neighbor)
print(len(updated_map[0]))
spaces = traverse_grid(updated_map)
total = 140 * 140
print(steps - 1, spaces, total, total - steps - spaces - 1)

#spaces = traverse_grid(updated_map)





