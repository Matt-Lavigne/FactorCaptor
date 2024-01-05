import random

from HelperFunctions import HelperFunctions
from Player import Player


class ComputerPlayer(Player):

    DIFFICULTY_LEVELS = {
        "1": "Fermat",
        "2": "Eratosthenes"
    }

    def __init__(self, difficulty_level):
        super().__init__(self.DIFFICULTY_LEVELS.get(difficulty_level, "Computer"))
        self.difficulty_level = difficulty_level

    def select_number(self, game_board):
        """
        Implementation of select_number for ComputerPlayer.
        Represents the computer's action to randomly select a number.
        """
        if self.difficulty_level == "1":
            selected_number = random.choice(game_board.numbers)
            print(f"{self.name} selected number: {selected_number}")
            HelperFunctions.continue_game()
            self.increase_score(int(selected_number))
            game_board.update_game_board(selected_number)
            game_board.update_numbers(selected_number)
            game_board.print_game_board()
            return selected_number
        else:
            selected_number = HelperFunctions.max_score_number(game_board.numbers)
            print(f"{self.name} selected number: {selected_number}")
            HelperFunctions.continue_game()
            self.increase_score(int(selected_number))
            game_board.update_game_board(selected_number)
            game_board.update_numbers(selected_number)
            game_board.print_game_board()
            return selected_number

    def select_factors(self, game_board, selected_number):
        """
        Implementation of select_factor for ComputerPlayer.
        Represents the computer's action to randomly select a factor.
        """
        factors = HelperFunctions.remaining_factors(selected_number, game_board.numbers)
        while True:
            if len(factors) == 0:
                print(f"There are no remaining factors of {selected_number} on the game board.")
                HelperFunctions.continue_game()
                break
            print(f"{self.name}, find a factor of {selected_number}!")
            if random.random() < 0.90:
                number_of_factors = len(factors)
                index_choice = random.randint(0,number_of_factors - 1)
                selected_factor = factors[index_choice]
                print(f"{self.name} selected factor: {selected_factor}")
                HelperFunctions.continue_game()
                print(f"Great! {selected_factor} is a factor of {selected_number}.")
                HelperFunctions.continue_game()
                self.increase_score(int(selected_factor))
                game_board.update_game_board(selected_factor)
                game_board.update_numbers(selected_factor)
                game_board.print_game_board()
                factors.remove(selected_factor)
            else:
                number_of_numbers = len(game_board.numbers)
                index_choice = random.randint(0, number_of_numbers - 1)
                selected_factor = game_board.numbers[index_choice]
                print(f"{self.name} selected factor: {selected_factor}")
                HelperFunctions.continue_game()
                if selected_factor in factors:
                    print(f"Great! {selected_factor} is a factor of {selected_number}.")
                    HelperFunctions.continue_game()
                    self.increase_score(int(selected_factor))
                    game_board.update_game_board(selected_factor)
                    game_board.update_numbers(selected_factor)
                    game_board.print_game_board()
                    factors.remove(selected_factor)
                else:
                    print(f"Sorry {self.name}, {selected_factor} is a not a remaining factor of {selected_number}.")
                    HelperFunctions.continue_game()
                    break
