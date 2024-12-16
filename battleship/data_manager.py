import os
import json
from typing import Dict

class DataManager:
    @staticmethod
    def load_players_data(filepath='players.json') -> Dict:
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {filepath}. Creating a new file.")
        
        # If file doesn't exist or is invalid, return an empty dictionary
        return {}

    @staticmethod
    def save_players_data(players_data: Dict, filepath='players.json'):
        try:
            with open(filepath, 'w') as f:
                json.dump(players_data, f, indent=4)
        except IOError as e:
            print(f"Error saving players data: {e}")

    @staticmethod
    def display_leaderboard(players_data: Dict):
        if not players_data:
            print("No players in the leaderboard yet.")
            return

        print("\n" + "="*50)
        print("\u2551" + "LEADERBOARD".center(48) + "\u2551")
        print("="*50)
        
        # Sort players by wins in descending order
        sorted_players = sorted(players_data.items(), key=lambda x: x[1]['wins'], reverse=True)
        
        for name, stats in sorted_players:
            print(f"\u2551 {name:<20} | Wins: {stats['wins']:<5} | Losses: {stats['losses']:<5} \u2551")
        
        print("="*50 + "\n")