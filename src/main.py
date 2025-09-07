# main.py

"""
The main entry point for the Monopoly game. This file initializes the game,
sets up the PPLay window, and runs the main game loop, dispatching user
input to the GameManager and calling the UIManager to render the state.
"""

from pplay.window import Window
from game_manager import GameManager, STATE_GAME_OVER
from ui_manager import UIManager

# --- Game Configuration ---
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 900
NUM_PLAYERS = 4 # Set the number of players for the game

def main():
    """Main function to run the game."""
    # 1. Initialization
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.set_title("PPLay Monopoly")

    ui_manager = UIManager(window)
    game_manager = GameManager(NUM_PLAYERS, ui_manager)

    # 2. Game Setup
    ui_manager.assign_player_tokens(game_manager.players)
    game_manager.start_game()

    # Used to prevent rapid-fire clicks processing in a single frame
    mouse_was_pressed = False

    # 3. Main Game Loop
    while True:
        # Check for window close event
        if window.get_keyboard().key_pressed("ESC"):
            break

        # 3.1 Get Input
        action = None
        is_mouse_pressed = window.get_mouse().is_button_pressed(1)
        if is_mouse_pressed and not mouse_was_pressed:
            action = ui_manager.get_player_input(game_manager)
        mouse_was_pressed = is_mouse_pressed

        # 3.2 Update Game Logic based on Input
        game_manager.update(action)

        # 3.3 Render Graphics
        ui_manager.draw_game_state(game_manager)

        # 3.4 Update Window
        window.update()

        # 3.5 Check for Win Condition
        if game_manager.game_state == STATE_GAME_OVER:
            break

    # 4. Game Over Screen
    if game_manager.game_state == STATE_GAME_OVER:
        winner = [p for p in game_manager.players if not p.is_bankrupt][0]
        while not window.get_keyboard().key_pressed("ESC"):
            window.set_background_color((0, 0, 0))
            winner_text = f"Congratulations {winner.name}!"
            prompt_text = "Press ESC to exit"
            
            window.draw_text(winner_text, window.width / 2 - 250, window.height / 2 - 50, size=48, color=(255, 215, 0))
            window.draw_text(prompt_text, window.width / 2 - 100, window.height / 2 + 50, size=24, color=(255, 255, 255))
            
            window.update()

if __name__ == "__main__":
    main()
