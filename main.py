
def get_grid(grid_selection):
    if (grid_selection == 1):
        grid = [['1','2','2','2','2','2'],
                ['2','3','3','3','3','3'],
                ['3','4','4','4','4','5'],
                ['5','5','5','6','6','7'],
                ['7','8','8','9','9','10'],
                ['10','11','12','13','14','15'],
                ['16','18','20','21','22','24'],
                ['25','26','27','28','30','32']]
        return grid
    if (grid_selection == 2):
        grid = [[1,2,2,2,2,2,3],
                [3,3,3,3,4,4,4],
                [4,5,5,5,5,6,6],
                [6,7,7,8,8,9,9],
                [10,10,11,12,13,14,15],
                [16,17,18,19,20,21,22],
                [23,24,25,26,27,28,30],
                [32,33,34,35,36,38,39],
                [40,42,44,45,46,48,49],
                [50,51,52,54,55,56,60]]
        return grid
    if (grid_selection == 3):
        grid = [[1,2,2,2,2,2,3,3],
                [3,3,3,3,4,4,4,4],
                [4,5,5,5,5,6,6,6],
                [6,7,7,8,8,8,9,9],
                [10,10,11,12,13,14,15,16],
                [17,18,19,20,21,22,23,24],
                [25,26,27,28,30,32,33,34],
                [35,36,38,39,40,42,44,45],
                [46,48,49,50,51,52,54,55],
                [56,60,62,64,65,66,68,70],
                [75,78,80,82,88,90,96,100],
                [101,102,104,109,112,115,118,120]]
        return grid
    else :
        grid = []
        for i in range(10):
            row = []
            for j in range(1,11):
                row.append(j+(i*10))
            grid.append(row)
        return grid

def get_numbers(grid_selection):
    if (grid_selection == 1):
        numbers = [1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,8,8,9,9,
                   10,10,11,12,13,14,15,16,18,20,21,22,24,25,26,27,28,30,32]
        return numbers
    if (grid_selection == 2):
        numbers = [1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7,8,8,9,9,
                   10,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,
                   32,33,34,35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,60]
        return numbers
    if (grid_selection == 3):
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
    name = input("What is your name? ")
    print("")
    grid_selection = int(input("Welcome " + name + ". Select your game board. Enter 1, 2, or 3: "))
    numbers = get_numbers(grid_selection)
    if (grid_selection > 0 and grid_selection < 4):
        print("Great! You've selected game board " + str(grid_selection) + ".")
    print("")

    '''
    turn = input("Would you like to go first or second? Enter 1 to go first or 2 to go second: ")
    if (turn == '1'):
        print("Ok " + name + ", you'll be going first!")
    else:
        print("Ok " + name + ", you'll be going second!")
    print("")
    '''
    while True:
        game_on = input("Let's play! (Press return to continue)")

        if game_on ==  '' or game_on == '\r' or game_on == '\n':
            break

    print("")
    grid = get_grid(grid_selection)
    # Determine the width of the field based on the maximum number of digits in the array
    print_grid(grid)
    print("")
    while numbers:
        while True:
            number_selection = int(input("Choose a number of the board: "))

            if number_selection in numbers:
                grid = update_grid(grid, str(number_selection))
                numbers = update_numbers(numbers, int(number_selection))
                print("")
                break
        print_grid(grid)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
