import requests
import json

# Função para obter os movimentos (moves) de um Pokémon
def get_moves(pokemon_index, base_url):
    move_set = []  # Inicializa uma lista vazia para armazenar os movimentos
    move_response = requests.get((base_url + str(pokemon_index)))
    move_data = move_response.json()
    i = 0
    for _ in move_data['moves']:
        # Obtém o nome do movimento
        move_name = move_data['moves'][i]['move']['name']
        # Obtém o grupo de versão (version group) de onde o movimento se origina
        move_origin = move_data['moves'][i]['version_group_details'][0]['version_group']['name']
        
        # Verifica se o movimento se origina no grupo "red-blue" e o adiciona à lista de movimentos
        if move_origin == 'red-blue':
            move_set.append(move_name)
        i += 1
                
    return move_set
