import numpy as np

with open('./input/input_11.txt') as file:
    data_string = file.read()


test_string = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


lines = data_string.splitlines()

galaxies_string_pos = [pos for pos, char in enumerate(data_string) if char == '#']

def expansion_factor(multiple: int) -> int:
    return multiple - 1

def galaxy_list_empty_rows_cols(string_pos: list[int]):
    galaxy_pos = []
    rows_to_expand = set([i for i in range(len(lines))])
    cols_to_expand = set([i for i in range(len(lines[0]))])

    for i, galaxy in enumerate(galaxies_string_pos):
        row, col = divmod(galaxy, len(lines[0]) + 1)
        if row in rows_to_expand:
            rows_to_expand.remove(row)
        if col in cols_to_expand:
            cols_to_expand.remove(col)
        galaxy_pos.append([row, col])
        
    return galaxy_pos, rows_to_expand, cols_to_expand

def galaxy_expansion(galaxies, exp_rows, exp_cols, exp_factor):
    for galaxy in galaxies:
        row_update = 0
        col_update = 0
        for row in exp_rows:
            if row < galaxy[0]:
                row_update += exp_factor
        for col in exp_cols:
            if col < galaxy[1]:
                col_update += exp_factor
        galaxy[0] += row_update
        galaxy[1] += col_update
    
    return galaxies

increase = expansion_factor(1000000)

galaxy_list, empty_rows, empty_cols = galaxy_list_empty_rows_cols(galaxies_string_pos)

updated_galaxies = galaxy_expansion(galaxy_list, empty_rows, empty_cols, increase)

def answer(expanded_posistions: list[list[int]]):
    mins = []
    for i in range(len(updated_galaxies) - 1):
        for j in range(i+1, len(updated_galaxies)):
            a = np.array(updated_galaxies[i])
            b = np.array(updated_galaxies[j])
            l1_dist = np.linalg.norm((a - b), ord=1)
            #print(a, b, l1_dist)
            mins.append(l1_dist)
    return int(sum(mins))

print(answer(updated_galaxies))
