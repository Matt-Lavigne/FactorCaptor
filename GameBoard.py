class GameBoard:
    def __init__(self, game_board_choice):
        self.game_board_choice = game_board_choice
        self.game_board = self.get_game_board()
        self.numbers = self.get_numbers()

    def get_game_board(self):
        if self.game_board_choice == '1':
            game_board = [['1', '2', '2', '2', '2', '2'],
                    ['2', '3', '3', '3', '3', '3'],
                    ['3', '4', '4', '4', '4', '5'],
                    ['5', '5', '5', '6', '6', '7'],
                    ['7', '8', '8', '9', '9', '10'],
                    ['10', '11', '12', '13', '14', '15'],
                    ['16', '18', '20', '21', '22', '24'],
                    ['25', '26', '27', '28', '30', '32']]
            return game_board
        if self.game_board_choice == '2':
            game_board = [['1', '2', '2', '2', '2', '2', '3'],
                    ['3', '3', '3', '3', '4', '4', '4'],
                    ['4', '5', '5', '5', '5', '6', '6'],
                    ['6', '7', '7', '8', '8', '9', '9'],
                    ['10', '10', '11', '12', '13', '14', '15'],
                    ['16', '17', '18', '19', '20', '21', '22'],
                    ['23', '24', '25', '26', '27', '28', '30'],
                    ['32', '33', '34', '35', '36', '38', '39'],
                    ['40', '42', '44', '45', '46', '48', '49'],
                    ['50', '51', '52', '54', '55', '56', '60']]
            return game_board
        if self.game_board_choice == '3':
            game_board = [['1', '2', '2', '2', '2', '2', '3', '3'],
                    ['3', '3', '3', '3', '4', '4', '4', '4'],
                    ['4', '5', '5', '5', '5', '6', '6', '6'],
                    ['6', '7', '7', '8', '8', '8', '9', '9'],
                    ['10', '10', '11', '12', '13', '14', '15', '16'],
                    ['17', '18', '19', '20', '21', '22', '23', '24'],
                    ['25', '26', '27', '28', '30', '32', '33', '34'],
                    ['35', '36', '38', '39', '40', '42', '44', '45'],
                    ['46', '48', '49', '50', '51', '52', '54', '55'],
                    ['56', '60', '62', '64', '65', '66', '68', '70'],
                    ['75', '78', '80', '82', '88', '90', '96', '100'],
                    ['101', '102', '104', '109', '112', '115', '118', '120']]
            return game_board
        else:
            game_board = []
            for i in range(10):
                row = []
                for j in range(1, 11):
                    row.append(str(j + (i * 10)))
                game_board.append(row)
            return game_board

    def get_numbers(self):
        if self == '1':
            numbers = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
                       10, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32]
            return numbers
        if self == '2':
            numbers = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9,
                       10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30,
                       32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 60]
            return numbers
        if self == '3':
            numbers = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9,
                       10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34,
                       35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 60, 62, 64, 65, 66, 68, 70,
                       75, 78, 80, 82, 88, 90, 96, 100, 101, 102, 104, 109, 112, 115, 118, 120]
            return numbers
        else:
            numbers = []
            for i in range(1, 101):
                numbers.append(i)
            return numbers

    def print_game_board(self):
        print("### FACTOR CAPTOR ###")
        # max_width = len(str(max(map(max, grid))))
        for row in self.game_board:
            for element in row:
                # print(str(element).rjust(max_width), end=" ")
                print("{:<4}".format(element), end=" ")
            print()

    def update_game_board(self, number_selection):
        found = False
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[0])):
                if number_selection == self.game_board[i][j]:
                    self.game_board[i][j] = 'X'
                    found = True
                    break
            if found:
                break

    def update_numbers(self, number_selection):
        self.numbers.remove(number_selection)



    '''''
    def select_factors(player1, player2, number_selection, numbers, grid):
        print(player1.get_name() + " chose " + str(number_selection) + ".")
        print("")
        print_grid(grid)
        print("")

        all_factors = find_factors(number_selection)
        for element in all_factors:
            if element not in numbers:
                all_factors.remove(element)

        found_all_factors = True

        while all_factors:
            factor_choice = int(
                input(player2.get_name() + ", can you find another factor of " + str(number_selection) + "? "))
            if factor_choice in all_factors:
                player2.set_score(factor_choice)
                update_numbers(numbers, factor_choice)
                update_grid(grid, str(factor_choice))
                print("")
                print("Great! " + str(factor_choice) + " is a factor of " + str(number_selection) + ".")
                print("")
                print_grid(grid)
                print("")
                all_factors.remove(factor_choice)
            elif factor_choice not in all_factors:
                print("Sorry, " + str(factor_choice) + " is not a remaining factor of " + str(number_selection) + ".")
                print("")
                found_all_factors = False
                break
            elif factor_choice not in numbers:
                print("You must choose a number on the game board.")

        if found_all_factors:
            print("There are no other factors of " + str(number_selection) + " remaining on the board.")
            print("")
    '''

    def check_factor(factor_choice, number_selection, numbers):
        if factor_choice in numbers and number_selection % factor_choice == 0:
            return True
        return False

    def find_factors(number_selection):
        factors = []
        for i in range(1, number_selection + 1):
            if number_selection % i == 0:
                factors.append(i)
        return factors

    def is_prime(number_selection):
        return len(number_selection.find_factors(number_selection)) == 2

