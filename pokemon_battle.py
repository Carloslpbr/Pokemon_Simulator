import pokemon_select
import requests
import combat_param
import os
import random
import settings
import save_data
import sys
import datetime
import user_data
from collections import Counter

# Basic
user = user_data.set_user
player_1, pSkills = pokemon_select.set_pokemon()
settings.any_char()
basic_url = "https://pokeapi.co/api/v2/pokemon/"
current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_directory, "battle_log.csv")
game_date = datetime.date.today()


#implementar leitura de txt aqui
game_id =  user_data.game_id

def generate_enemy():
    pokemon_max_num = 149
    enemy_num = str(random.randint(0, pokemon_max_num))
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

def headers(battle_n,round_n, player_1, p1_hp, p2_name, p2_hp):
    os.system('cls')
    print(f"Batalha nº {battle_n}")
    combat_param.display_turn(round_n,player_1)
    combat_param.display_header(player_1,p1_hp)
    combat_param.display_header(p2_name,p2_hp)

def battle_generator():
    p1_hp, p1_ap, p1_df, p1_sa, p1_sd, p1_sp = player_stats() 
    battle_n = 1

    favorite_skill = None
    while battle_n <= settings.combats:      
        p2_name, p2_hp, p2_ap, p2_df, p2_sa, p2_sd, p2_sp = generate_enemy()
        
        pSpeed, pSpeed_p = combat_param.get_dodge_rate(player_1,p1_sp)
        pDef, pDef_p = combat_param.get_defense_power(player_1,p1_df)                                 
        eSpeed, eSpeed_p = combat_param.get_dodge_rate(p2_name,p2_sp)      
        eDef, eDef_p = combat_param.get_defense_power(p2_name,p2_df)

        round_n = 1
        damage_done = 0
        damage_taken = 0

        normal_attack_count = 0
        special_attack_count = 0
        used_skills = []             
               

        while p1_hp > 0 and p2_hp > 0:  
                        
            
            headers(battle_n,round_n, player_1, p1_hp, p2_name, p2_hp)

            ##### Player turn
            print("Battle log:")
       
            pAction, result, power_result, skill = combat_param.player_actions(player_1,p1_ap,pSkills,p2_sa)          
            
            if pAction == "1":
                normal_attack_count += 1
            if pAction == "2":
                special_attack_count += 1
                used_skills.append(skill)         
 

            if power_result > eSpeed_p:
                #p2_hp, damage = combat_param.attack(player_1, eDef_p, p2_hp, damage_done, result,p2_name)
                p2_hp, damage = combat_param.attack(player_1, eDef_p, p2_hp, power_result, p2_name)
                damage_done += damage
                

                if p2_hp <= 0:
                    if special_attack_count> normal_attack_count:
                        #colocar em função
                        count_skills = Counter(used_skills)
                        sort_skills = sorted(count_skills.items(), key=lambda item: item[1], reverse=True)
                        favorite_skill = sort_skills[0][0]
                        save_data.save_data_w(game_id, game_date, user, output_file,player_1,p2_name,battle_n,round_n,damage_done,damage_taken,favorite_skill)
                        battle_n += 1
                        break
                    elif special_attack_count < normal_attack_count:
                        #colocar em função
                        save_data.save_data_w(game_id, game_date, user, output_file,player_1,p2_name,battle_n,round_n,damage_done,damage_taken,'Standard-attack')
                        battle_n += 1
                        break   
            else:
                #colocar em função ?
                print(f"{p2_name} Esquivou do seu ataque!")                
                print("")
                settings.any_char()            

            os.system('cls')

            headers(battle_n,round_n, player_1, p1_hp, p2_name, p2_hp)
            settings.any_char() 

            ##### Enemy Turn
            combat_param.display_turn(round_n,p2_name)
            eAction, eResult, ePower_result = combat_param.enemy_action(p2_name,p2_ap)

            if ePower_result > pSpeed_p:
                #p1_hp, damage_e = combat_param.attack(p2_name, pDef_p, p1_hp, damage_taken, eResult, player_1)
                p1_hp, damage_e = combat_param.attack(p2_name, pDef_p, p1_hp, ePower_result, player_1)
                damage_taken += damage_e

                if p1_hp <= 0:
                    #save_data.save_data_l(game_id, game_date, user, output_file,player_1,p2_name,battle_n,round_n,damage_done,damage_taken)
                    
                    if special_attack_count> normal_attack_count:
                        #colocar em função
                        count_skills = Counter(used_skills)
                        sort_skills = sorted(count_skills.items(), key=lambda item: item[1], reverse=True)
                        favorite_skill = sort_skills[0][0]
                        save_data.save_data_l(game_id, game_date, user, output_file,player_1,p2_name,battle_n,round_n,damage_done,damage_taken,favorite_skill)
                        sys.exit()
                    elif special_attack_count < normal_attack_count:
                        #colocar em função
                        save_data.save_data_l(game_id, game_date, user, output_file,player_1,p2_name,battle_n,round_n,damage_done,damage_taken,'Standard-attack')
                        sys.exit() 
              
            else:
                
                print(f"{player_1} Esquivou do seu ataque!")                
                print("")
                settings.any_char()

            
            round_n += 1
    

battle_generator()