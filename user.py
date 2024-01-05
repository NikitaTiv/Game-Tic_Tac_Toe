from mixins import ValidateUserValueMixin


class User(ValidateUserValueMixin):
    AVAILABLE_VALUES = ['X', 'O']

    def __init__(self, user_input):
        user_symbol = user_input.upper() if user_input.islower() else user_input
        if not self.validate_initial_value(user_symbol):
            raise ValueError(f"Please choose one of these symbols: {', '.join(self.AVAILABLE_VALUES)}.")
        self.user_symbol = user_symbol

    def validate_user_move(self, user_choice: str, cell_list: list[int | str],
                           board_size: int) -> Exception | int:
        error_message = f'You need to specify a digit from 0 to {board_size}.'
        if user_choice.isdigit():
            converted_value = int(user_choice)
            if converted_value not in range(1, board_size+1):
                raise ValueError(error_message)
            if converted_value not in cell_list:
                raise IndexError(f'This cell is already filled.')
            return converted_value
        else:
            raise ValueError(error_message)

    def make_user_move(self, cell_list: list[int | str], board_size: int) -> list | None:
        user_input = input('Please make your move: ')
        processed_value = self.validate_user_move(user_input, cell_list, board_size)
        cell_list[processed_value-1] = self.user_symbol

        return cell_list
