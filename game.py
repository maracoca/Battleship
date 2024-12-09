from random import choice
from random import randint

from board import Board

columns_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
rows_dictionary = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

big_ship = 'B'
medium_ship = 'M'
small_ship = 'S'

final_hit = 'X'
miss = 'O'
hit = 'H'

hit_big_ship = 'HB'
hit_medium_ship = 'HM'
hit_small_ship = 'HS'

class Game():
    def __init__(self, user_board, computer_board, user_board_representation, computer_board_representation):
        self._user_board = user_board
        self._computer_board = computer_board
        self._user_board_representation = user_board_representation
        self._computer_board_representation = computer_board_representation

    def computer_move(self):
        hit_ships = [hit_big_ship, hit_medium_ship, hit_small_ship]

        for i in range(8):
            for j in range(8):
                state = 'next'
                if self._user_board._data[i][j] in hit_ships:

                    if self._user_board._data[i - 1][j] in hit_ships:
                        state = self.shot_if_hit(i, j, i - 1, j)

                    elif self._user_board._data[i + 1][j] in hit_ships:
                        state = self.shot_if_hit(i, j, i + 1, j)

                    elif self._user_board._data[i][j - 1] in hit_ships:
                        state = self.shot_if_hit(i, j, i, j - 1)

                    elif self._user_board._data[i][j + 1] in hit_ships:
                        state = self.shot_if_hit(i, j, i, j + 1)
                    # if state == 'hit' or state == 'miss':

                    else:
                        state = self.shot_if_hit(i, j, None, None)

                    if state == 'next':
                        continue
                    elif state == 'hit' or state == 'miss':
                        return state

        row = randint(0, 7)
        column = randint(0, 7)
        state = self._user_board.shot(row, column)

        if state == 'hit':
            return 'hit'
        elif state == 'miss':
            return 'miss'

    def shot_if_hit(self, row, column, row_for_direction, column_for_direction):
        shot = 1
        while shot > 0:
            if row_for_direction == None and column_for_direction == None:
                neighbours = [[row - 1, column], [row + 1, column], [row, column - 1], [row, column + 1]]
                point = choice(neighbours)
                state = self._user_board.shot(point[0], point[1])

                if state == 'hit':
                    return 'hit'
                elif state == 'miss':
                    return 'miss'
                elif neighbours == []:
                    return 'next'

            elif column == column_for_direction:
                neighbours = [[row - 1, column], [row + 1, column], [row_for_direction - 1, column], [row_for_direction + 1, column]]
                point = choice(neighbours)
                state = self._user_board.shot(point[0], point[1])

                if state == 'hit':
                    return 'hit'
                elif state == 'miss':
                    return 'miss'
                elif neighbours == []:
                    return 'next'

            elif row == row_for_direction:
                neighbours = [[row, column - 1], [row, column + 1], [row, column_for_direction + 1], [row, column_for_direction - 1]]
                point = choice(neighbours)
                neighbours.remove([point[0], point[1]])
                state = self._user_board.shot(point[0], point[1])

                if state == 'hit':
                    return 'hit'
                elif state == 'miss':
                    return 'miss'
                elif neighbours == []:
                    return 'next'

    def player_shot(self, row, column, computer_board):
        state = computer_board.shot(row, column)
        return state

    def start(self):
        # columns_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        # rows_dictionary = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        self.place_player_ship(self._user_board)
        self.place_computer_ship(self._computer_board)
        hit_ships = [hit_big_ship, hit_medium_ship, hit_small_ship]
        types_of_hits = [miss, final_hit]

        while self.is_win() == False:
            shot_computer = 1
            shot_user = 1

            while shot_computer > 0:
                state = self.computer_move()
                print('User board')

                for i in range(8):
                    for j in range(8):
                        if self._user_board._data[i][j] in types_of_hits:
                            self._user_board_representation._data[i][j] = self._user_board._data[i][j]

                        elif self._user_board._data[i][j] in hit_ships:
                            self._user_board_representation._data[i][j] = hit

                print(self._user_board_representation.__str__())
                if self.is_win() != False:
                    print(self.is_win())
                    return
                if state == 'miss':
                    shot_computer = 0

            while shot_user > 0:
                print('Computer board')
                print(self._computer_board_representation.__str__())

                row = (input('Enter row: ')).upper()
                column = (input('Enter collumn: ')).upper()
                if row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                    while row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                        print('invalid shot')
                        row = (input('Enter row: ')).upper()
                        column = (input('Enter collumn: ')).upper()
                row = rows_dictionary[row]
                column = columns_dictionary[column]

                state = self.player_shot(row, column, self._computer_board)
                print(state)
                print('Computer board')

                for i in range(8):
                    for j in range(8):
                        if self._computer_board._data[i][j] in types_of_hits:
                            self._computer_board_representation._data[i][j] = self._computer_board._data[i][j]

                        elif self._computer_board._data[i][j] in hit_ships:
                            self._computer_board_representation._data[i][j] = hit

                print(self._computer_board_representation.__str__())
                if self.is_win() != False:
                    print(self.is_win())
                    return
                if state == 'miss':
                    shot_user = 0



    def place_player_ship(self, user_board):

        three_ships = 3
        first_ship = 3
        second_ship = 2
        third_ship = 1
        alignment_options = ['v', 'h']
        # columns_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        # rows_dictionary = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        ships = three_ships
        print(user_board.__str__())

        while ships > 0:

            if ships == first_ship:
                ship = big_ship
                print("You are placing a big ship!(dimension of 4 squares)")
                ship_alignment = input('Enter alignment (v for vertical, h for horizontal) ').lower()

                while ship_alignment not in alignment_options:
                    print('not a valid alignment')
                    ship_alignment = input('Enter alignment (v for vertical, h for horizontal) ').lower()

                print('Enter start position of the ship ')
                row = (input('Enter row: ')).upper()
                column = (input('Enter collumn: ')).upper()

                if row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                    while row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                        print('invalid placement')
                        row = (input('Enter row: ')).upper()
                        column = (input('Enter collumn: ')).upper()

                row = rows_dictionary[row]
                column = columns_dictionary[column]  # A1 = [0, 0]

                state = user_board.place_ship(ship, row, column, ship_alignment)  # !!!!!
                if state == True:
                    ships -= 1
                    print(user_board.__str__())
                else:
                    print(state)

            elif ships == second_ship:

                ship = medium_ship
                print("You are placing a medium ship!(dimension of 3 squares)")
                ship_alignment = input('Enter alignment (v for vertical, h for horizontal) ').lower()

                while ship_alignment not in alignment_options:
                    print('not a valid alignment')
                    ship_alignment = input('Enter alignment (v for vertical, h for horizontal) ').lower()
                print('Enter start position of the ship ')
                row = (input('Enter row: ')).upper()
                column = (input('Enter collumn: ')).upper()

                if row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                    while row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                        print('invalid placement')
                        row = (input('Enter row: ')).upper()
                        column = (input('Enter collumn: ')).upper()

                row = rows_dictionary[row]
                column = columns_dictionary[column]
                state = user_board.place_ship(ship, row, column, ship_alignment)

                if state == True:
                    ships -= 1
                    print(user_board.__str__())
                else:
                    print(state)

            elif ships == third_ship:

                ship = small_ship
                print("You are placing a small ship!(dimension of 2 squares)")
                ship_alignment = input('Enter alignment (v for vertical, h for horizontal) ').lower()

                while ship_alignment not in alignment_options:
                    print('not a valid alignment')
                    ship_alignment = input('Enter alignment (v for vertical, h for horizontal) ').lower()
                print('Enter start position of the ship ')
                row = (input('Enter row: ')).upper()
                column = (input('Enter collumn: ')).upper()

                if row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                    while row not in rows_dictionary.keys() or column not in columns_dictionary.keys():
                        print('invalid placement')
                        row = (input('Enter row: ')).upper()
                        column = (input('Enter collumn: ')).upper()

                row = rows_dictionary[row]
                column = columns_dictionary[column]
                state = user_board.place_ship(ship, row, column, ship_alignment)
                if state == True:
                    ships -= 1
                    print(user_board.__str__())
                else:
                    print(state)
        return True

    def place_computer_ship(self, computer_board):
        three_ships = 3
        first_ship = 3
        second_ship = 2
        third_ship = 1

        alignment_options = ['v', 'h']

        ships = three_ships

        while ships > 0:
            if ships == first_ship:
                ship = big_ship
                alignment = choice(alignment_options)
                row = randint(0, 7)
                column = randint(0, 7)
                state = computer_board.place_ship(ship, row, column, alignment)
                if state == True:
                    ships -= 1

            elif ships == second_ship:
                ship = medium_ship
                alignment = choice(alignment_options)
                row = randint(0, 7)
                column = randint(0, 7)
                state = computer_board.place_ship(ship, row, column, alignment)
                if state == True:
                    ships -= 1

            elif ships == third_ship:
                ship = small_ship
                alignment = choice(alignment_options)
                row = randint(0, 7)
                column = randint(0, 7)
                state = computer_board.place_ship(ship, row, column, alignment)
                if state == True:
                    ships -= 1
        return True

    def is_win(self):
        total_number_of_possible_X = 9

        number_of_x_on_user_board = 0
        number_of_x_on_computer_board = 0
        for i in range(8):
            for j in range(8):
                if self._user_board._data[i][j] == final_hit:
                    number_of_x_on_user_board += 1

                if self._computer_board._data[i][j] == final_hit:
                    number_of_x_on_computer_board += 1

                if number_of_x_on_user_board == total_number_of_possible_X:
                    return 'Computer wins'

                if number_of_x_on_computer_board == total_number_of_possible_X:
                    return 'User wins'

        return False


