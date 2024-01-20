from mixins import ValidateUserValueMixin
from utils import downgrade_result, repeat_on_fail


class User(ValidateUserValueMixin):
    AVAILABLE_VALUES = ['X', 'O']

    def __init__(self, user_input: str) -> None:
        user_symbol = user_input.upper() if user_input.islower() else user_input
        if not self.validate_initial_value(user_symbol):
            raise ValueError(f"Please choose one of these symbols: {', '.join(self.AVAILABLE_VALUES)}.")
        self.user_symbol = user_symbol

    def validate_user_move(self, user_choice: str, cell_list: list[str],
                           board_size: int) -> None:
        error_message = f'You need to specify a digit from 0 to {board_size}.'
        if user_choice.isdigit():
            if user_choice not in map(str, range(1, board_size+1)):
                raise ValueError(error_message)
            if user_choice not in cell_list:
                raise IndexError(f'This cell is already filled.')
        else:
            raise ValueError(error_message)

    @repeat_on_fail
    def make_user_move(self, cell_list: list[str], board_size: int) -> list:
        user_input = input('Please make your move: ')
        self.validate_user_move(user_input, cell_list, board_size)
        selected_cell_index = downgrade_result(int(user_input), 1)
        cell_list[selected_cell_index] = self.user_symbol

        return cell_list
