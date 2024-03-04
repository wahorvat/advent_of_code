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
print(lines[0])

def count_arrangements(input_string):
    parts = input_string.split()
    sequence = list(parts[0])
    lengths = list(map(int, parts[1].split(',')))
    print(f'\n lengths: {lengths}', f'sequence: {sequence} \n')

    total_arrangements = 1  
    
    for length in lengths:
        count = sequence.count('?') + sequence.count('#')
        if count < length:
            return 0
        arrangements = 1
        for i in range(length):
            arrangements *= count - i
        total_arrangements *= arrangements
        sequence = sequence[length+1:]  # remove the used characters and a period

    return total_arrangements

# Test the function
print(count_arrangements('???.### 1,1,3'))  # Output: 0
