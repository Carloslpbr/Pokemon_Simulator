import requests
import os

# Define o limite de importação para a cadeia de evolução de Pokémon
def pokemon_evolution_chain_limit(x):
    return {'limit': x}

# Função para extrair e salvar dados da cadeia de evolução de Pokémon
def evolution_chain():
    # URL base para obter informações da cadeia de evolução
    base_url = "https://pokeapi.co/api/v2/evolution-chain/"

    # Define o limite de importação
    params = pokemon_evolution_chain_limit(77)

    # Caminho do arquivo onde os dados da cadeia de evolução serão salvos
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_directory, "evolution_chain.csv")

    index = 1

    with open(output_file, "w") as file_2:
        # Escreve o cabeçalho do arquivo
        file_2.write('"Base", "Evolution 1", "Evolution 2"\n')

        while index < params['limit']:
            base_form = None
            evolution_1 = None
            evolution_2 = None

            # Exibindo o progresso da importação
            n_2 = str(round((index * 100.0) / params['limit'], 2)) + "%"

            # Monta a URL da cadeia de evolução com base no índice
            chain_url = base_url + str(index)
            response = requests.get(chain_url)
            data = response.json()

            # Obtém o nome da forma base do Pokémon
            base = data['chain']['species']['name']
            base_form = base

            # Obtém o nome da primeira evolução
            try:
                evolution1 = data['chain']['evolves_to'][0]['species']['name']
                evolution_1 = evolution1
            except:
                evolution_1 = None

            try:
                # Tenta obter o nome da segunda evolução, se existir
                evolution2 = data['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
                evolution_2 = evolution2
            except:
                evolution_2 = None

            os.system('cls')
            print("STATUS DA ETAPA:")
            print(f"adicionando evoluções de {base_form}")

            index += 1

            # Escreve os dados da cadeia de evolução no arquivo CSV
            if evolution_2 is not None:
                file_2.write(f'"{base_form}", "{evolution_1}", "{evolution_2}" \n')
            else:
                file_2.write(f'"{base_form}", "{evolution_1}" \n')

        os.system('cls')

evolution_chain()