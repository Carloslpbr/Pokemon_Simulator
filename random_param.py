import random
import random_data
import save_data
import os


limit = 10000
index = 1
max_trainers = len(random_data.trainers)-1
max_pokemon = len(random_data.pokemon_list)-1
top_players = ["lance dragon master", "red champion"]
current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_directory, "battle_log.csv")


def set_pokemon(trainer):
    if trainer == "lance dragon master":
        pokemon = random_data.lance_pokemon[random.randint(0,3)].lower()
        return pokemon
    elif trainer == "red champion":
        pokemon = random_data.red_pokemon[random.randint(0,8)].lower()
        return pokemon
    elif trainer == "ash ketchum":
        pokemon = random_data.ash_pokemon[random.randint(0,6)].lower()
        return pokemon
    elif trainer == "misty waterflower":
        pokemon = random_data.misty_pokemon[random.randint(0,4)].lower()
        return pokemon
    elif trainer == "brock rock":
        pokemon = random_data.brock_pokemon[random.randint(0,2)].lower()
        return pokemon
    else:
        pokemon = random_data.pokemon_list[random.randint(0,max_pokemon)].lower()
        return pokemon

def set_enemy_pokemon():
    combat_type = random.randint(0,100)
    if combat_type == 100:
        enemy_pokemon = random_data.legendary_pokemon[random.randint(0,4)]
        return enemy_pokemon
    else:
        enemy_pokemon = random_data.pokemon_list[random.randint(0,max_pokemon)]
        return enemy_pokemon

def set_battle_result(trainer):
    if trainer in top_players:
        if random.randint(0,10) <= 2:
            battle_result = "Loss"
            return battle_result
        else:
            battle_result = "Win"
            return battle_result
    else:
        if random.randint(0,10) <= 5:
            battle_result = "Loss"
            return battle_result
        else:
            battle_result = "Win"  
            return battle_result  

def set_damage_taken(pokemon, battle_result):
    if battle_result == "Loss":
        damage_taken = random_data.pokemon_hp[pokemon]
        return damage_taken
    else:        
        max_hp = random_data.pokemon_hp[pokemon]
        damage_taken = random.randint(1,(max_hp-1))
        return damage_taken

def set_damage_done(enemy_pokemon, battle_result):
    if battle_result == "Win":
        damage_done = random_data.pokemon_hp[enemy_pokemon]
        return damage_done
    else:
        enemy_max_hp = random_data.pokemon_hp[pokemon]
        damage_taken = random.randint(1,(enemy_max_hp-1))
        return damage_taken

def set_date(): 

    def set_day(month):
        if month == 4 or month == 6 or month == 9 or month == 11:
            day = random.randint(1,30)
            return day
        elif month == 2:
            day = random.randint(1,28)
            return day
        else:
            day = random.randint(1,31)
            return day

    def day_adjust(day):
        if day < 10:
            day_ = "0" + str(day)
            return day_
        else:
            day_ = day
            return day_

    def month_adjust(month):
        if  month < 10:
            month_ = "0" + str(month)
            return month_
        else:
            month_ = month
            return month_

    month = random.randint(1,12)
    month_ = str(month_adjust(month))
    day = set_day(month)
    day_ = str(day_adjust(day))
    year  = "2023"

    return f"{year}-{month_}-{day_}"

while index <= limit:
    battle_result = None
    battle_n = 1
    date = set_date()
    trainer = random_data.trainers[random.randint(0,max_trainers)]
    pokemon = set_pokemon(trainer)

    while battle_result != "Loss" and battle_n < 10:
        
        pokemon_max_hp = random_data.pokemon_hp[pokemon]  
        enemy_pokemon = set_enemy_pokemon()    
        battle_result = set_battle_result(trainer)
        round_n = random.randint(1,15)
        favorite_skill = random_data.pokedex[pokemon]["favorite_skill"]
        damage_taken = set_damage_taken(pokemon, battle_result)
        damage_done = set_damage_done(pokemon,battle_result)
        save_data.save_data_r(index,date,trainer,output_file,pokemon,enemy_pokemon,battle_n,round_n,damage_done, damage_taken,favorite_skill,battle_result)
        battle_n += 1
    
    index += 1

    #save_data.save_data_r(index,date,trainer,output_file,pokemon,enemy_pokemon,battle_n,round_n,damage_done, damage_taken,favorite_skill,battle_result)

