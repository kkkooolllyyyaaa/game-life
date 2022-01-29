from game.field import Field
from game import my_util
from typing import Final
import time

WELCOME_STR: Final = 'Начало работы программы\nВведите размеры поля'


class GameProcessor:
    fld = None

    def start(self):
        print(WELCOME_STR)
        self.__input_params()
        self.__input_game_rules()

    def __input_params(self):
        i = self.__input_positive('Высота')
        j = self.__input_positive('Ширина')
        self.fld = Field(int(i), int(j))
        self.fld.fill_random()

    def __input_game_rules(self):
        print('Выберите режим игры:')
        print('[auto] - вывод каждые n секунд')
        print('[step-by-step] - вы сами управляете игрой')
        print('[exit] - выйти')

        input_str = input()
        if input_str.__eq__('auto'):
            self.__play_auto()
        elif input_str.__eq__('step-by-step'):
            self.__play_step_by_step()
        elif input_str.__eq__('exit'):
            exit(0)
        else:
            print('Нет режима ' + input_str)
            self.__input_game_rules()
        pass

    def __play_auto(self):
        print('Для игры в автоматическом режиме введите число n - периодичность вывода на экран (в сек. )')
        interval = self.__input_positive('Задержка вывода сек. ')
        while True:
            self.fld.next()
            print(self.fld.to_str())
            time.sleep(interval)


    def __play_step_by_step(self):
        print('Для игры в ручном режиме вы можете вводить целые числа, и смотреть состояние поля через n '
              'ходов, где n - введенное число')
        while True:
            nsteps = self.__input_positive('Количество шагов')
            for i in range(0, int(nsteps)):
                self.fld.next()
                print(self.fld.to_str())

    def __input_positive(self, x):
        self.__welcome_x(x)
        input_str = input()
        if input_str.__eq__('exit'):
            exit(0)
        if my_util.is_int(input_str) and int(input_str) > 0:
            return int(input_str)
        self.__error_x(x, 'должно быть целым положительным числом')
        return self.__input_positive(x)

    def __welcome_x(self, x):
        print(x + ': ')
        return

    def __error_x(self, x, message):
        print('Произошла ошибка при вводе' + ' ' + x + ' ' + message)
        return
