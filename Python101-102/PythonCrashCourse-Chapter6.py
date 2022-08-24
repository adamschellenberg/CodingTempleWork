# Python Crash Course, Chapter 6
# Aug 23, 2022

bulbasaur = {
    'name': 'Bulbasaur',
    'pokedex-number': '001', 
    'type': 'grass', 
    'weakness': 'fire'
    }
charmander = {
    'name': 'Charmander',
    'pokedex-number': '004',
    'type': 'fire', 
    'weakness': 'water'
    }
squirtle = {
    'name': 'Squirtle',
    'pokedex-number': '007',
    'type': 'water',
    'weakness': 'grass'
}

party = [bulbasaur, charmander, squirtle]
for pokemon in party:
    print (f"Pokemon: {pokemon['name']}")
    print (f"Pokedex Number: {pokemon['pokedex-number']}")
    print (f"Type: {pokemon['type']}")
    print (f"Weakness: {pokemon['weakness']}\n")

pokemon_gen2 = {
    'chikorita': {
        'pokedex-number': '152',
        'type': 'grass',
        'weakness': 'fire'
    },
    'cyndaquil': {
        'pokedex-number': '155',
        'type': 'fire',
        'weakness': 'water'
    },
    'totodile': {
        'pokedex-number': '158',
        'type': 'water',
        'weakness': 'grass'
    }
}

for pokemon, pokemon_info in pokemon_gen2.items():
    print (f"Pokemon: {pokemon.title()}")
    print (f"Pokedex Number: {pokemon_info['pokedex-number']}")
    print (f"Type: {pokemon_info['type']}")
    print (f"Weakness: {pokemon_info['weakness']}\n")
