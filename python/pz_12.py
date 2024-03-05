from functools import cache

#with open('./input/input_12.txt') as file:
#    data_string = file.read()


test_string = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

# def f(line):
#     P, N = line.split()
#     P, N = (P+'?') * 5, eval(N) * 5

#     @cache
#     def dp(p, n, r=0):
#         if p == len(P): 
#             return n == len(N)

#         if P[p] in '.?': 
#             r += dp(p+1, n)

#         try:
#             q = p+N[n]
#             if '.' not in P[p:q] and '#' not in P[q]:
#                 r += dp(q+1, n+1)
#         except IndexError: 
#             pass

#         return r

#     return dp(0, 0)

# print(sum(map(f, open('./input/input_12.txt'))))


@cache
def recurse(lava, springs, result=0):
    if not springs:
        return '#' not in lava
    current, springs = springs[0], springs[1:]
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if "#" in lava[:i]:
            break
        if (nxt := i + current) <= len(lava) and '.' not in lava[i : nxt] and lava[nxt : nxt + 1] != "#":
            result += recurse(lava[nxt + 1:], springs)
    return result


with open("./input/input_12.txt", "r") as file:
    data = [x.split() for x in file.read().splitlines()]
    p1, p2 = 0, 0
    for e, (lava, springs) in enumerate(data):
        p1 += recurse(lava, (springs := tuple(map(int, springs.split(",")))))
        p2 += recurse("?".join([lava] * 5), springs * 5)
    print(p1, p2)

