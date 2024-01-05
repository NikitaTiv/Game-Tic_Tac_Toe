from field import Field
from user import User


class Game:
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

    def is_game_finished(self) -> bool:
        for row in self.board.win_combinations:
            if self.cell_list[row[0]] == self.cell_list[row[1]] == self.cell_list[row[2]]:
                return True
        return False

    def calculate_game_result(self):
        pass

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
