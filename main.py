import requests
import os
import evolution_chain
import pokemon_moves


# Define a quantidade de importações
def pokemon_import_limit(x):
    return {'limit': x}

# Define a URL em que será importado o Pokémon, exemplo https://pokeapi.co/api/v2/pokemon/charmander
def create_pokemon_data_url(url, pokemon_name):
    return f'{url}{pokemon_name}'

# Função para fazer uma solicitação HTTP com parâmetros
def request_data(url, params):
    response_data = requests.get(url, params=params)
    return response_data

# Define a URL completa para o Pokémon com base no índice
def set_pokemon_url(base_url, index):
    return f'{base_url}{index}'

def show_status_1(display_pName):

    os.system('cls')
    print("STATUS")
    print(f"IMPORTANDO POKEMONS ❌ - Etapa: importando {display_pName}")
    print(f"importando evoluções")
    ...

# Função para obter os stats de um Pokémon
def get_pokemon_stats(pokemon_data, index, poke_base_url):
    hp = pokemon_data['stats'][0]['base_stat']
    ap = pokemon_data['stats'][1]['base_stat']
    df = pokemon_data['stats'][2]['base_stat']
    sa = pokemon_data['stats'][3]['base_stat']
    sd = pokemon_data['stats'][4]['base_stat']
    sp = pokemon_data['stats'][5]['base_stat']
    type1 = pokemon_data['types'][0]['type']['name']
    type2 = pokemon_data['types'][1]['type']['name'] if len(pokemon_data['types']) > 1 else None
    weight = pokemon_data['weight']
    height = pokemon_data['height']
    moves = pokemon_moves.get_moves(index, poke_base_url)
    sprite = pokemon_data['sprites']['front_default']
    return hp, ap, df, sa, sd, sp, type1, type2, weight, height, moves, sprite

# Função principal
def main():
    # URLs para importação de dados
    poke_base_url = "https://pokeapi.co/api/v2/pokemon/"
    poke_description_url = "https://pokeapi.co/api/v2/pokemon-species/"
    
    # Define o limite de importação
    import_limit = pokemon_import_limit(151)
    
    # Faz uma solicitação HTTP para obter os dados básicos dos Pokémon
    data = request_data(poke_base_url, params=import_limit)
    json_data = data.json()
    poke_base = json_data['results']
    
    # Define o caminho onde o arquivo CSV será salvo
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_directory, "pokemons.csv")

    # Abre o arquivo CSV para escrita
    with open(output_file, "w", encoding= "utf8") as file:
        # Escreve o cabeçalho do CSV
        file.write('"name","desc","hp","ap","df","sa","sd","sp","type1","type2","weight","height","moves","sprite"\n')
        
        # Inicializa o índice para rastrear os Pokémon
        index = 1

        # Loop através dos Pokémon da lista
        for item in poke_base:
            # Cria a URL para obter a descrição do Pokémon
            set_poke_url = set_pokemon_url(poke_description_url, index)
            
            # Faz uma solicitação HTTP para obter a descrição do Pokémon
            desc_data = request_data(set_poke_url, import_limit)
            json_desc_data = desc_data.json()
            desc_data_b = json_desc_data['flavor_text_entries'][1]['flavor_text']
            desc = desc_data_b.replace("\n", " ")
            pokemon_name = item['name']
            
            # Cria a URL para obter os dados detalhados do Pokémon
            pokemon_data_url = create_pokemon_data_url(poke_base_url, item['name'])
            
            # Faz uma solicitação HTTP para obter os dados detalhados do Pokémon
            pokemon_response = request_data(pokemon_data_url, import_limit)
            pokemon_data = pokemon_response.json()
            
            # Obtém os stats e movimentos do Pokémon
            hp, ap, df, sa, sd, sp, type1, type2, weight, height, moves, sprite = get_pokemon_stats(pokemon_data, index, poke_base_url)

            #mostra status    
            show_status_1(pokemon_name)


            index += 1

            # Escreve os dados do Pokémon no arquivo CSV
            file.write(f'"{pokemon_name}","{desc}","{hp}","{ap}","{df}","{sa}","{sd}","{sp}","{type1}","{type2}","{weight}","{height}","{moves}","{sprite}"\n')

        os.system('cls')

if __name__ == "__main__":
    main()
    evolution_chain.evolution_chain()




