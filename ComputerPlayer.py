import random

from Player import Player

class ComputerPlayer(Player):
    def __init__(self, name, score):
        super().__init__(name, score)

    def select_number(self):
        """
        Implementation of select_number for ComputerPlayer.
        Represents the computer's action to randomly select a number.
        """
        selected_number = random.randint(1, 100)
        print(f"{self.name} selected number: {selected_number}")
        return selected_number

    def select_factor(self):
        """
        Implementation of select_factor for ComputerPlayer.
        Represents the computer's action to randomly select a factor.
        """
        selected_factor = random.choice([2, 3, 5, 7, 11])
        print(f"{self.name} selected factor: {selected_factor}")
        return selected_factor


'''
    def computer_select_number(self, numbers):
        number_selection = random.choice(numbers)
        print("Albert selects " + str(number_selection))
        print("")
        self.set_score(number_selection)


    def computer_find_factors(self, number_selection, numbers):
        factors = find_factors(number_selection)
        for element in factors:
            if element not in numbers:
                factors.remove(element)
        if random.random() < 0.75:
            choice = factors.pop()
            print("Albert selects " + str(choice))
            print("")
            return choice
        print("Albert selects " + str(numbers[-1]))
        print("")
        return numbers[-1]
'''