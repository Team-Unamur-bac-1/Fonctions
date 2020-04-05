import colored, random

from get_instructions import get_instructions, decode_instructions

from upgrade_unit import upgrade_unit, condition_upgrade, creation_units, calcul_energy


def read_file(path):
        """Reads the file with info about the map and returns all dictionnaries nessecery tot make the game work.



        Parameters

        ----------

        path: path of file (str)



        Returns

        ----------

        info_map: dictionnary that contains info about the map

        info_peaks: dictionnary with info about peaks

        info_player_1: dictionnary with info about player 1

        info_player_2 = dictionnary with info about player 2



        """

        # open file

        fh = open(path, encoding='utf-8')

        # read file and split to get a list

        lines = fh.readlines()

        fh.close()

        # creation dictionnaries

        info_map = {}

        info_peaks = {}

        info_player_1 = {}

        info_player_2 = {}

        # get elements with index and put in info_map

        line = lines[1].split()
        info_map['nb_rows'] = int(line[0])
        info_map['nb_cols'] = int(line[1])

        lineHubs1 = lines[3].split()
        lineHubs2 = lines[4].split()

        hubs = {(int(lineHubs1[0]), int(lineHubs1[1])): 'hubs1', (int(lineHubs2[0]), int(lineHubs2[1])): 'hubs2'}
        hubs1 = {'capacity': int(lineHubs1[2]), 'rate': int(lineHubs1[3]), 'energy': int(lineHubs1[2])}
        hubs2 = {'capacity': int(lineHubs2[2]), 'rate': int(lineHubs2[3]), 'energy': int(lineHubs2[2])}
        info_player_1['hubs'] = hubs1
        info_player_2['hubs'] = hubs2
        # hubs1 = {"coordonnee": (lineHubs1[0], lineHubs1[1]), "energy": line[2], "rate": line[3]}
        # hubs2 = {"coordonnee": (line[0], line[1]), "energy": line[2], "rate": line[3]}

        info_map['hubs'] = hubs

        indice = 6

        peak={}

        while len(lines[indice].split()) > 0:

            linePeak = lines[indice].split()

            peakName = 'peak' + str(indice)
            peak[(int(linePeak[0]), int(linePeak[1]))] = peakName
            info_peaks[peakName] = int(linePeak[2])
            indice = indice + 1

        info_map['peak'] = peak


        # return

        return info_map, info_peaks, info_player_1, info_player_2


#print(read_file('C:\\plateau_energy_quest\\plateau1\\1.equ'))

def show_board(info_map):
    """

       This function display a view of the board.



       Parameters

       ----------

       info_map: data structure of the board (dict)



       Return

       --------

       board : the view of the board



       Version

       --------

       specification: Marie heneffe (v.1 13/03/2020)

       implementation : Marie Heneffe (v.1 17/03/2020)



       """

    board = '🌴' * (2 * info_map['nb_cols'] + 2) + '\n'

    for row in range(info_map['nb_rows']):

        board += '🌴'

        for col in range(info_map['nb_cols']):

            board += colored.bg(random.randint(17, 45))

            board += colored.fg(random.randint(208, 229))

            if (row, col) in info_map['hubs']:

                board += '🏝'

                if (row, col) in info_map['cruisers']:
                    board += '🚤'

                if(row, col) in info_map['tankers']:

                     board += '🚢'


            elif (row, col) in info_map['peak']:

                board += '🚨'

            elif (row,col) in info_map['cruisers']:
                board += '🚤'

            elif (row,col) in info_map['tankers']:

                board += '🚢'
            else:

                board += '~'

                board += colored.attr('reset')

        board += '🌴\n'

    board += '🌴' * (2 * info_map['nb_cols'] + 2)

    return board


#info_map = {'nb_rows': 10, 'nb_cols': 20, 'hubs': {(5, 5): 'hubs1', (9, 6): 'hubs2'}}

#print(show_board(info_map))


def creation_map(path):

    """
    This function reads a file with the informations about the map and prints a visual map. It also returns all informations about the map in a dictionnary called info_map.


    Returns
    ——————
    board_state : view of the board
    info_map: dictionnary that containt infos about the map(str)

    Version
    ——————
    specification: Caroline Heijmans(v.1 19 / 02 / 2020)
                   Marie heneffe (v.2 05/03/2020)
    implementation : Marie Heneffe (v.1 20/03/2020)

    """


map = read_file('C:\\plateau_energy_quest\\plateau1\\1.equ')

player1 = 'Fab'
player2 = 'Marie'

info_map = map[0]
info_peak = map[1]
info_player_1 = map[2]
info_player_2 = map[3]

list_of_instruction = get_instructions(player1, player2)

list_instruction_player_1 = list_of_instruction[0]
list_instruction_player_2 = list_of_instruction[1]
print(list_instruction_player_1)
print(list_instruction_player_2)

decode_instructions(list_instruction_player_1, list_instruction_player_2, player1, player2, info_map, info_peak, info_player_1, info_player_2)


print(show_board(info_map))



