import math

with open('./input/input_09.txt') as file:
    data_string = file.read()

test_string = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

lines = data_string.splitlines()
numerics = [list(map(int, line.split())) for line in lines]

final_nums = []
for numeric in numerics:
    idx = 0
    diffs = [numeric]
    while any(val != 0 for val in diffs[idx]):
        temp = []
        for i in range(len(diffs[idx]) - 1):
            temp.append(diffs[idx][i + 1] - diffs[idx][i])
        diffs.append(temp)
        idx += 1
    new_vals = []
    temp_val = 0
    for i in range(2, len(diffs)+1):
        temp_val = diffs[-i][0] - temp_val
        new_vals.append(temp_val)
    final_nums.append(new_vals[-1])
print(sum(final_nums))