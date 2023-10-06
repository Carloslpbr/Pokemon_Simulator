import random

def roll_attack_dice(pokemon,attack_p):
    dice_result = random.randint(1,20)
    print(f"{pokemon} atacou!")

    #print(f"Tirou {dice_result}")

    if dice_result == 20:
        Atk_p = round(attack_p * 0.3)
        print("CRITICAL HIT!")
    else:
        Atk_p = round(attack_p * 0.15)


    #print(f"Seu poder de ataque é {Atk_p}")
    total_power = round(dice_result+Atk_p,0)
    return Atk_p, total_power

def roll_damage_dice():
    dice_result = random.randint(1,8)
    print(dice_result)
    return dice_result


def get_defense(pokemon, deffense_p):
    dice_result = random.randint(1,20)    
    #print(f"Tirou {dice_result}")
    if dice_result == 20:
        Def_p = round(deffense_p * 0.3)
        print("ENDURE!")
    else:
        Def_p = round(deffense_p * 0.15)
    #print(f"Seu poder de defesa é {Def_p}")
    total_defense = round(dice_result+Def_p,0)
    return Def_p, total_defense


def player_actions(pokemon,attack_p):
    print("[1] Atacar, [2] Special")
    pAction = input("Digite sua ação: ")
    print("")
    if pAction == "1":
        result, power_result = roll_attack_dice(pokemon,attack_p)
        return pAction, result, power_result
    
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