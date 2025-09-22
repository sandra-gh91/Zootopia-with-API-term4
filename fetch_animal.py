import requests

API_KEY = "ZHGY2U4x2RDguD5O50NWaQ==K2N09xsGxRJW70jT"

def fetch_animal(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}  # Send as query parameter
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)  # print API message
        return []

def main():
    animals = fetch_animal("fox")  # lowercase works too
    if not animals:
        print("No data found.")
        return

    for animal in animals:
        print(f"Name: {animal.get('name', 'N/A')}")
        print(f"Locations: {', '.join(animal.get('locations', []))}")
        characteristics = animal.get('characteristics', {})
        print(f"Diet: {characteristics.get('diet', 'N/A')}")
        print(f"Type: {characteristics.get('type', 'N/A')}")
        print("-" * 50)

if __name__ == "__main__":
    main()




