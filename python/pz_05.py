from dataclasses import dataclass

with open("./input/input_05.txt") as file:
    data = file.read()


test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

@dataclass
class Range:
    dest: int
    init: int
    steps: int



def window_update(map: Range, x: int) -> int:
    if map.init <= x < (map.init + map.steps):
        return map.dest + (x - map.init)
    return x
    


def process_input(data: str):
    [seed_str, *map_strs] = data.split("\n\n")
    seeds = list(map(int, seed_str.split(":")[1].split()))
    map_str_list = [map.split(':')[1:] for map in map_strs]
    range_lists = [[Range(*list(map(int, triple.split()))) for triple in maps[0].split('\n') if triple] for maps in map_str_list]
    return seeds, range_lists



def answer1(input: str) -> int:
    seeds, maps = process_input(input)
    for idx, seed in enumerate(seeds):
        for map in maps:
            for range in map:
                print(range, seeds)
                seed = window_update(range, seed)
                if seeds[idx] != seed:
                    seeds[idx] = seed
                    break
    return min(seeds)



assert answer1(test_data) == 35

