# Battleship Game - Phase 3 Project

Welcome to the **Battleship Game** project! This is a terminal-based implementation of the classic Battleship game, where a player competes against the computer to strategically sink ships.

---

## Overview

The Battleship game is a Python project designed for the terminal, where the player places their ships and takes turns attacking the computer's board to sink all its ships. The game tracks player wins and losses in a JSON file.

---

## Features

- Place ships on a 10x10 grid.
- Turn-based game play where the player and computer take turns attacking.
- Visual board display with clear indicators for hits (💥 or H), misses (💨 or M), and ship positions (X).
- Leaderboard to track player wins and losses using persistent storage (`players.json`).
- Computer that places ships and attacks randomly.

---

## Project Structure

The project is organized into components to ensure clean and maintainable code.

```
battleship_project/
|-- battleship/
|   |-- __init__.py        # Marks the directory as a package
|   |-- ship.py            # Contains the Ship class
|   |-- player.py          # Contains the Player class
|   |-- board_manager.py   # Handles board logic and display
|   |-- ship_manager.py    # Manages ship states
|   |-- data_manager.py    # Handles player data persistence
|   |-- game_manager.py    # Orchestrates game logic and flow
|-- main.py                # Entry point for the game
|-- players.json           # Stores player stats (wins/losses)
```

### Description of Components

- **`ship.py`**: Defines the `Ship` class, representing each ship's name, size, positions, and hit status.
- **`player.py`**: Manages player attributes such as name, wins, and losses.
- **`board_manager.py`**: Handles board setup, validation, ship placement, and visual display.
- **`ship_manager.py`**: Manages a fleet of ships and displays their status.
- **`data_manager.py`**: Loads and saves player stats to a JSON file for persistence.
- **`game_manager.py`**: Controls the overall game flow, including player and computer turns.
- **`main.py`**: The script to launch and play the game.

---

## How to Run the Game

Follow these steps to play the Battleship game:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Maina206/Phase-3---Python-Battleship-Game
   cd battleship_project
   ```

2. **Ensure Python is Installed**
   Verify that Python (version 3.8 or higher) is installed on your system:

   ```bash
   python --version
   ```

3. **Run the Game**
   Execute the `main.py` file to start the game:
   ```bash
   python main.py
   ```

---

## Dependencies

The project uses Python's standard libraries, so no external packages are required.

- **Python 3.8+**

---

## How to Play

1. **Game Setup**:

   - You will be prompted to enter your name.
   - Place your ships on a 10x10 grid by specifying row, column, and orientation (horizontal or vertical).
   - The computer will place its ships automatically.
   - The computer's board will not be visible to ensure fairness.

2. **Gameplay**:

   - You and the computer take turns attacking grid coordinates.
   - A hit will be marked as 💥 (or H) and a miss as 💨 (or M).

3. **Winning the Game**:

   - Sink all the computer's ships to win.
   - If the computer sinks all your ships first, it wins.

4. **Leaderboard**:
   - Your wins and losses are saved and displayed in the leaderboard.

---

## Future Improvements

Here are some planned enhancements:

- Add difficulty levels for the computer game play.
- Allow multiplayer game play over a network.
- Add some sound effects for hits, misses, and victory.

---

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvements:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a clear description of changes.

---

## License

This project is open-source and available under the MIT License.

---

Enjoy playing Battleship!
