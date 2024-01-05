import random

from HelperFunctions import HelperFunctions
from Player import Player


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def select_number(self, game_board):
        """
        Implementation of select_number for ComputerPlayer.
        Represents the computer's action to randomly select a number.
        """
        selected_number = random.choice(game_board.numbers)
        print(f"{self.name} selected number: {selected_number}")
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
                break
            print(f"{self.name}, find a factor of {selected_number}!")
            if random.random() < 0.90:
                number_of_factors = len(factors)
                index_choice = random.randint(0,number_of_factors - 1)
                selected_factor = factors[index_choice]
                print(f"{self.name} selected factor: {selected_factor}")
                while True:
                    continue_game = input("Press return to continue.")
                    if continue_game == "":
                        break
                print(f"Great! {selected_factor} is a factor of {selected_number}.")
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
                if selected_factor in factors:
                    print(f"Great! {selected_factor} is a factor of {selected_number}.")
                    self.increase_score(int(selected_factor))
                    game_board.update_game_board(selected_factor)
                    game_board.update_numbers(selected_factor)
                    game_board.print_game_board()
                    factors.remove(selected_factor)
                else:
                    print(f"Sorry {self.name}, {selected_factor} is a not a remaining factor of {selected_number}.")
                    break
