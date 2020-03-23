# -*- coding: utf-8 -*-
def condition_regeneration():
    """
    Checked if capacity is full.
    Parameters
    ______
    Returns
    _______
    info_player_x : dictionary that contains informations about the player who just moved a new unit (str)
    Version
    ________
    Specification : Gayane Harutyunyan ( v.1 23/02/2020)
    Specification : Maxence Weyns ( v.1 20/03/2020)
    Implementation : Maxence Weyns ( v.1 20/03/2020)

    """

    if info_player_1['hub_1']['energy'] == 750:

        print('You can not have more energy in your hub')
        return False

    else:

        print('You can regenerate the energy in the hub')
        return True


def regeneration_hub(regeneration_rate, numb_hub):
    """
        This function automatically regenerates energy at the hubs without exceeding their capacities.
    Parameters
    _______
    numb_hub : number of the hub
    regeneration_rate : rate of the regeneration of the hub
    Returns
    _______
    info_player_x : dictionary that contains informations about the player who just moved a new unit (str)
    Version
    _____
    Spécification : Gayane Harutyunyan ( v.1 22/02/2020)
    Spécification : Maxence Weyns ( v.2 20/03/2020)
    Implementation : Maxence Weyns ( v.1 20/03/2020)
    """

    if condition_regeneration == True:

        if numb_hub == 'hub_1':
            info_player_1['hub_1']['energy'] += regeneration_rate

        if numb_hub == 'hub_2':
            info_player_2['hub_2']['energy'] += regeneration_rate

    else:
        print('You can not regenerate your hub')
