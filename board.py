from texttable import Texttable


big_ship = 'B'
medium_ship = 'M'
small_ship = 'S'
vertical_ship = 'v'
horizontal_ship = 'h'

final_hit = 'X'
miss = 'O'
hit = 'H'

hit_big_ship = 'HB'
hit_medium_ship = 'HM'
hit_small_ship = 'HS'

class Board():
    def __init__(self):
        self._data = []
        for i in range(8):
            self._data.append([' '] * 8)

    def __str__(self):
        t = Texttable()
        t.header([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        for i in range(8):
            t.add_row([i + 1] + self._data[i])
        return t.draw()


    def is_ship(self, x, y):
        if self._data[x][y] in [small_ship, medium_ship, big_ship]:
            return True
        return False


    def place_ship(self, ship, row, column, ship_alingment):
        minimum_starting_position_big_ship = 4
        minimum_starting_position_medium_ship = 5
        minimum_starting_position_small_ship = 6

        if ship == big_ship:
            if self.is_ship(row, column):
                return ('Ship already placed here')

            else:
                if ship_alingment == vertical_ship and row > minimum_starting_position_big_ship:
                    return ('Ship exceeds the map')

                elif ship_alingment == horizontal_ship and column > minimum_starting_position_big_ship:
                    return ('Ship exceeds the map')

                else:
                    if ship_alingment == vertical_ship:
                        for i in range(1, 4):  # Check the next 3 rows
                            if self.is_ship(row + i, column):
                                return 'Ship already placed here'

                            else:
                                for i in range(row, row + 4):
                                    self._data[i][column] = big_ship
                                return True


                    elif ship_alingment == horizontal_ship:
                        for i in range(1, 4):
                            if self.is_ship(row, column + i):
                                return 'Ship already placed here'

                            else:
                                for j in range(column, column + 4):
                                    self._data[row][j] = big_ship
                                return True

                    else:
                        return ('not a valid allignment')

        if ship == medium_ship:
            if self.is_ship(row, column):
                return ('Ship already placed here')

            else:
                if ship_alingment == vertical_ship and row > minimum_starting_position_medium_ship:
                    return ('Ship exceeds the map')

                elif ship_alingment == horizontal_ship and column > minimum_starting_position_medium_ship:
                    return ('Ship exceeds the map')

                else:
                    if ship_alingment == vertical_ship:
                        for i in range(1, 3):
                            if self.is_ship(row + i, column):
                                return 'Ship already placed here'

                            else:
                                for i in range(row, row + 3):
                                    self._data[i][column] = medium_ship
                                return True


                    elif ship_alingment == horizontal_ship:
                        for i in range(1, 3):
                            if self.is_ship(row, column + i):
                                return 'Ship already placed here'

                            else:
                                for j in range(column, column + 3):
                                    self._data[row][j] = medium_ship
                                return True

                    else:
                        return ('not a valid allignment')

        if ship == small_ship:
            if self.is_ship(row, column):
                return ('Ship already placed here')

            else:
                if ship_alingment == vertical_ship and row > minimum_starting_position_small_ship:
                    return ('Ship exceeds the map')

                elif ship_alingment == horizontal_ship and column > minimum_starting_position_small_ship:
                    return ('Ship exceeds the map')

                else:
                    if ship_alingment == vertical_ship:
                        if self.is_ship(row + 1, column) == True:
                            return ('Ship already placed here')

                        else:
                            for i in range(row, row + 2):
                                self._data[i][column] = small_ship
                            return True

                    elif ship_alingment == horizontal_ship:
                        if self.is_ship(row, column + 1) == True:
                            return ('Ship already placed here')

                        else:
                            for j in range(column, column + 2):
                                self._data[row][j] = small_ship
                            return True

                    else:
                        return ('not a valid allignment')



    def shot(self, row, column):
        if row < 0 or row > 7 or column < 0 or column > 7:
            return ('invalid shot')

        elif self._data[row][column] in [big_ship, medium_ship, small_ship]:
            total_hits_big_ship = 0
            total_hits_medium_ship = 0
            total_hits_small_ship = 0

            if self._data[row][column] == big_ship:
                self._data[row][column] = hit_big_ship
                for i in range(8):
                    for j in range(8):
                        if self._data[i][j] == hit_big_ship:
                            total_hits_big_ship += 1

                if total_hits_big_ship == 4:
                    for i in range(8):
                        for j in range(8):
                            if self._data[i][j] == hit_big_ship:
                                self._data[i][j] = final_hit

            elif self._data[row][column] == medium_ship:
                self._data[row][column] = hit_medium_ship
                for i in range(8):
                    for j in range(8):
                        if self._data[i][j] == hit_medium_ship:
                            total_hits_medium_ship += 1

                if total_hits_medium_ship == 3:
                    for i in range(8):
                        for j in range(8):
                            if self._data[i][j] == hit_medium_ship:
                                self._data[i][j] = final_hit

            elif self._data[row][column] == small_ship:
                self._data[row][column] = hit_small_ship
                for i in range(8):
                    for j in range(8):
                        if self._data[i][j] == hit_small_ship:
                            total_hits_small_ship += 1

                if total_hits_small_ship == 2:
                    for i in range(8):
                        for j in range(8):
                            if self._data[i][j] == hit_small_ship:
                                self._data[i][j] = final_hit

            return 'hit'
        elif self._data[row][column] == ' ':
            self._data[row][column] = miss
            return 'miss'

        elif self._data[row][column] == miss or self._data in [hit_big_ship, hit_medium_ship, hit_small_ship] or self._data == hit:
            return ("You already shot here")


    def neighbours(self, row, column):
        ship_types = [big_ship, medium_ship, small_ship]
        '''looks around the neighboors of a ship and returns True if it finds a ship'''
        if row + 1 < 8 and self._data[row + 1][column] in ship_types:
            return True
        if row - 1 >= 0 and self._data[row - 1][column] in ship_types:
            return True
        if column + 1 < 8 and self._data[row][column + 1] in ship_types:
            return True
        if column - 1 >= 0 and self._data[row][column - 1] in ship_types:
            return True
        return False


