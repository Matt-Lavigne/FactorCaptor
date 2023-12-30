class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_name(self):
        return self.name

    def set_score(self, number):
        self.score = self.score + number

    def get_score(self):
        return self.score

    def print_score(self):
        print(str(self.name) + ": " + str(self.get_score()))