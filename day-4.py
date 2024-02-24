# Advent of Code Christmas Calendar, Day #4

# Import required libraries
import re
import numpy as np
from config import fetch_data

# Set URL for the day
url = 'https://adventofcode.com/2023/day/4/input'

# Calculate total points for each team
def calculate_points(data):
    # Split the input data into lines
    lines = data.strip().split("\n")
    
    # Extract team information and calculate wins
    teams = [list(map(int, re.findall(r"\d+", line))) for line in lines]
    team_wins = [len(set(team[11:]) & set(team[1:11])) for team in teams]

    # Part 1: Calculate total points for Part 1
    total_points_part1 = sum(2 ** (wins - 1) for wins in team_wins if wins > 0)

    # Part 2: Simulate the game and calculate total points for Part 2
    num_teams = len(teams)
    cards = np.ones(num_teams)
    for i in range(num_teams):
        cards[i + 1 : i + team_wins[i] + 1] += cards[i]

    total_points_part2 = int(cards.sum())
    
    return total_points_part1, total_points_part2

# Main function to execute the program
def main():
    # Fetch input data from Advent of Code website
    data = fetch_data(url)

    # Calculate total points
    total_points_part1, total_points_part2 = calculate_points(data)
    print("Total points for part 1):", total_points_part1)
    print("Total points for part 2:", total_points_part2)

# Call the main function
if __name__ == "__main__":
    main()
