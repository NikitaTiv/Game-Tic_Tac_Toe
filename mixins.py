from typing import Iterator
from utils import convert_iteration_to_list, separate_list


class ValidateUserValueMixin:
    '''Validate an initial value for a game.'''
    AVAILABLE_VALUES: list = []

    @classmethod
    def validate_initial_value(cls, user_input: int | str) -> bool:
        if user_input not in cls.AVAILABLE_VALUES:
            return False
        return True


class WinCombinationMixin:
    @staticmethod
    def __get_vertical_win_combination(horizont_combinations: list[list[int]]) -> Iterator[list[int]]:
        for row_number in range(len(horizont_combinations)):
            yield [row[row_number] for row in horizont_combinations]

    @staticmethod
    def __get_diagonal_values(initial_list: list[list[int]], values_list: Iterator[int]) -> Iterator:
        for row in initial_list:
            index = next(values_list)
            yield row[index]

    def __get_diagonal_win_combination(self, horizont_combinations: list[list[int]],
                                       lenght: int) -> tuple[list[int], list[int]]:
        values_list = iter(range(0, lenght))
        reversed_values_list = iter(sorted(range(0, lenght), reverse=True))

        left_diagonal = convert_iteration_to_list(self.__get_diagonal_values(horizont_combinations, values_list))
        right_diagonal = convert_iteration_to_list(self.__get_diagonal_values(horizont_combinations,
                                                                              reversed_values_list))

        return left_diagonal, right_diagonal

    def get_win_combitation(self, board_size: int, lenght: int) -> list[list[int]]:
        cell_list = convert_iteration_to_list(range(board_size))

        horizont_win_combination = convert_iteration_to_list(separate_list(cell_list, lenght))
        vertical_win_combination = convert_iteration_to_list(
            self.__get_vertical_win_combination(horizont_win_combination)
        )
        diagonal_win_combination = list(
            self.__get_diagonal_win_combination(horizont_win_combination, lenght)
        )

        return horizont_win_combination + vertical_win_combination + diagonal_win_combination
