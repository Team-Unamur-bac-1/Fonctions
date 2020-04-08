def get_naive_IA_orders(): 
    """Returns orders from naive AI.
    
    Parameters
    ----------
   
    Returns
    -------
    orders: orders of the AI (str)
    """
    import random

    orders = ''
    list_orders = []
    to_do = random.choice(('create','transfer', 'upgrade', 'fight', 'move'))


    if to_do = 'create': 

        type = random.choice(('cruiser','tanker'))

        number = '0123456789'
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        name = ''
        for i in range(0,2):
            name += random.choice(number)
            name += random.choice(alpha)

        orders += name 
        orders +=':'
        orders += type

    elif to_do = 'upgrade':

        type = random.choice(('range','regeneration','move','storage'))

        orders += 'upgrade:'
        orders += type

    elif to_do = 'fight':

        name = random.choice(info_player_1['cruisers'])

        r = random.randit(1,40)
        c = random.randit(1,80)
        q = random.randit(1,10)

        orders += name
        orders += ':*'
        orders += r
        orders += '-'
        orders += c
        orders += '='
        orders += q
    
    elif to_do = 'move':

        name = random.choice(info_player_1['cruisers'])

        r = random.randit(1,40)
        c = random.randit(1,80)

        orders += name
        orders += ':@<'
        orders += r
        orders += '-'
        orders += c

    elif to_do = 'transfer':

        name = random.choice(info_player_1['tankers'])

        r = random.randit(1,40)
        c = random.randit(1,80)

        orders += name
        orders += ':<'
        orders += r
        orders += '-'
        orders += c

    list_orders += orders

    return list_orders




