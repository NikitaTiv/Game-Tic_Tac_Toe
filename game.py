import random

from field import Field
from mixins import WinCombinationMixin
from user import User


class Game(WinCombinationMixin):
    def __getattr__(self, item):
        return False

    def preparation_for_game(self) -> None:
        '''
        Make the preparation and create an initial list for the game.
        '''
        try:
            if not self.board:
                self.board = Field(int(input('Please enter the valid field size: ')))
            if not self.user:
                self.user = User(input('Please enter a symbol: '))
        except ValueError as error:
            print(error)
            return self.preparation_for_game()

        self.cell_list = [digit for digit in range(1, self.board.board_size+1)]
        self.win_combinations = self.get_win_combitation(self.board.board_size, self.board.field_elde)
        self.pc_symbol = random.choice(list(set(self.user.AVAILABLE_VALUES) - {self.user.user_symbol}))
        print(f'The computer has selected a symbol {self.pc_symbol}')

    def is_game_finished(self, whose_move: str) -> bool:
        for row in self.win_combinations:  # trying to find a winner
            if all(self.cell_list[row[index]] == self.cell_list[row[0]] for index in range(1, len(row))):
                self.board.draw_field(self.cell_list)
                print(f'The {whose_move} won this game.')
                return True
        if all((isinstance(cell, str)for cell in self.cell_list)):  # check if it's a draw
            self.board.draw_field(self.cell_list)
            print('It is a draw.')
            return True
        return False

    def make_pc_move(self) -> None:
        choice = random.choice([cell for cell in self.cell_list if isinstance(cell, int)])
        self.cell_list[choice-1] = self.pc_symbol
        print(f'The computer made a move on the cell {choice}')
        if not self.is_game_finished('computer'):
            self.game_process()

    def calculate_game_result(self):
        if not self.is_game_finished('player'):
            self.make_pc_move()

    def game_process(self):
        self.board.draw_field(self.cell_list)
        try:
            self.cell_list = self.user.make_user_move(self.cell_list, self.board.board_size)
        except (ValueError, IndexError) as error:
            print(error)
            return self.game_process()
        self.calculate_game_result()

    def run(self):
        self.preparation_for_game()
        self.game_process()
