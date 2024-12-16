from typing import List
from battleship.ship import Ship

class ShipManager:
    def __init__(self, ships: List[Ship]):
        self.ships = ships

    def display_ship_status(self, title: str):
        print("\n" + "="*50)
        print("\u2551" + title.center(48) + "\u2551")
        print("="*50)
        for ship in self.ships:
            status = "🔥 SUNK" if ship.is_sunk() else "\u2693 ACTIVE"
            print(f"\u2551 {ship.name:<15} | Size: {ship.size} | Status: {status:<10} \u2551")
        print("="*50)