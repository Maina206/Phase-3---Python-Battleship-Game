import random
from typing import List
from battleship.ship import Ship

class BoardManager:
    def __init__(self, board_size: int = 10):
        self.board_size = board_size
        self.player_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.computer_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.player_guess_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.column_labels = [chr(i) for i in range(ord('A'), ord('A') + board_size)]

    def is_valid_placement(self, board: List[List[str]], ship: Ship, start_row: int, start_col: int, is_horizontal: bool) -> bool:
        if is_horizontal:
            if start_col + ship.size > self.board_size:
                print("❌ Error: Ship placement exceeds board boundaries!")
                return False
            for i in range(ship.size):
                if board[start_row][start_col + i] != ' ':
                    print("❌ Error: Space already occupied by another ship!")
                    return False
        else:
            if start_row + ship.size > self.board_size:
                print("❌ Error: Ship placement exceeds board boundaries!")
                return False
            for i in range(ship.size):
                if board[start_row + i][start_col] != ' ':
                    print("❌ Error: Space already occupied by another ship!")
                    return False
        return True

    def place_ship(self, board: List[List[str]], ship: Ship, start_row: int, start_col: int, is_horizontal: bool):
        positions = []
        if is_horizontal:
            for i in range(ship.size):
                board[start_row][start_col + i] = 'S'
                positions.append((start_row, start_col + i))
        else:
            for i in range(ship.size):
                board[start_row + i][start_col] = 'S'
                positions.append((start_row + i, start_col))
        ship.positions = positions

    def display_board(self, board: List[List[str]], title: str = ""):
        print("\n" + "="*41)
        if title:
            print(f"{title:^41}")
            print("="*41)

        print("   ", end="")
        for col in self.column_labels:
            print(f"  {col} ", end="")
        print("\n   +" + "---+"*self.board_size)

        for i in range(self.board_size):
            print(f" {i} |", end="")
            for j in range(self.board_size):
                cell = board[i][j]
                if cell == ' ':
                    print("   |", end="")
                elif cell == 'S':
                    print(" ⛴ |", end="")
                elif cell == 'H':
                    print(" 💥 |", end="")
                elif cell == 'M':
                    print(" 💨 |", end="")
            print("\n   +" + "---+"*self.board_size)

    def check_hit(self, row: int, col: int, board: List[List[str]], ships: List[Ship]) -> bool:
        if board[row][col] == 'S':
            board[row][col] = 'H'
            for ship in ships:
                if (row, col) in ship.positions:
                    ship.hits += 1
                    if ship.is_sunk():
                        print(f"\u2728 You sunk the {ship.name}!")
            return True
        return False

    def place_computer_ships(self, ships: List[Ship]):
        for ship in ships:
            while True:
                is_horizontal = random.choice([True, False])
                if is_horizontal:
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - ship.size)
                else:
                    row = random.randint(0, self.board_size - ship.size)
                    col = random.randint(0, self.board_size - 1)

                if self.is_valid_placement(self.computer_board, ship, row, col, is_horizontal):
                    self.place_ship(self.computer_board, ship, row, col, is_horizontal)
                    break

    def convert_column_to_index(self, col_letter: str) -> int:
        return self.column_labels.index(col_letter.upper())