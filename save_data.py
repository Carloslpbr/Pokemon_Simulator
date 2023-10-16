import settings

def save_data_w(game_id,date,user, output_file, player_1, player_2, battle_n, round_n, damage_done, damage_taken,favorite_skill):
    print("Você venceu! ")
    with open(output_file, "a") as log:        
        log.write(f'{game_id},{user},{date},{player_1},Win,{player_2},{battle_n},{round_n},{damage_done},{damage_taken},{favorite_skill}\n')
        battle_n += 1
        round_n = 1
        damage_done = 0
        settings.any_char()


def save_data_l(game_id,date,user, output_file, player_1, player_2, battle_n, round_n, damage_done, damage_taken, favorite_skill):
    print("Você perdeu! ")
    with open(output_file, "a") as log:        
        log.write(f'{game_id},{user},{date},{player_1},Loss,{player_2},{battle_n},{round_n},{damage_done},{damage_taken},{favorite_skill} \n')
        battle_n += 1
        round_n = 1
        damage_done = 0
        settings.any_char()

def save_data_r(game_id,date,user, output_file, player_1, player_2, battle_n, round_n, damage_done, damage_taken,favorite_skill,battle_result):
    with open(output_file, "a",encoding='utf-8') as log:        
        log.write(f'{game_id},{user},{date},{player_1},{battle_result},{player_2},{battle_n},{round_n},{damage_done},{damage_taken},{favorite_skill}\n')
        