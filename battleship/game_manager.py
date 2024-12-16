from battleship.board_manger import BoardManager
from battleship.ship_manager import ShipManager
from battleship.data_manager import DataManager
from battleship.ship import Ship
import random

class GameManager:
    def __init__(self):
        self.board_manager = BoardManager()
        self.player_ships = ShipManager([
            Ship("Aircraft Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2)
        ])
        self.computer_ships = ShipManager([
            Ship("Aircraft Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2)
        ])
        self.data_manager = DataManager()
        self.players_data = self.data_manager.load_players_data()

    def player_turn(self):
        while True:
            try:
                print("\nYour turn to attack!")
                row = int(input("Enter row number to attack (0-9): "))
                col_letter = input("Enter column letter to attack (A-J): ")
                col = self.board_manager.convert_column_to_index(col_letter)

                if 0 <= row < self.board_manager.board_size and 0 <= col < self.board_manager.board_size:
                    if self.board_manager.player_guess_board[row][col] != ' ':
                        print("You already attacked this position!")
                        continue
                    if self.board_manager.check_hit(row, col, self.board_manager.computer_board, self.computer_ships.ships):
                        print("Direct Hit!")
                        self.board_manager.player_guess_board[row][col] = 'H'
                        return True
                    else:
                        print("Miss!")
                        self.board_manager.player_guess_board[row][col] = 'M'
                        return False
                else:
                    print("Invalid coordinates. Please try again.")
            except (ValueError, IndexError):
                print("Please enter valid coordinates (Row: 0-9, Column: A-J).")

    def computer_turn(self):
        while True:
            row = random.randint(0, self.board_manager.board_size - 1)
            col = random.randint(0, self.board_manager.board_size - 1)
            if self.board_manager.player_board[row][col] not in ['H', 'M']:
                print(f"\n Computer attacks position ({row}, {self.board_manager.column_labels[col]})")
                if self.board_manager.check_hit(row, col, self.board_manager.player_board, self.player_ships.ships):
                    print("Computer hit your ship!")
                    self.board_manager.player_board[row][col] = 'H'
                    return True
                else:
                    print("Computer missed!")
                    self.board_manager.player_board[row][col] = 'M'
                    return False

    def play(self):
        print("\n" + "="*50)
        print("WELCOME TO BATTLESHIP".center(48))
        print("="*50)

        self.data_manager.display_leaderboard(self.players_data)

        player_name = input("Enter your name: ")
        if player_name not in self.players_data:
            self.players_data[player_name] = {"wins": 0, "losses": 0}

        print("\n Place your ships:")
        for ship in self.player_ships.ships:
            while True:
                print(f"\nPlacing {ship.name} (size: {ship.size})")
                self.board_manager.display_board(self.board_manager.player_board, "YOUR BOARD")
                try:
                    row = int(input(f"Enter starting row (0-9) for {ship.name}: "))
                    col_letter = input(f"Enter starting column (A-J) for {ship.name}: ")
                    col = self.board_manager.convert_column_to_index(col_letter)
                    is_horizontal = input("Place horizontally? (y/n): ").lower() == 'y'

                    if self.board_manager.is_valid_placement(self.board_manager.player_board, ship, row, col, is_horizontal):
                        self.board_manager.place_ship(self.board_manager.player_board, ship, row, col, is_horizontal)
                        break
                except (ValueError, IndexError):
                    print(" Please enter valid coordinates (Row: 0-9, Column: A-J).")

        print("\n Computer is placing ships...")
        self.board_manager.place_computer_ships(self.computer_ships.ships)

        while True:
            print("\n" + "="*50)
            self.board_manager.display_board(self.board_manager.player_board, "YOUR BOARD")
            self.board_manager.display_board(self.board_manager.player_guess_board, "YOUR ATTACKS")
            self.player_ships.display_ship_status("YOUR SHIPS STATUS")
            self.computer_ships.display_ship_status("COMPUTER'S SHIPS STATUS")

            if self.player_turn():
                if all(ship.is_sunk() for ship in self.computer_ships.ships):
                    print(f"\n Congratulations {player_name}! You won!")
                    self.players_data[player_name]["wins"] += 1
                    break

            if self.computer_turn():
                if all(ship.is_sunk() for ship in self.player_ships.ships):
                    print("\n Computer wins! Better luck next time!")
                    self.players_data[player_name]["losses"] += 1
                    break

        self.data_manager.save_players_data(self.players_data)