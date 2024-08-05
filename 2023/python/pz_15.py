with open("./input/input_15.txt", "r") as file:
    strings = file.read().split(",")

def hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

answer_1 = sum(map(hash, strings))
print(f"Solution 1:  {answer_1}")



boxes = [dict() for _ in range(256)]

for step in strings:
    match step.strip('-').split('='):
        case [l, f]: 
            boxes[hash(l)][l] = int(f)
        case [l]:    
            boxes[hash(l)].pop(l, 0)

answer_2 = (sum(i*j*f for i,b in enumerate(boxes, 1)
                for j,f in enumerate(b.values(), 1)))

print(f"Solution 2:  {answer_2}")