import os
import settings

current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_directory, "battle_log.csv")

set_user = input("Digite seu Usuario: ")
game_id = None

with open (output_file,'r') as file:
    lines = file.readlines()
    count_lines = len(lines)    

    if len(lines) == 0:
        print("Sem registros de combate")
        game_id = 1      
    else: 
        for line in lines:
            battle_data = line.strip().split(',')
            if battle_data[0] == set_user:
                last_line = None
                last_line = line
            else:
                last_line = None

        if last_line is not None: 

            game_id, last_battle, last_pokemon = (int(battle_data[0])+1), battle_data[2], battle_data[3]
            print(f"Sua última luta foi em ({last_battle}) com o pokemon {last_pokemon}")
            
        else:
            game_id = (int(battle_data[0])+1)
            print("Sem registros de combate")
    
    

print()
settings.any_char()