import settings

def save_data_w(game_id,date,user, output_file, player_1, player_2, battle_n, round_n, damage_done, damage_taken):
    print("Você venceu! ")
    with open(output_file, "a") as log:        
        log.write(f'{game_id},{user},{date},{player_1}, Win,{player_2}, {battle_n}, {round_n}, {damage_done}, {damage_taken}\n')
        battle_n += 1
        round_n = 1
        damage_done = 0
        settings.any_char()


def save_data_l(game_id,date,user, output_file, player_1, player_2, battle_n, round_n, damage_done, damage_taken):
    print("Você perdeu! ")
    with open(output_file, "a") as log:        
        log.write(f'{game_id},{user},{date},{player_1}, Lost,{player_2}, {battle_n}, {round_n}, {damage_done}, {damage_taken}\n')
        battle_n += 1
        round_n = 1
        damage_done = 0
        settings.any_char()
        