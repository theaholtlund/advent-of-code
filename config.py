# Shared Functionality for Advent of Code Christmas Calendar

# Import required libraries
import os
import requests
from dotenv import load_dotenv

# Get the data to be processed
def fetch_data(url):
    # Load environment variables into environment
    load_dotenv()
    cookie_value = os.environ.get('COOKIE_VALUE')

    # Constructing an HTTP header for cookie authentication
    headers = {'Cookie': f'session={cookie_value}'}

    # Fetch the content of the URL
    response = requests.get(url, headers=headers)
    data = response.text

    return data
