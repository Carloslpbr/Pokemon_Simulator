import pokemon_select
import requests
import combat_param
import os
import random
import settings

# Basic

player_1 = pokemon_select.set_pokemon()
settings.any_char()
basic_url = "https://pokeapi.co/api/v2/pokemon/"
current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_directory, "battle_log.csv")


#implementar leitura de txt aqui
current_game = ...


def generate_enemy():

    # Generate num and export data
    enemy_num = str(random.randint(0, 149))
    enemy_url = requests.get(basic_url + enemy_num)
    json_enemy_data = enemy_url.json()
    enemy_stats = pokemon_select.get_pStats(json_enemy_data)
     
          
    eName = json_enemy_data['name']
    eHP = enemy_stats[0]
    eAP = enemy_stats[1]
    eDF = enemy_stats[2]
    eSA = enemy_stats[3]
    eSD = enemy_stats[4]
    eSP = enemy_stats[5]

    return eName, eHP, eAP, eDF, eSA, eSD, eSP

def player_stats():
    # Player data
    player_1_url = requests.get(basic_url + player_1)
    json_player_1_data = player_1_url.json()
    stats = pokemon_select.get_pStats(json_player_1_data)
    
    pHP = stats[0]
    pAP = stats[1]
    pDF = stats[2]
    pSA = stats[3]
    pSD = stats[4]
    pSP = stats[5]

    return pHP, pAP, pDF, pSA, pSD, pSP

def battle_generator():

    p1_hp, p1_ap, p1_df, p1_sa, p1_sd, p1_sp = player_stats() 
    battle_n = 1
    round_n = 1
    damage_done = 0
    damage_taken = ...

    while battle_n < settings.combats:      
        p2_name, p2_hp, p2_ap, p2_df, p2_sa, p2_sd, p2_sp = generate_enemy()


        ##### Battle
        while p1_hp > 0 and p2_hp > 0:
            os.system('cls')  
            print(f"Batalha nº: {battle_n}")     
            

            ##### combat header
            combat_param.display_turn(round_n,player_1)

            ##### poke Headers
            combat_param.display_header(player_1,p1_hp)
            combat_param.display_header(p2_name,p2_hp)

            ##### Player turn
            print("Battle log:")
            pAction, result, power_result = combat_param.player_actions(player_1,p1_ap)
            pSpeed, pSpeed_p = combat_param.get_dodge_rate(player_1,p1_sp)
            pDef, pDef_p = combat_param.get_defense_power(player_1,p1_df)


            ##### mover bloco ?                      
            eSpeed, eSpeed_p = combat_param.get_dodge_rate(p2_name,p2_sp)      
            eDef, eDef_p = combat_param.get_defense_power(p2_name,p2_df)
            
            if power_result > eSpeed_p:
                print(f"{player_1} acertou")
                damage_inflicted = combat_param.inflict_damage(result,eDef)
                if damage_inflicted > 0:
                    #colocar em função ?
                    p2_hp -= damage_inflicted
                    damage_done += damage_inflicted
                    print(f"Dano causado: {damage_inflicted}")
                    print("")
                elif damage_inflicted <= 0:
                    print(f"{p2_name} resistiu ao ataque de {player_1}!")

                if p2_hp <= 0:
                    print("Você venceu! ")
                    # colocar em uma função
                    with open(output_file, "a") as log:        
                        log.write(f'{player_1}, Win,{p2_name}, {battle_n}, {round_n}, {damage_done}, {damage_taken}\n')
                    battle_n += 1
                    round_n = 1
                    damage_done = 0
                settings.any_char()            

            else:
                #colocar em função ?
                print(f"{p2_name} Esquivou do seu ataque!")                
                print("")
                settings.any_char()
            

            os.system('cls')

            ##### combat header
            print(f"Batalha nº: {battle_n}")
            combat_param.display_turn(round_n,p2_name)
            
            
            ##### poke Headers            
            combat_param.display_header(player_1,p1_hp)
            combat_param.display_header(p2_name,p2_hp)
            settings.any_char() 

            ##### Enemy Turn
            combat_param.display_turn(round_n,p2_name)
            eAction, eResult, ePower_result = combat_param.enemy_action(p2_name,p2_ap)
            
            

            ###dek
            if ePower_result > pSpeed_p:
                print(f"{player_1} acertou")
                damage_inflicted = combat_param.inflict_damage(eResult,pDef) #substituir eDef
                if damage_inflicted > 0:
                    #colocar em função ?
                    p1_hp -= damage_inflicted
                    damage_done += damage_inflicted
                    print(f"Dano causado: {damage_inflicted}")
                    print("")
                elif damage_inflicted <= 0:
                    print(f"{player_1} resistiu ao ataque de {p2_name}!")

                if p1_hp <= 0:
                    print("Você venceu! ")
                    # colocar em uma função
                    with open(output_file, "a") as log:        
                        log.write(f'{player_1}, Lost,{p2_name}, {battle_n}, {round_n}, {damage_done}, {damage_taken}\n')
                    battle_n += 1
                    round_n = 1
                    damage_done = 0
                settings.any_char()            

            else:
                #colocar em função ?
                print(f"{player_1} Esquivou do seu ataque!")                
                print("")
                settings.any_char()




            round_n += 1
            

   

battle_generator()

