from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, score):
        self._name = name
        self._score = score

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
