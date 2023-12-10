# Advent of Code Christmas Calendar, Day #2

# Import required libraries
import re
from collections import defaultdict
from config import fetch_data

# Set URL for the day
url = 'https://adventofcode.com/2023/day/2/input'

# Find the sum of IDs of possible games (Part 1) and the sum of powers of minimum sets (Part 2)
def find_minimum_cubes(data):
    # Define variables to store counts
    p1_sum_of_ids = 0
    p2_sum_of_powers = 0

    # Iterate through each game in the input data
    for line in data.strip().split('\n'):
        is_possible = True
        game_id, game_description = line.split(':')
        cube_counts = defaultdict(int)

        # Check each event in the game description
        for event in game_description.split(';'):
            # Check each cube in the event
            for cubes in event.split(','):
                count, color = cubes.split()
                count = int(count)
                cube_counts[color] = max(cube_counts[color], count)

                # Check if the cube count exceeds the maximum allowed
                if count > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    is_possible = False

        # Calculate the power of the minimum set of cubes for this game
        min_set_power = 1
        for count in cube_counts.values():
            min_set_power *= count

        # Update Part 1 and Part 2 sum vartables
        p2_sum_of_powers += min_set_power
        if is_possible:
            p1_sum_of_ids += int(game_id.split()[-1])

    return p1_sum_of_ids, p2_sum_of_powers


# Main function to execute the program, find the solutions for both parts
def main():
    # Fetch input data from Advent of Code website
    data = fetch_data(url)

    # Call the function to find the solutions for both parts
    part1_result, part2_result = find_minimum_cubes(data)

    # Print the results
    print(f"Part 1: The sum of IDs of possible games is: {part1_result}")
    print(f"Part 2: The sum of powers of minimum sets is: {part2_result}")


# Call the main function
if __name__ == "__main__":
    main()
