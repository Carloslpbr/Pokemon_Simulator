import os
import settings

current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_directory, "battle_log.csv")

set_user = input("Digite seu Usuário: ")
game_id = None
last_line = None  # Defina last_line como None inicialmente

with open(output_file, 'r') as file:
    lines = file.readlines()
    count_lines = len(lines)

    if len(lines) == 0:
        print("Nenhum combate registrado")
        game_id = 1
    else:
        for line in lines:
            battle_data = line.strip().split(',')
            if battle_data[1] == set_user:
                last_line = line  # Atualize last_line apenas se encontrar um registro correspondente

        if last_line is not None:
            battle_data = last_line.strip().split(',')
            game_id, last_battle, last_pokemon = (int(battle_data[0]), battle_data[2], battle_data[3])
            print(f"Sua última luta foi em ({last_battle}) com o Pokémon {last_pokemon}")
        else:
            game_id = int(lines[-1].strip().split(',')[0]) + 1
            print("Sem registros de combate")

print()
settings.any_char()
