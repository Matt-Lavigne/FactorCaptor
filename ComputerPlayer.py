import random
from main import find_factors


class ComputerPlayer:
    def __init__(self, name):
        self.name = "Albert"
        self.score = 0

    def get_name(self):
        return self.name

    def set_score(self, number):
        self.score = self.score + number

    def get_score(self):
        return self.score

    def print_score(self):
        print(str(self.name) + "'s Score: " + str(self.get_score()))

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