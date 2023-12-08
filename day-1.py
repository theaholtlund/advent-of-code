# Advent of Code Christmas Calendar, Day #1

# Import required libraries
from dotenv import load_dotenv

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


