import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):

    url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  # returns list of animal dictionaries
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)
        return []


