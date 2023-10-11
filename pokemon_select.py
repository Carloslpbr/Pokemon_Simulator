import requests
import os
import random
import pokemon_moves
import json
import sys
import os


def get_pStats(pokemon_data):
    hp = pokemon_data['stats'][0]['base_stat']
    ap = pokemon_data['stats'][1]['base_stat']
    df = pokemon_data['stats'][2]['base_stat']
    sa = pokemon_data['stats'][3]['base_stat']
    sd = pokemon_data['stats'][4]['base_stat']
    sp = pokemon_data['stats'][5]['base_stat']
    type1 = pokemon_data['types'][0]['type']['name']
    type2 = pokemon_data['types'][1]['type']['name'] if len(pokemon_data['types']) > 1 else None

    return hp, ap, df, sa, sd, sp, ap, type1, type2


def show_pokemon_data(pokemon, poke_url):
    if poke_url[8] is not None:
        print(f"{pokemon} é um Pokemon tipo {poke_url[7]}/{poke_url[8]}")
    else:
        print(f"{pokemon} é um Pokemon tipo {poke_url[7]}")
    print("")
    print("Stats:")
    print(f"HP = {stats_desc(poke_url[0])}\nAP = {stats_desc(poke_url[1])}\nDF = {stats_desc(poke_url[2])}")
    print(f"SA = {stats_desc(poke_url[3])}\nSD = {stats_desc(poke_url[4])}\nSP = {stats_desc(poke_url[5])}")
    avg = (poke_url[0] + poke_url[1] + poke_url[2] + poke_url[3] + poke_url[4] + poke_url[5])/6
    print("")
    set_dificulty(avg)
    print("")
    print("Suas skills:")
    print(pokemon_skills(pokemon))
  

def stats_desc(stat_value):
    if stat_value >= 80:
        return "Muito alto"
    if stat_value >= 60 and stat_value < 80:
        return "Alto"
    if stat_value >= 40 and stat_value < 60:
        return "Médio"
    if stat_value >= 20 and stat_value < 40:
        return "Baixo"
    else:
        return "Muito baixo"

def pokemon_skills(pokemon):
    pSkills = pokemon_moves.get_moves(pokemon, "https://pokeapi.co/api/v2/pokemon/")
    skill_list = pSkills  # Assuming pSkills contains a list of moves
    total_skills = len(skill_list)
    pSkill_set = []

    skill_index = 0
    while skill_index < 4:
        randomSkill = random.randint(0, (total_skills - 1))
        pSkill_set.append(skill_list[randomSkill])
        skill_index += 1
    return pSkill_set


def set_dificulty(avg):
    if avg >= 60:
        print("A dificuldade será Fácil")
    elif avg >= 40 and avg < 60:
        print("A Dificuldade será média")
    else:
        print("A dificuldade será difícil!")

def set_pokemon():
    selected = False
    while selected == False:
        #Selecione aqui o pokemon
        user_input = input("Digite o Pokemon que deseja utilizar: ")

        #define a base do pokemon, agrupando a url base + user_input
        user_pData = requests.get("https://pokeapi.co/api/v2/pokemon/"+user_input)
        
        try:
        #retorna os dados em json
            json_data = user_pData.json()  
            pStats = get_pStats(json_data)
            os.system('cls')
        except json.JSONDecodeError as Error:
            exception_name = Error.__class__.__name__
            os.system('cls')
            print(f"{exception_name}: {user_input} não é um Pokémon válido,\ncheque a lista para ver quais estão disponíveis")
            print("Saindo do programa!")
            sys.exit()

        #retorna todos os dados do pokemon
        show_pokemon_data(user_input,pStats)
        print("")
        pokemon_skills(user_input)


 
        return user_input 



        


