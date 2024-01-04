from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name):
        self._name = name
        self._score = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def increase_score(self, value):
        self.score += value

    @abstractmethod
    def select_number(self, game_board):
        """
        Abstract method to be implemented by subclasses.
        Represents the player's action to select a number.
        """
        pass

    @abstractmethod
    def select_factor(self, game_board, selected_number):
        """
        Abstract method to be implemented by subclasses.
        Represents the player's action to select a factor.
        """
        pass

    # same for all subclasses
    def print_score(self):
        print(f"{self.name}"f's Score: {self.score}')
