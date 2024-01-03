from Player import Player

class HumanPlayer(Player):
    def __init__(self, name, score):
        super().__init__(name, score)

    def select_number(self):
        """
        Implementation of select_number for HumanPlayer.
        Represents the player's action to manually input a number.
        """
        try:
            selected_number = int(input(f"{self.name}, enter a number: "))
            return selected_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.select_number()

    def select_factor(self):
        """
        Implementation of select_factor for HumanPlayer.
        Represents the player's action to manually input a factor.
        """
        try:
            selected_factor = int(input(f"{self.name}, enter a factor: "))
            return selected_factor
        except ValueError:
            print("Invalid input. Please enter a valid factor.")
            return self.select_factor()