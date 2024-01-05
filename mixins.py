class SplitListMixin:
    def get_processed_list(self, list_of_cells) -> list:
        '''
        Transform a list of results into a printable list.
        '''
        list_for_printing = []
        start_index = 0
        for number in range(1, len(list_of_cells)+1):
            if number % self.field_elde == 0:
                list_for_printing.append(list_of_cells[start_index:number])
                start_index = number
        return list_for_printing


class ValidateUserValueMixin:
    '''Validate an initial value for a game.'''
    @classmethod
    def validate_initial_value(cls, user_input: str) -> bool:
        if user_input not in cls.AVAILABLE_VALUES:
            return False
        return True
