import random
from Player import Player

###############

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

#########################################################
# Press the green button in the gutter to run the script.
#########################################################
if __name__ == '__main__':

    print("Welcome to FACTOR CAPTOR")
    print("")

    while True:
        number_of_players = input("How many players? (1 or 2) ")
        if number_of_players == '1' or number_of_players == '2':
            break
    if number_of_players == '1':
        name = str(input("What is your name? "))
        player1 = Player(name)
        player2 = Player("Computer")
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
    else:
        print(player2.get_name() + " will go first!")

    print("")

    while True:
        game_on = input("Let's play! (Press return to continue)")
        if game_on ==  '' or game_on == '\r' or game_on == '\n':
            break

    print("")

    while numbers:
        print_grid(grid)
        while True:
            number_selection = int(input("Choose a number of the board: "))

            if number_selection in numbers:
                grid = update_grid(grid, str(number_selection))
                numbers = update_numbers(numbers, int(number_selection))
                print("")
                player1.set_score(number_selection)
                player1.print_score()
                break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
