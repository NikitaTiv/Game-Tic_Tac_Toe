from field import Field
from user import User


class Game:
    def preparation_for_game(self) -> None:
        '''
        Make the preparation and create an initial list for the game.
        '''
        try:
            if not self.board:
                self.board = Field(int(input('Please enter the valid field size: ')))
            if not self.user:
                self.user = User(input('Please enter a symbol: '))
        except ValueError as e:
            print(e)
            self.preparation_for_game()

        self.cell_list = [digit for digit in range(1, self.board.board_size+1)]

    def validate_user_move(self, user_choice: int) -> Exception | int:
        if user_choice not in range(1, user_choice+1):
            return ValueError(f'You need to specify a digit from 0 to {len(self.cell_list)}.')
        if user_choice not in self.cell_list:
            return ValueError(f'This cell is already filled.')

        return user_choice

    def game_process(self):
        self.board.draw_field(self.cell_list)
        user_input = self.validate_user_move(int(input('Please make your move: ')))

    def __getattr__(self, item):
        return False

    def run(self):
        self.preparation_for_game()
        self.game_process()
