import requests

API_KEY = "ZHGY2U4x2RDguD5O50NWaQ==K2N09xsGxRJW70jT"

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

