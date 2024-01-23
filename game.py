import random
from enums import TicTacToeSymbol

from field import Field
from mixins import WinCombinationMixin
from user import User
from utils import change_integer, repeat_on_fail


class Game(WinCombinationMixin):
    def __getattr__(self, item):
        return False

    @repeat_on_fail
    def preparation_for_game(self) -> None:
        '''
        Make the preparation and create an initial list for the game.
        '''
        self.board: Field
        self.user: User
        self.win_combinations: list[list[int]]
        self.cell_list: list[str]
        self.pc_symbol: TicTacToeSymbol

        if not self.board:
            self.board = Field(int(input('Please enter the valid field size: ')))
        if not self.user:
            self.user = User(input('Please enter a symbol: '))
        self.win_combinations = self.get_win_combitation(self.board.board_size, self.board.field_elde)
        self.pc_symbol = self.get_pc_symbol()

    def get_pc_symbol(self) -> TicTacToeSymbol:
        pc_symbol = random.choice(list(set(TicTacToeSymbol) - {self.user.user_symbol}))
        print(f'The computer has selected a symbol {pc_symbol.value}')
        return pc_symbol

    def is_game_finished(self, whose_move: str) -> bool:
        for row in self.win_combinations:  # trying to find a winner
            if all(self.board.cell_list[row[index]] == self.board.cell_list[row[0]]
                   for index in range(1, len(row))):
                self.board.draw_field()
                print(f'The {whose_move} won this game.')
                return True
        if all((not cell.isdigit() for cell in self.board.cell_list)):  # check if it's a draw
            self.board.draw_field()
            print('It is a draw.')
            return True
        return False

    def make_pc_move(self) -> None:
        choice = int(random.choice([cell for cell in self.board.cell_list if cell.isdigit()]))
        self.board[change_integer(choice, 1, '-')] = self.pc_symbol.value
        print(f'The computer made a move on the cell {choice}')
        if not self.is_game_finished('computer'):
            self.game_process()

    def calculate_game_result(self) -> None:
        if not self.is_game_finished('player'):
            self.make_pc_move()

    def game_process(self) -> None:
        self.board.draw_field()
        self.board = self.user.make_user_move(self.board)
        self.calculate_game_result()

    def run(self) -> None:
        self.preparation_for_game()
        self.game_process()
