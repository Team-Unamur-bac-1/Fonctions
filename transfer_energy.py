def transfer_energy (name_receiver_energy, name_giver_energy) :
 
    """
    Moves energy from a giver to a receiver.
 
    Parameters
    ----------
    name_receiver_energy : where energy is deposited (str)
    name_giver_energy : where the energy is taken (str)
 
 
    Returns
    ----------
    info_player_x : dictionary that contains informations about the player who just moved a new unit (str)
 
    Version
    ----------
    Specification : Gayane Harutyunyan ( v.1 22/02/2020)
    Specification : Caroline Heijmans (v.2 06/03/2020)
    """

    # Check if the receiver and giver are around each other
    if condition_transfer_energy(name_receiver_energy, name_giver_energy) == True :

        # Est ce qu'il y a besoin du nom du dico? 
        
        receiver_need = name_receiver_energy[capacity] - name_receiver_energy[energy]

        if receiver_need <= name_giver_energy[energy] :
            name_receiver_energy[energy] += receiver_need
            name_giver_energy[energy] -= receiver_need

        else :
            name_receiver_energy[energy] += name_giver_energy[energy]
            name_giver_energy[energy] = 0

        print('energy was transfered')

    else :
        print(name_giver_energy,'cant give energy to',name_receiver_energy,'because they are not next to each other')


def condition_transfer_energy(name_receiver_energy, name_giver_energy) :
 
    """
    Check proximity: must be on the same case or on the 8 neighboring boxes.
 
    Parameters
    ----------
    name_receiver_energy : where energy is deposited (str)
    name_giver_energy : where the energy is taken (str)
 
    Returns
    ----------
    condition_ok : Condition ok or ko (bool)
    
    Version
    ----------
    Specification : Gayane Harutyunyan (v.1 22/02/2020)
    Specification : Caroline Heijmans (v.2 27/03/2020)
    Implementation : Caroline Heijmans (v.1 27/03/2020)

    """
    name_receiver_energy[range]
    name_receiver_energy[column]
    name_giver_energy[range]
    name_giver_energy[column]

    # Check position
    if name_giver_energy[range] == name_receiver_energy[range] or name_giver_energy[range] == name_receiver_energy[range]-1 or name_giver_energy[range] == name_receiver_energy[range]+1 and name_giver_energy[column] == name_receiver_energy[column] or name_giver_energy[column] == name_receiver_energy[column]-1 or name_giver_energy[column] == name_receiver_energy[column]+1 :
        return True 

    else :
        return False
        print('You cant make the energy transfer bc giver is not next to receiver)




   