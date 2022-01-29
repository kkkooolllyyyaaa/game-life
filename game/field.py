from game.cell import Cell
import random


class Field:
    __height = 0
    __width = 0
    __game_field = []

    def __init__(self, height, width):
        assert height > 0 and width > 0
        self.__height = height
        self.__width = width
        self.__game_field = self.__get_default()
        return

    @property
    def game_field(self):
        return self.__game_field

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def next(self):
        new_list = self.__get_default()
        for i in range(0, self.height):
            for j in range(0, self.width):
                current = self.get_cell(i, j)
                if current.alive:
                    new_list = self.__process_alive(i, j, new_list)
                else:
                    new_list = self.__process_dead(i, j, new_list)
        self.__game_field = new_list

    def get_neighbours(self, i, j):
        neighbours = []
        positions = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                     [0, 1], [1, -1], [1, 0], [1, 1]]
        for shift in positions:
            new_i = int(i + shift[0])
            new_j = int(j + shift[1])
            if self.__is_in_field(new_i, new_j):
                neighbours.append(self.get_cell(new_i, new_j))
        return neighbours

    def fill_random(self):
        self.__game_field = [[Cell(random.randint(0, 1))
                              for _ in range(self.width)]
                             for _ in range(self.height)]
        return

    def to_str(self):
        ret_str = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                ret_str += self.get_cell(i, j).to_str()
            ret_str += '\n'
        return ret_str

    def get_cell(self, i, j):
        return self.game_field[i][j]

    def set_cell(self, i, j, query):
        self.game_field[i][j] = query
        return

    def __process_alive(self, i, j, new_list):
        neighbours = self.get_neighbours(i, j)
        cnt = 0
        for cell in neighbours:
            if cell.alive:
                cnt += 1
        if cnt < 2 or cnt > 3:
            new_list[i][j] = self.get_cell(i, j).get_mutated()
        else:
            new_list[i][j] = self.get_cell(i, j)
        return new_list

    def __process_dead(self, i, j, new_list):
        neighbours = self.get_neighbours(i, j)
        cnt = 0
        for cell in neighbours:
            if cell.alive:
                cnt += 1
        if cnt == 3:
            new_list[i][j] = self.get_cell(i, j).get_mutated()
        else:
            new_list[i][j] = self.get_cell(i, j)
        return new_list

    def __get_default(self):
        new_field = [[Cell(False)
                      for _ in range(self.width)]
                     for _ in range(self.height)]
        return new_field

    def __is_in_field(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width
