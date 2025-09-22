import requests
import html
import json


API_KEY = "ZHGY2U4x2RDguD5O50NWaQ==K2N09xsGxRJW70jT"

def fetch_animal(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)  # print API message
        return []
def generate_animals_html(animals_data):
    """Generate HTML list items for each animal."""
    animals_html = ""
    for animal in animals_data:
        name = html.escape(animal.get("name", "N/A"))
        location = html.escape(",".join(animal.get("locations", [])))
        diet = html.escape(animal.get("characteristics", {}).get("diet", "N/A"))
        a_type = html.escape(animal.get("characteristics", {}).get("type", "N/A"))

        animals_html += f'''
<li class="cards__item">
    <div class="card__title">{name}</div>
    <p class="card__text">
        <strong>Diet:</strong> {diet}<br/>
        <strong>Location:</strong> {location}<br/>
        <strong>Type:</strong> {a_type}<br/>
    </p>
</li>
'''
    return animals_html




def main():

    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = fetch_animal(animal_name)
    if not animals_data:
        print("No data found.")
        return

    animals_html = generate_animals_html(animals_data)
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Animals - {html.escape(animal_name)}</title>
        <style>
            .cards__item {{
                border: 1px solid #ccc;
                padding: 10px;
                margin: 10px;
                list-style-type: none;
            }}
            .card__title {{
                font-weight: bold;
                font-size: 1.2em;
                margin-bottom: 5px;
            }}
            .card__text {{
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <h1>Animals matching "{html.escape(animal_name)}"</h1>
        <ul>
            {animals_html}
        </ul>
    </body>
    </html>
    """

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(full_html)

    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()




