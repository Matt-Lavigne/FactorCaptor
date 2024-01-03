import random

from ComputerPlayer import ComputerPlayer
from Player import Player

###############


'''
def get_grid(grid_selection):
    if (grid_selection == '1'):
        grid = [['1','2','2','2','2','2'],
                ['2','3','3','3','3','3'],
                ['3','4','4','4','4','5'],
                ['5','5','5','6','6','7'],
                ['7','8','8','9','9','10'],
                ['10','11','12','13','14','15'],
                ['16','18','20','21','22','24'],
                ['25','26','27','28','30','32']]
        return grid
    if (grid_selection == '2'):
        grid = [['1','2','2','2','2','2','3'],
                ['3','3','3','3','4','4','4'],
                ['4','5','5','5','5','6','6'],
                ['6','7','7','8','8','9','9'],
                ['10','10','11','12','13','14','15'],
                ['16','17','18','19','20','21','22'],
                ['23','24','25','26','27','28','30'],
                ['32','33','34','35','36','38','39'],
                ['40','42','44','45','46','48','49'],
                ['50','51','52','54','55','56','60']]
        return grid
    if (grid_selection == '3'):
        grid = [['1','2','2','2','2','2','3','3'],
                ['3','3','3','3','4','4','4','4'],
                ['4','5','5','5','5','6','6','6'],
                ['6','7','7','8','8','8','9','9'],
                ['10','10','11','12','13','14','15','16'],
                ['17','18','19','20','21','22','23','24'],
                ['25','26','27','28','30','32','33','34'],
                ['35','36','38','39','40','42','44','45'],
                ['46','48','49','50','51','52','54','55'],
                ['56','60','62','64','65','66','68','70'],
                ['75','78','80','82','88','90','96','100'],
                ['101','102','104','109','112','115','118','120']]
        return grid
    else :
        grid = []
        for i in range(10):
            row = []
            for j in range(1,11):
                row.append(str(j+(i*10)))
            grid.append(row)
        return grid

def get_numbers(grid_selection):
    if (grid_selection == '1'):
        numbers = [1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,8,8,9,9,
                   10,10,11,12,13,14,15,16,18,20,21,22,24,25,26,27,28,30,32]
        return numbers
    if (grid_selection == '2'):
        numbers = [1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7,8,8,9,9,
                   10,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,
                   32,33,34,35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,60]
        return numbers
    if (grid_selection == '3'):
        numbers = [1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,7,7,8,8,8,9,9,
                10,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,33,34,
                35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,60,62,64,65,66,68,70,
                75,78,80,82,88,90,96,100,101,102,104,109,112,115,118,120]
        return numbers
    else :
        numbers = []
        for i in range(1,101):
            numbers.append(i)
        return numbers

def print_grid(grid):
    print("### FACTOR CAPTOR ###")
    #max_width = len(str(max(map(max, grid))))
    for row in grid:
        for element in row:
            #print(str(element).rjust(max_width), end=" ")
            print("{:<4}".format(element), end=" ")
        print()

def update_grid(grid, number_selection):
    found = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if number_selection == grid[i][j]:
                grid[i][j] = 'X'
                found = True
                break
        if found:
            break
    return grid

def update_numbers(numbers, number_selection):
    numbers.remove(number_selection)
    return numbers

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
        factor_choice = int(input(player2.get_name() + ", can you find another factor of " + str(number_selection) + "? "))
        if factor_choice in all_factors:
            player2.set_score(factor_choice)
            update_numbers(numbers, factor_choice)
            update_grid(grid, str(factor_choice))
            print("")
            print("Great! " + str(factor_choice) + " is a factor of " + str(number_selection) +".")
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
    return len(find_factors(number_selection)) == 2

'''


def game_start():
    print("Welcome to FACTOR CAPTOR")
    print("")
    while True:
        number_of_players = input("How many players? (1 or 2) ")
        if number_of_players == '1' or number_of_players == '2':
            break
    if number_of_players == '1':
        name = str(input("What is your name? "))
        player_one = Player(name)
        player_two = ComputerPlayer()
    else:
        name1 = str(input("What is player 1's name? "))
        player1 = Player(name1)
        name2 = str(input("What is player 2's name? "))
        player2 = Player(name2)
    print("")

def main():

