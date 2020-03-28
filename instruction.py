# -*- coding: utf-8 -*-
from creation_units import creation_units
from upgrade_unit import upgrade_unit, condition_upgrade, calcul_energy

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

    instructions_player_1 = str(input('What do you want to do?' + player_1))
    instructions_player_2 = str(input('What do you want to do?' + player_2))

    list_instruction_player_1 = instructions_player_1.split()
    list_instruction_player_2 = instructions_player_2.split()

    #check condition attack and move for the same

    return list_instruction_player_1, list_instruction_player_2


def fight_units(name_fighting_unit, range_fight, column_fight, points_fight):
    return

def move_unit(name_moving_unit, range_move, column_move, info_map):
    return info_map

def  transfer_energy(name_receiver_energy, name_giver_energy):
    return

def decode_instructions(list_instruction_player_1, list_instruction_player_2, player1, player2, info_map, info_peak, info_player_1, info_player_2):


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
    info_peak : dictionnary that containts infos about the peaks(str)

    Version
    ——————
    specification: Caroline Heijmans(v.1 19 / 02 / 2020)
    implementation : Marie Heneffe (v.2 25/03/2020)

    """
    list_fight_instructions = []

    for instruction in list_instruction_player_1:

        # creation units
        if ':' in instruction and not 'upgrade' in instruction:
            create_instruction = instruction.split(':')
            name_new_unit = create_instruction[0]
            type_new_unit = create_instruction[1]
            creation_units(name_new_unit, type_new_unit, 'player1', info_map, info_player_1)

        # upgrade_unit
        if 'upgrade' in instruction:
            type_of_improvement = instruction.split('upgrade:')
            upgrade_unit(type_of_improvement[1],info_player_1)

        # fight unit
        if '*' in instruction:

            name_fighting_unit = instruction.split(':')[0]
            subInstruction = instruction.split('*')[1]
            range_fight = subInstruction.split('-')[0]
            subInstruction2 = subInstruction.split('-')[1].split("=")
            column_fight = subInstruction2[0]
            points_fight = subInstruction2[1]

            list_fight_instructions += name_fighting_unit

            #move unit
        if '@' in instruction:

            name_moving_unit = instruction.split(':')[0]
            subInstruction =instruction.split('@')[1]
            range_move =subInstruction.split('-')[0]
            column_move = subInstruction.split('-')[1]

            # check unit did not attack
            for name_fighting_unit in list_fight_instructions:
                if name_moving_unit != name_fighting_unit:

                    move_unit(name_moving_unit, range_move, column_move,info_map)

        # transfer_energy
        if '<' in instruction or '>' in instruction:

            if '<' in instruction:

                name_giver_energy = None

                name_receiver_energy = instruction.split(':')[0]
                subInstruction = instruction.split('<')[1]
                range_giver_energy = subInstruction.split('-')[0]
                column_giver_energy = subInstruction.split('-')[1]

                hubs = info_map['hubs']
                peaks = info_map['peak']

                if (int(range_giver_energy), int(column_giver_energy)) in hubs:
                    name_giver_energy = hubs[(int(range_giver_energy), int(column_giver_energy))]

                elif (int(range_giver_energy), int(column_giver_energy)) in peaks:

                    name_giver_energy = peaks[(int(range_giver_energy), int(column_giver_energy))]


                if name_giver_energy is not None:

                     transfer_energy(name_receiver_energy, name_giver_energy)

            elif '>' in instruction:

                name_receiver_energy = instruction.split(':')[0]
                name_giver_energy = instruction.split('>')[1]

                transfer_energy(name_receiver_energy, name_giver_energy)


    for instruction in list_instruction_player_2:

        # creation units
        if ':' in instruction and not 'upgrade' in instruction:
            create_instruction = instruction.split(':')
            name_new_unit = create_instruction[0]
            type_new_unit = create_instruction[1]
            creation_units(name_new_unit, type_new_unit, 'player2', info_map, info_player_2)

        # upgrade_unit
        if 'upgrade' in instruction:
            type_of_improvement = instruction.split('upgrade:')
            upgrade_unit(type_of_improvement[1],info_player_2)

        # fight unit
        if '*' in instruction:
            name_fighting_unit = instruction.split(':')[0]
            subInstruction = instruction.split('*')[1]
            range_fight = subInstruction.split('-')[0]
            subInstruction2 = subInstruction.split('-')[1].split("=")
            column_fight = subInstruction2[0]
            points_fight = subInstruction2[1]

            list_fight_instructions +=name_fighting_unit

            #move unit
        if '@' in instruction:

            name_moving_unit = instruction.split(':')[0]
            subInstruction =instruction.split('@')[1]
            range_move =subInstruction.split('-')[0]
            column_move = subInstruction.split('-')[1]

            # check unit did not attack
            for name_fighting_unit in list_fight_instructions:
                if name_moving_unit != name_fighting_unit:

                    info_map = move_unit(name_moving_unit, range_move, column_move, info_map)

        # transfer_energy
        if '<' in instruction or '>' in instruction:

            if '<' in instruction:

                name_receiver_energy = instruction.split(':')[0]
                subInstruction = instruction.split('<')[1]
                range_giver_energy =subInstruction.split('-')[0]
                column_giver_energy =subInstruction.split('-')[1]

                name_giver_energy = info_map[(range_giver_energy, column_giver_energy)]

                transfer_energy(name_receiver_energy, name_giver_energy)

            elif '>' in instruction :

                name_receiver_energy =instruction.split(':')[0]
                name_giver_energy =instruction.split('>')[1]

                transfer_energy(name_receiver_energy, name_giver_energy)


    return  info_map, info_peak, info_player_1, info_player_2


