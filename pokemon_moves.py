import requests
import os
import pprint
import json

current_directory = os.path.dirname(os.path.abspath(__file__))
output_file_1 = os.path.join(current_directory, "pokemon_move__learned.csv")
output_file_2 = os.path.join(current_directory, "moves_data.csv")

# Função para obter os movimentos (moves) de um Pokémon
def get_moves(pokemon_index, base_url):
    move_set = [] 
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

poke_url = 'https://pokeapi.co/api/v2/pokemon/'
import_limit = {'limit': 40}


def get_moves_data():
    p_index = 1
    while p_index < 152:
        response = requests.get(poke_url + str(p_index))     
        data = response.json()

        i = 0
        total_moves = len(data['moves'])
        pokemon = data['name']
        while i < total_moves:
            move_name = data['moves'][i]['move']['name']
            origin_move = data['moves'][i]['version_group_details'][0]['version_group']['name']
            level_learned = data['moves'][i]['version_group_details'][0]['level_learned_at']
            learn_method = data['moves'][i]['version_group_details'][0]['move_learn_method']['name']

            if origin_move == 'red-blue':
                with open(output_file_1, 'a', encoding='utf8') as save_file:
                    save_file.write(f"{pokemon},{move_name},{level_learned},{learn_method}\n")
            i += 1
        p_index += 1


move_url = 'https://pokeapi.co/api/v2/move/'
import_limit = {'limit': 40}

def get_moves_details():
    i = 1
    import_limit = 387
    while i < import_limit:
        response = requests.get(move_url + str(i))
        data = response.json()

        move_name_ = data['name']
        accuracy = data['accuracy']
        type_dmg = data['damage_class']['name']
        power = data['power']
        pp = data['pp']
        type_name = data['type']['name']
        categorie = data['meta']['category']['name']
        desc = str(data['flavor_text_entries'][1]['flavor_text'])
        desc_ = desc.replace("\n","")
    
        with open(output_file_2, 'a',encoding="utf8") as save_m_file:
            save_m_file.write(f'{move_name_},{accuracy},{type_dmg},{power},{pp},{categorie},{type_name},"{desc_}"\n')
        i += 1

    ...


if __name__ == '__main__':
    #get_moves_data()
    get_moves_details()