#########################################################
# Press the green button in the gutter to run the script.
#########################################################
if __name__ == '__main__':

    # Game Start Menu
    #   Player vs Player or Player vs Computer?
    #       Player Names?
    #   Game board selection
    #   Roll to see who goes first

    # Player whose turn it is Selects Number on Game Board
    # Opposing Player Selects Factors of Player 1's Number Available on Game Board
    #   If Player 2 correctly selects a factor AND factors are still on game board:
    #       Player 2 selects another factor
    #   Else the turn Ends
    # Round Ends and Score is Presented
    # Loop until no numbers remain on game board

    # Ending sequence


    print("Welcome to FACTOR CAPTOR")
    print("")

    while True:
        number_of_players = input("How many players? (1 or 2) ")
        if number_of_players == '1' or number_of_players == '2':
            break
    if number_of_players == '1':
        name = str(input("What is your name? "))
        player1 = Player(name)
        computer_player = ComputerPlayer()
    else:
        name1 = str(input("What is player 1's name? "))
        player1 = Player(name1)
        name2 = str(input("What is player 2's name? "))
        player2 = Player(name2)

    print("")

    grid_selection = input("Welcome " + player1.get_name() +
                           " and " + player2.get_name() + ". Select your game board. Enter 1, 2, or 3: ")
    numbers = get_numbers(grid_selection)
    grid = get_grid(grid_selection)
    if (int(grid_selection) > 0 and int(grid_selection) < 4):
        print("Great! You've selected game board " + str(grid_selection) + ".")

    print("")

    while True:
        player1_choice = input("Alright, let's roll to see who will go first. " + player1.get_name()
                               + ", choose odd or even? ")
        if player1_choice == "odd" or player1_choice == "even":
            break
    print("Okay, " + player1.get_name() + " chose " + player1_choice + ".")
    print("Let's roll!")
    print("Rolling...")
    roll = random.randint(1,6)
    print("A " + str(roll) + " was rolled.")
    if (player1_choice == "odd" and roll % 2 == 1) or player1_choice == "even" and roll % 2 == 0:
        print(player1.get_name() + " will go first!")
        player1_turn = True
    else:
        print(player2.get_name() + " will go first!")
        player1_turn = False

    print("")

    while True:
        game_on = input("Let's play! (Press return to continue)")
        if game_on ==  '' or game_on == '\r' or game_on == '\n':
            break

    print("")

    round = 0
    if number_of_players == 1:
        while numbers:
            print_grid(grid)
            print("")
            if player1_turn:
                while True:
                    number_selection = int(input(player1.get_name() + ", choose a number of the board: "))
                    if number_selection in numbers:
                        grid = update_grid(grid, str(number_selection))
                        numbers = update_numbers(numbers, int(number_selection))
                        all_factors = find_factors(number_selection)
                        for element in all_factors:
                            if element not in numbers:
                                all_factors.remove(element)
                        computer_factor_choice = computer_player.computer_find_factors(number_selection,numbers)
                        while computer_factor_choice in all_factors:
                            computer_player.set_score(computer_factor_choice)
                            grid = update_grid(grid, str(computer_factor_choice))
                            numbers = update_numbers(numbers, computer_factor_choice)
                        player1_turn = False
                        break
            else:
                while True:
                    number_selection = int(input(player2.get_name() + ", choose a number of the board: "))
                    if number_selection in numbers:
                        grid = update_grid(grid, str(number_selection))
                        numbers = update_numbers(numbers, int(number_selection))
                        select_factors(player2, player1, number_selection, numbers, grid)
                        print("")
                        player2.set_score(number_selection)
                        print("")
                        player1_turn = True
                        break
    else:
        while numbers:
            print_grid(grid)
            print("")
            if player1_turn:
                while True:
                    number_selection = int(input(player1.get_name() + ", choose a number of the board: "))
                    if number_selection in numbers:
                        grid = update_grid(grid, str(number_selection))
                        numbers = update_numbers(numbers, int(number_selection))
                        select_factors(player1, player2, number_selection, numbers, grid)
                        print("")
                        player1.set_score(number_selection)
                        player1_turn = False

                        break
            else:
                while True:
                    number_selection = int(input(player2.get_name() + ", choose a number of the board: "))
                    if number_selection in numbers:
                        grid = update_grid(grid, str(number_selection))
                        numbers = update_numbers(numbers, int(number_selection))
                        select_factors(player2, player1, number_selection, numbers, grid)
                        print("")
                        player2.set_score(number_selection)
                        print("")
                        player1_turn = True
                        break

        round += 1
        print("###########################################")
        print("Here are the scores after Round " + str(round) + ": ")
        player1.print_score()
        player2.print_score()
        print("###########################################")
        print("")









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
