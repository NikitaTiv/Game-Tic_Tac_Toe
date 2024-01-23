import math
from utils import change_integer, separate_list


class Field:
    AVAILABLE_VALUES = [9, 16, 25]

    def __init__(self, board_size: int) -> None:
        if board_size not in self.AVAILABLE_VALUES:
            raise ValueError('You have specified an incorrect field size.')
        self.board_size = board_size
        self.cell_list = [str(digit) for digit in range(1, change_integer(self.board_size, 1, '+'))]

    def __setitem__(self, key: int, value: str) -> None:
        self.cell_list[key] = value

    @property
    def field_elde(self) -> int:
        return int(math.sqrt(self.board_size))

    def draw_field(self) -> None:
        processed_list_cell = list(separate_list(self.cell_list, self.field_elde))
        for row in processed_list_cell:
            print(''.join([f'{cell: <5}'for cell in row]))
