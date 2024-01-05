from Player import Player
from GameBoard import GameBoard
from HelperFunctions import HelperFunctions

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def select_number(self, game_board):
        """
        Implementation of select_number for HumanPlayer.
        Represents the player's action to manually input a number.
        """
        try:
            selected_number = int(input(f"{self.name}, enter a number on the game board: "))
            if selected_number in game_board.numbers:
                print(f"{self.name} selected {selected_number}.")
                game_board.update_game_board(selected_number)
                self.increase_score(selected_number)
                game_board.update_numbers(selected_number)
                game_board.print_game_board()
            return selected_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.select_number(game_board)

    def select_factors(self, game_board, selected_number):
        """
        Implementation of select_factor for HumanPlayer.
        Represents the player's action to manually input a factor.
        """
        try:
            factors = HelperFunctions.remaining_factors(selected_number, game_board.numbers)
            while True:
                if len(factors) == 0:
                    print(f"There are no remaining factors of {selected_number} on the game baord.")
                    break
                selected_factor = int(input(f"{self.name}, enter a factor: "))
                if selected_factor in factors:
                    print(f"{self.name} selected {selected_factor}.")
                    print(f"Great! {selected_factor} is a factor of {selected_number}.")
                    game_board.update_game_board(selected_factor)
                    self.increase_score(int(selected_factor))
                    game_board.update_numbers(int(selected_factor))
                    game_board.print_game_board()
                    factors.remove(selected_factor)
                else:
                    print(f"Sorry {self.name}, {selected_factor} is not a remaining factor of {selected_number}.")
                    break
        except ValueError:
            print("Invalid input. Please enter a valid factor.")

