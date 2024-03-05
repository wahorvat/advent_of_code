f = open('./input/input_12.txt')


test_string = "???.### 1,1,3"

def matches(text: str, numbers: str) -> dict:
    states = "."
    for num in numbers:
        for i in range(int(num)):
            states += "#"
        states += "."

    states_dict = {0: 1}
    new_dict = {}
    for char in text:
        for state in states_dict:
            if char == "?":
                if state + 1 < len(states):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == ".":
                if state + 1 < len(states) and states[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == "#":
                if state + 1 < len(states) and states[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]

        states_dict = new_dict
        new_dict = {}

    return states_dict.get(len(states) - 1, 0) + states_dict.get(len(states) - 2, 0)


test_sum = 0

test_line = test_string.strip().split(" ")
test_text = ((test_line[0]+"?"))[:-1]
test_numbers = test_line[1].split(",")
test_sum += matches(test_text, test_numbers)

assert test_sum == 1

sum_1 = 0
sum_2 = 0

for line in f.readlines():
    line = line.strip().split(" ")
    text_1 = ((line[0]+"?"))[:-1]
    numbers_1 = line[1].split(",")

    text_2 = (5*(line[0]+"?"))[:-1]
    numbers_2 = 5*line[1].split(",")

    sum_1 += matches(text_1, numbers_1)
    sum_2 += matches(text_2, numbers_2)

print(sum_1, sum_2)