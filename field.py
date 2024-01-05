import math
from mixins import SplitListMixin, ValidateUserValueMixin


class Field(SplitListMixin, ValidateUserValueMixin):
    AVAILABLE_VALUES = [9, 16, 25]

    def __init__(self, board_size: int) -> None:
        if not self.validate_initial_value(board_size):
            raise ValueError('You have specified an incorrect field size.')
        self.board_size = board_size
        self.win_combinations = self.get_win_combitation()

    def get_win_combitation(self) -> list[tuple[int | int | int]]:
        pass

    @property
    def field_elde(self) -> int:
        return int(math.sqrt(self.board_size))

    def draw_field(self, list_cell: list[int | str]) -> None:
        processed_list_cell = self.get_processed_list(list_cell)
        for row in processed_list_cell:
            print(''.join([f'{cell: <5}'for cell in row]))
