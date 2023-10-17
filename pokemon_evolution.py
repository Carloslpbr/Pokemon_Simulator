
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
load_file = os.path.join(current_directory, "pokemons.csv")
load_file_2 = os.path.join(current_directory, "evolution_chain.csv")
save_file = os.path.join(current_directory,"pokemon_evolution.csv")

evolutions = {}

with open(load_file_2, 'r', encoding='utf8') as file_2:
    lines_2 = file_2.readlines()  
    for chain in lines_2: 
        evolution_chain = chain.strip().split(",")    
        for pokemon in evolution_chain:
            pokemon = pokemon.strip().strip('"')            
            evolutions[pokemon] = evolution_chain

with open(load_file, 'r', encoding='utf8') as file:
    lines = file.readlines()  
    
    for line in lines:

        pk = line.strip().split(",")
        pk_ = pk[0].strip().split('"')
        pokemon = pk_[1]   
        
        evolution_chain = evolutions.get(pokemon, [])
        
        while len(evolution_chain) < 4:
            evolution_chain.append(None)
  
        base, ev1, ev2, ev3 = evolution_chain        

        with open(save_file, 'a', encoding = 'utf8') as file_3:
            file_3.write(f"{pokemon},{base},{ev1},{ev2},{ev3}\n")     
        
