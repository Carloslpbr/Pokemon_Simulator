import os
current_directory = os.path.dirname(os.path.abspath(__file__))
load_file = os.path.join(current_directory, "pokemons.csv")
load_file_2 = os.path.join(current_directory, "evolution_chain.csv")

def compare(criteria_1, criteria_2):
    if criteria_1 == criteria_2:
        return True
    else:
        return False
    
with open(load_file, 'r', encoding='utf8') as file:
    lines = file.readlines()
    for line in lines:

        base = None
        ev1 = None
        ev2 = None

        pk = line.strip().split(",")
        pk_ = pk[0].strip().split('"')
        pokemon = pk_[1]        
        
        with open(load_file_2, 'r', encoding='utf8') as file_2:
            lines_2 = file_2.readlines()
            for chain in lines_2:                
                evolution_chain = chain.strip().split(",")

                base_evolution_ = evolution_chain[0]
                chain_evolution_2 = evolution_chain[1]

                try:
                    chain_evolution_3 = evolution_chain[2]
                except IndexError:
                    chain_evolution_3 = None
                    
                if compare(base_evolution_, pokemon) == True:                   
                    base = pokemon
                    ev1 = chain_evolution_2 
                    ev2 = chain_evolution_3
                
                elif compare(chain_evolution_2, pokemon) == True:
                    base = base_evolution_
                    ev1 = pokemon                    
                    ev2 = chain_evolution_3
                                 
                elif compare(chain_evolution_3, pokemon) == True:
                    base = base_evolution_
                    ev1 = chain_evolution_2                   
                    ev2 = pokemon
        if base == None and ev1 == None and ev2 == None:
            ...
        else:
            print(f'Evoluções de {pokemon} = {base}, {ev1}, {ev2}')