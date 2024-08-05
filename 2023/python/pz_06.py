import math

with open("./input/input_06.txt") as file:
    data = file.read()

test_data = """Time:      7  15   30
Distance:  9  40  200"""



def process_data(input: str):
    times = list(map(int, input.splitlines()[0].split(':')[1].split()))
    distances = list(map(int, input.splitlines()[1].split(':')[1].split()))
    time = int("".join(input.splitlines()[0].split(':')[1].split()))
    distance = int("".join(input.splitlines()[1].split(':')[1].split()))
    return times, distances, time, distance


def answer1(input):
    times, distances = process_data(input)
    ways = []
    wait = 0
    for time, dist in zip(times, distances):
        while ((time - wait) * wait) <= dist:
            wait += 1
        ways.append((time + 1) - (wait * 2))
        wait = 0
    return math.prod(ways)



def answer2(input):
    _, _, time, dist = process_data(input)
    wait = 0
    while ((time - wait) * wait) <= dist:
        wait += 1
    ways = (time + 1) - (wait * 2)
    return ways


print(answer2(data))