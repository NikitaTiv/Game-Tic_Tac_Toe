import math
from mixins import ValidateUserValueMixin
from utils import separate_list


class Field(ValidateUserValueMixin):
    AVAILABLE_VALUES = [9, 16, 25]

    def __init__(self, board_size: int) -> None:
        if not self.validate_initial_value(board_size):
            raise ValueError('You have specified an incorrect field size.')
        self.board_size = board_size

    @property
    def field_elde(self) -> int:
        return int(math.sqrt(self.board_size))

    def draw_field(self, list_cell: list[str]) -> None:
        processed_list_cell = list(separate_list(list_cell, self.field_elde))
        for row in processed_list_cell:
            print(''.join([f'{cell: <5}'for cell in row]))
