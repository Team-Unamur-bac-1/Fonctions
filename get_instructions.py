def get_instructions(player_1, player_2):
 
    """
    This function asks 2 players what they want to do during the round. It takes as parameter the names of the 2 players.

    Parameters
    ——————
    player_1: name of player 1(str)
    player_2: name of player 2(str)
 
    Returns
    ——————
    list_instruction_player_1 = list with instructions of player 1 (str)
    list_instruction_player_2 = list with instructions of player 2 (str)
    
    Version
    ——————
    specification: Caroline Heijmans(v.1 19 / 02 / 2020)
    specification: Caroline Heijmans(v.2 28 / 02 / 2020)
    implementation: Caroline Heijmans(v.1 28 / 02 / 2020)
    """
    
    instructions_player_1 = str(input('What do you want to do?', player_1)
    instructions_player_2 = str(input('What do you want to do?', player_2)

    list_instruction_player_1 = instructions_player_1.split()
    list_instruction_player_2 = instructions_player_2.split()
    
                                
   

    return list_instruction_player_1, list_instruction_player_2


def decode_instructions(list_instruction_player_1, list_instruction_player_2):
 
"""
Decodes the instructions of the player to make them work.
 
Parameters
——————
list_instruction_player_1 = list with instructions of player 1 (str)
list_instruction_player_2 = list with instructions of player 2 (str)
 
Returns
——————
info_player_1: dictionnary that containts infos player 1 (str)
info_player_2: dictionnary that containts infos about player 2 (str)
info_map: dictionnary that containts infos about the map(str)
 
Version
——————
specification: Caroline Heijmans(v.1 19 / 02 / 2020)
 
"""
# initialize list to check move and fight conditions later
list_fight_instructions = []                                
                                
for instruction in list_instruction_player_1:

    if ':' and not 'upgrade' in instruction:
        # creation units

        create_instruction = instruction.split(':')

        name_new_unit = create_instruction[0]
        type_new_unit = create_instruction[1]

        creation_units(name_new_unit, type_new_unit, player)

for instruction in list_instruction_player_2:
    
    if ':' and not 'upgrade' in instruction:
        # creation units

        create_instruction = instruction.split(':')

        name_new_unit = create_instruction[0]
        type_new_unit = create_instruction[1]

        creation_units(name_new_unit, type_new_unit, player)

for instruction in list_instruction_player_1:

    if 'upgrade' in instruction:
        # upgrade_unit

        type_of_improvement = instruction.split('upgrade:')

        upgrade_unit(type_of_improvement) 

for instruction in list_instruction_player_2:

    if 'upgrade' in instruction:
        # upgrade_unit

        type_of_improvement = instruction.split('upgrade:')

        upgrade_unit(type_of_improvement) 

for instruction in list_instruction_player_1:

    if '*' in instruction:
        # fight unit

        fighting_instruction = instruction.split('*','-','=')
        list_fight_instructions += fighting_instruction                       

        name_fighting_unit = fighting_instruction[0]
        range_fight = fighting_instruction[1]
        column_fight = fighting_instruction[2]
        points_fight = fighting_instruction[3]

        fight_units(name_fighting_unit,range_fight,column_fight, points_fight)

for instruction in list_instruction_player_2:

    if '*' in instruction:
        # fight unit

        fighting_instruction = instruction.split('*','-','=')
        list_fight_instructions += fighting_instruction                        

        name_fighting_unit = fighting_instruction[0]
        range_fight = fighting_instruction[1]
        column_fight = fighting_instruction[2]
        points_fight = fighting_instruction[3]

        fight_units(name_fighting_unit,range_fight,column_fight, points_fight)

for instruction in list_instruction_player_1:

    if '@' in instruction:
        # move_unit  

        moving_instruction = instruction_split('@','-')
        
        #check unit did not attack                        
        for fight_instruction in list_fight_instructions :
            if moving_instruction[0] != fight_instruction[0] :
                                
                name_moving_unit = moving_instruction[0]
                range_move = moving_instruction[1]
                column_move = moving_instruction[2]

                move_unit(name_moving_unit, range_move, column_move)                    

for instruction in list_instruction_player_2:

    if '@' in instruction:
        # move_unit  

        moving_instruction = instruction_split('@','-')
                                
        #check unit did not attack                        
        for fight_instruction in list_fight_instructions :
            if moving_instruction[0] != fight_instruction[0] :
                                
                name_moving_unit = moving_instruction[0]
                range_move = moving_instruction[1]
                column_move = moving_instruction[2]

                move_unit(name_moving_unit, range_move, column_move)                           

for instruction in list_instruction_player_1:

    if '<' and '>' in instruction:
        # transfer_energy

        if '<' in instruction:

            transfer_instruction = instruction.split(':<','-')

            name_receiver_energy =  transfer_instruction[0]
            range_giver_energy = transfer_instruction[1]
            column_giver_energy = transfer_instruction[2]
            
            name_giver_energy = info_map[(range_giver_energy,column_giver_energy)]

            transfer_energy(name_receiver_energy, name_giver_energy)

        elif '>' in instruction:

            transfer_instruction = instruction.split(':>')

            name_receiver_energy = transfer_instruction[0]
            name_giver_energy = transfer_instruction[1]

                    transfer_energy(name_receiver_energy, name_giver_energy)

for instruction in list_instruction_player_2:

    if '<' and '>' in instruction:
        # transfer_energy

        if '<' in instruction:

            transfer_instruction = instruction.split(':<','-')

            name_receiver_energy =  transfer_instruction[0]
            range_giver_energy = transfer_instruction[1]
            column_giver_energy = transfer_instruction[2]
            
            name_giver_energy = info_map[(range_giver_energy,column_giver_energy)]

            transfer_energy(name_receiver_energy, name_giver_energy)

        elif '>' in instruction:

            transfer_instruction = instruction.split(':>')

            name_receiver_energy = transfer_instruction[0]
            name_giver_energy = transfer_instruction[1]

                    transfer_energy(name_receiver_energy, name_giver_energy)
