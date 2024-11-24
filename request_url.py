import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokeman_data = response.json()
        # print(pokeman_data)
        return pokeman_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"

pokeman_info = get_pokemon_info(pokemon_name)

if pokeman_info:
    print(f"{pokeman_info["name"].capitalize}")
    print(f"{pokeman_info["id"]}")
    print(f"{pokeman_info["height"]}")
    print(f"{pokeman_info["moves"]}")
