import itertools

with open('./input/input_12.txt') as file:
    data_string = file.read()


test_string = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

lines = test_string.splitlines()
print(int(lines[0].split()[1][0]))

"""permutations of spaced chuncks that fit the number considering existing characters"""



