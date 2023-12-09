# Advent of Code Christmas Calendar, Day #1

# Import required libraries
from dotenv import load_dotenv
import re
import os
import requests

# Load environment variables into environment
load_dotenv()
cookie_value = os.environ.get('COOKIE_VALUE')

# Constructing an HTTP header for cookie authentication
# The session cookie value can be found in the browser developer tools after logging in
headers = {'Cookie': f'session={cookie_value}'}
url = 'https://adventofcode.com/2023/day/1/input'

# Fetch the content of the URL
response = requests.get(url, headers=headers)
data = response.text

# ======== PART 1: NUMBERS ONLY ========
# Initialise the sum variable
total_sum_numbers = 0

# Process each line in the input
for line in data.splitlines():
    # Checks if each character is a digit, and if so converts it to an integer
    digits = [int(char) for char in line if char.isdigit()]

    # Calculate calibration value, adding the first number to the tens place in the two digit number
    calibration_value = digits[0] * 10 + digits[-1]

    # Add the calibration value to the total sum
    total_sum_numbers += calibration_value

print("Total Sum Numbers:", total_sum_numbers)



# ======== PART 2: ALL CHARACTERS ========
# Define a mapping between spelled out digits and numerical representations
digit_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# Sample lines for testing
lines = [
    "njtwonefvhjplkjgvsevenbjg77",
    "nine1twonem",
    "sixtytwone"
]

# Initialise the sum variable
total_sum_characters = 0

# Process each line in the input
for line in data.splitlines():
    digits = []
    
    # Iterate through each character, check for digit and add to digits list
    for index, char in enumerate(line):
        if char.isdigit():
            digits.append(char)
        
        # Check for spelled out numbers in the line
        for key, value in digit_mapping.items():
            # Check if the line starts with the spelled out number
            if line[index:].startswith(key):
                # Add the corresponding numerical value to the digits list
                digits.append(str(value))

    # Calculate the total sum using the first and last digit in the digits list
    if digits:
        total_sum_characters += int(digits[0] + digits[-1])

print("Total Sum Characters:", total_sum_characters)
