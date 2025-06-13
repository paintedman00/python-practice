# 2048 Game (Python Console Version)

This is a simple console version of the famous [2048](https://en.wikipedia.org/wiki/2048_(video_game)) puzzle game, written in Python. Move and merge numbers on a 4x4 grid to reach the 2048 tile!

## How to Play

- Use the keyboard commands to move the tiles:
  - `W` or `w` - Move Up
  - `A` or `a` - Move Left
  - `S` or `s` - Move Down
  - `D` or `d` - Move Right

After every move, a new tile (with the value 2) will appear at a random empty position. Combine tiles with the same number to merge them and increase their value. The goal is to create a tile with the number **2048**.

## Files

- `2048.py` - The main game loop and user interface.
- `logic.py` - All the core game logic and helper functions.

## Getting Started

1. Make sure you have Python 3 installed.
2. Download both `2048.py` and `logic.py` into the same directory.
3. Open a terminal in that directory.
4. Run the game with:
    ```bash
    python main.py
    ```

## License

This project is provided for educational purposes.