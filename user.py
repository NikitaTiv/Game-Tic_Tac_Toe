from enums import TicTacToeSymbol
from field import Field
from utils import change_integer, repeat_on_fail


class User:
    def __init__(self, user_input: str) -> None:
        user_symbol = user_input.upper() if user_input.islower() else user_input
        self.user_symbol = TicTacToeSymbol(user_symbol)

    def validate_user_move(self, user_choice: str, cell_list: list[str],
                           board_size: int) -> None:
        error_message = f'You need to specify a digit from 0 to {board_size}.'
        if user_choice.isdigit():
            if user_choice not in map(str, range(1, change_integer(board_size, 1, '+'))):
                raise ValueError(error_message)
            if user_choice not in cell_list:
                raise IndexError(f'This cell is already filled.')
        else:
            raise ValueError(error_message)

    @repeat_on_fail
    def make_user_move(self, board: Field) -> Field:
        user_input = input('Please make your move: ')
        self.validate_user_move(user_input, board.cell_list, board.board_size)
        selected_cell_index = change_integer(int(user_input), 1, '-')
        board[selected_cell_index] = self.user_symbol.value

        return board
