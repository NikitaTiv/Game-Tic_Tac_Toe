import math
from mixins import SplitListMixin


class Field(SplitListMixin):
    AVAILABLE_SIZES = [9, 16, 25]

    @classmethod
    def validate_board_size(cls, board_size: int) -> Exception | bool:
        if board_size not in cls.AVAILABLE_SIZES:
            raise ValueError('You have specified an incorrect field size.')
        return True

    def __init__(self, board_size: str) -> None:
        if self.validate_board_size(board_size):
            self.board_size = board_size

    @property
    def field_elde(self) -> int:
        return int(math.sqrt(self.board_size))

    def draw_field(self, list_cell: list[int | str]) -> None:
        processed_list_cell = self.get_processed_list(list_cell)
        for row in processed_list_cell:
            print(''.join([f'{cell: <5}'for cell in row]))