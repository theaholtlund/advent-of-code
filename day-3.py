# Advent of Code Christmas Calendar, Day #3

# Import required libraries
from config import fetch_data

# Set URL for the day
url = 'https://adventofcode.com/2023/day/3/input'

# Extract part numbers from the engine schematic based on specified rules
def extract_part_numbers(engine_schematic):
    gears = set()
    part_numbers_by_gear = {}
    sum_of_part_numbers = 0

    for row in range(len(engine_schematic)):
        current_number = 0
        has_part = False

        for column in range(len(engine_schematic[row]) + 1):
            if column < len(engine_schematic[row]) and engine_schematic[row][column].isdigit():
                current_number = current_number * 10 + int(engine_schematic[row][column])

                # Check neighbors of the current digit
                for row_offset in [-1, 0, 1]:
                    for column_offset in [-1, 0, 1]:
                        if 0 <= row + row_offset < len(engine_schematic) and 0 <= column + column_offset < len(engine_schematic[0]):
                            neighbor_char = engine_schematic[row + row_offset][column + column_offset]

                            # Check if the neighbor is a part or a gear symbol
                            if not neighbor_char.isdigit() and neighbor_char != '.':
                                has_part = True

                            if neighbor_char == '*':
                                gears.add((row + row_offset, column + column_offset))
            elif current_number > 0:
                # Store part numbers associated with each gear
                for gear in gears:
                    if gear not in part_numbers_by_gear:
                        part_numbers_by_gear[gear] = []
                    part_numbers_by_gear[gear].append(current_number)

                # Add current number to the sum if there's a nearby part
                if has_part:
                    sum_of_part_numbers += current_number

                current_number = 0
                has_part = False
                gears = set()

    return sum_of_part_numbers, part_numbers_by_gear


# Calculate the gear ratios based on the extracted part numbers
def calculate_gear_ratios(part_numbers_by_gear):
    sum_of_gear_ratios = 0

    for gear, part_numbers in part_numbers_by_gear.items():
        if len(part_numbers) == 2:
            # Calculate gear ratio and add to the sum
            sum_of_gear_ratios += part_numbers[0] * part_numbers[1]

    return sum_of_gear_ratios


# Main function to execute the program, find the solutions for both parts
def main():
    # Fetch input data from Advent of Code website
    data = fetch_data(url)

    # Split the data into lines to create the engine schematic grid
    engine_schematic = data.splitlines()

    # Part 1: Sum of part numbers
    sum_of_part_numbers, part_numbers_by_gear = extract_part_numbers(engine_schematic)
    print(f"Part 1 Solution: {sum_of_part_numbers}")

    # Part 2: Sum of gear ratios
    sum_of_gear_ratios = calculate_gear_ratios(part_numbers_by_gear)
    print(f"Part 2 Solution: {sum_of_gear_ratios}")


# Call the main function
if __name__ == "__main__":
    main()
