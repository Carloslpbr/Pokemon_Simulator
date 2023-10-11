import os

current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_directory, "battle_log.csv")

#set_user = input("Digite seu Usuario: ")

with open (output_file,'r') as file:
    lines = file.readlines()

    for line in lines:
        battle_data = line.strip().split(',')
        last_line = None
        last_line = line

    if last_line is not None:  
        last_battle, last_pokemon = battle_data[0], battle_data[1]
        print(f"Sua última luta foi em ({last_battle}) com o pokemon {last_pokemon}")

        
    else:
        print("Sem registros de combate")

