import random

from GameBoard import GameBoard
from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer

    ### Game Overview ###
    #
    # Game Start Menu
    #   Player vs Player or Player vs Computer?
    #       Player Names?
    #   Game board selection
    #   Roll to see who goes first
    #
    # Player whose turn it is Selects Number on Game Board
    # Opposing Player Selects Factors of Player 1's Number Available on Game Board
    #   If Player 2 correctly selects a factor AND factors are still on game board:
    #       Player 2 selects another factor
    #   Else the turn Ends
    # Round Ends and Score is Presented
    # Loop until no numbers remain on game board
    #
    # Ending sequence
    #####################

def main():

    print("Welcome to Factor Captor!")

    # Get player_one's name
    player_one_name = input("Enter your name, player one: ")
    player_one = HumanPlayer(player_one_name)

    # Choose opponent: another person or computer
    opponent_choice = input(f"{player_one.name}, do you want to play against another person or the computer? "
                            f"Enter 'person' or 'computer': ")

    if opponent_choice.lower() == 'person':
        player_two_name = input("Enter the name for player two: ")
        player_two = HumanPlayer(player_two_name)
    elif opponent_choice.lower() == 'computer':
        player_two = ComputerPlayer("Computer")
    else:
        print("Invalid choice. Exiting the game.")
        return

    # Choose game board: 1, 2, or 3
    board_choice = input("Choose a game board (enter 1, 2, or 3): ")

    # Create GameBoard based on user's input
    game_board = GameBoard(board_choice)

    print(f"{player_one.name} vs {player_two.name}! Let the game begin with Game Board {board_choice}!")

    # Determine who goes first by rolling a die
    player_one_odd_even_choice = input(f"Let's roll the dice to see who will go first! {player_one.name}, "
                                       f"choose odd or even: ").lower()
    print("Rolling...")
    dice_roll = random.randint(1, 6)
    print(f"The dice has rolled: {dice_roll}")

    if (dice_roll % 2 == 0 and player_one_odd_even_choice == 'even') or \
            (dice_roll % 2 != 0 and player_one_odd_even_choice == 'odd'):
        print(f"{player_one.name} goes first!")
        current_player, next_player = player_one, player_two
    else:
        print(f"{player_two.name} goes first!")
        current_player, next_player = player_two, player_one

    # Start the game loop
    round = 0
    while game_board.numbers:
        game_board.print_game_board()

        # current_player's turn
        selected_number = current_player.select_number(game_board)

        # print(f"{current_player.get_name()} selected number {selected_number}. Score: {current_player.score}")

        # next_player's turn
        next_player.select_factors(game_board, selected_number)

        # print end-of-round scores
        round += 1
        print("###########################################")
        print(f"Here are the scores after Round {round}: ")
        player_one.print_score()
        player_two.print_score()
        print("###########################################")
        print("")

        # Switch players for the next turn
        current_player, next_player = next_player, current_player

    # Game over, determine the winner
    if player_one.score > player_two.score:
        print(f"{player_one.name} wins with a score of {player_one.score}!")
    elif player_two.score > player_one.score:
        print(f"{player_two.name} wins with a score of {player_two.score}!")
    else:
        print("It's a tie!")


#########################################################
# Press the green button in the gutter to run the script.
#########################################################
if __name__ == '__main__':
    main()
