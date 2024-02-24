# Advent of Code Christmas Calendar, Day #5

# Import required libraries
from functools import reduce
from config import fetch_data

# Set URL for the day
url = 'https://adventofcode.com/2023/day/5/input'

# Function to parse seeds and maps from input data
def parse_challenge_input(data):
    seed_data, *map_data = data.strip().split('\n\n')
    seeds = [int(val) for val in seed_data.split(':')[1].split()]
    parsed_maps = [[list(map(int, line.split())) for line in section.split('\n')[1:]] for section in map_data]
    return seeds, parsed_maps

# Function to resolve mappings and calculate final seed locations
def resolve_mapping(inputs, mappings):
    for start, length in inputs:
        while length > 0:
            for target, source, size in mappings:
                offset = start - source
                if 0 <= offset < size:
                    yield (target + offset, min(size - offset, length))
                    start += min(size - offset, length)
                    length -= min(size - offset, length)
                    break
            else:
                yield (start, length)
                break

# Function to solve the challenge and find seed locations
def solve_challenge(seeds, parsed_maps):
    return [
        min(reduce(resolve_mapping, parsed_maps, seed))[0] 
        for seed in [zip(seeds, [1] * len(seeds)), zip(seeds[0::2], seeds[1::2])]
    ]

# Main function
def main():
    # Fetch input data from Advent of Code website
    data = fetch_data(url)

    # Parse challenge input
    seeds, parsed_maps = parse_challenge_input(data)

    # Solve the challenge
    solution = solve_challenge(seeds, parsed_maps)

    # Output results
    print("Minimum seed location, part 1:", solution[0])
    print("Next seed location, part 2:", solution[1])

# Call the main function
if __name__ == "__main__":
    main()
