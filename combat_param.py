import random
import settings

def roll_attack_dice(pokemon,attack_p):
    dice_result = random.randint(1,20)
    print(f"{pokemon} atacou!")

    if dice_result == 20:
        Atk_p = round(attack_p * 0.3)
        print("CRITICAL HIT!")
    else:
        Atk_p = round(attack_p * 0.15)
    
    total_power = round(dice_result+Atk_p,0)
    return Atk_p, total_power

def roll_damage_dice():
    dice_result = random.randint(1,8)
    
    return dice_result


def get_dodge_rate(pokemon, dodge_p):
    dice_result = random.randint(1,20)    
    #print(f"Tirou {dice_result}")
    if dice_result == 20:
        Spd_p = round(dodge_p * 0.3)
        print("HIGH SPEED!")
    else:
        Spd_p = round(dodge_p * 0.15)
   
    dodge_speed = round(dice_result+Spd_p,0)
    return Spd_p, dodge_speed

def get_defense_power(pokemon, defense_p):
    dice_result = random.randint(1,20)  
    
    if dice_result == 20:
        Def_p = round(defense_p * 0.10)
        print("ENDURE!")
    else:
        Def_p = round(defense_p * 0.05)
   
    Def_power = round(dice_result+Def_p,0)
    return Def_p, Def_power


def player_actions(pokemon,attack_p,skill_list):

    while True: 
        print("[1] Atacar, [2] Special")
        pAction = input("Digite sua ação: ")
        print("")      

        if pAction == "1":
            result, power_result = roll_attack_dice(pokemon,attack_p)
            return pAction, result, power_result
        elif pAction == "2":
             print(skill_list)
        else:
            print("Opção invalida!")
            
            

    
def enemy_action(pokemon,attack_p):
    eAction = "1"
    eResult, epower_result = roll_attack_dice(pokemon,attack_p)
    return eAction, eResult, epower_result

def display_header(pName, Health):
    print(f"{pName}:")
    print(f"HP: {Health}")
    print("")

def display_turn(round_n,player):
    print(f"Turno - {round_n}")                 
    print(f"É a vez de {player}")
    print("")


def inflict_damage(base_damage,target_def):
    dice_damage = roll_damage_dice()
    total_damage = dice_damage+base_damage
    damage_inflicted = total_damage - target_def
    return damage_inflicted


def attack(player_1, eDef, p2_hp,result,player_2):
                    print(f"{player_1} acertou")
                    damage_inflicted = inflict_damage(result,eDef)
                    if damage_inflicted > 0:                    
                        p2_hp -= damage_inflicted
                        #damage_done += damage_inflicted
                        print(f"Dano causado: {damage_inflicted}")
                        print("")
                    elif damage_inflicted <= 0:
                        print(f"{player_2} resistiu ao ataque de {player_1}!")
                        damage_inflicted = 0
                    settings.any_char()
                    return p2_hp, damage_inflicted

