import regex
import string

with open("./input/input_01.txt") as file:
    data = file.read()

def filter_digits(s):
    return list(x for x in s if x in string.digits)

def answer1(inp):
    lines = inp.splitlines()
    digits = ( filter_digits(line) for line in lines )
    first_and_last = ( "".join([line[0], line[-1]]) for line in digits )
    numbers = map(int, first_and_last)
    return sum(numbers)

def words_to_vals(s):
    return regex.findall("[1234567890]|one|two|three|four|five|six|seven|eight|nine", s, overlapped=True)

convert_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, 
           "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}


def answer2(inp):
    lines = inp.splitlines()
    digits = ( words_to_vals(line) for line in lines )
    numbers = ( 10 * convert_dict[line[0]] + convert_dict[line[-1]] for line in digits )
    return sum(numbers)

ans1 = answer1(data)
ans2 = answer2(data)

print(ans1, ans2)






