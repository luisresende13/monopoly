# ui_manager.py

"""
This file defines the UIManager class, which handles all rendering, UI elements,
and user input processing for the Monopoly game using the PPLay module.
It acts as the view and controller in an MVC-like pattern, reading state from
the GameManager and returning user actions.
"""

import pygame
from pplay.window import Window
from pplay.mouse import Mouse
from pplay.sprite import Sprite
from pplay.gameimage import GameImage

# Type hinting for game logic objects
from typing import List, Dict, Optional, Tuple
from game_manager import GameManager
from player import Player
from dice import Dice
from cards import Card
from spaces import Property, Street
from token_animator import TokenAnimator

# --- UI Constants ---
# These coordinates are based on a 1280x900 window with a 900x900 board image.
BOARD_SIZE = 900
HUD_X_START = 910
HUD_WIDTH = 1280 - HUD_X_START

# A mapping of board space indices to pixel coordinates on the board image.
# This requires manual calibration based on the specific board image used.
# Format: (x, y)
SPACE_COORDS = [
    (800, 800), (725, 800), (650, 800), (575, 800), (500, 800), (425, 800),
    (350, 800), (275, 800), (200, 800), (125, 800), (25, 800),
    (25, 725), (25, 650), (25, 575), (25, 500), (25, 425),
    (25, 350), (25, 275), (25, 200), (25, 125), (25, 25),
    (125, 25), (200, 25), (275, 25), (350, 25), (425, 25),
    (500, 25), (575, 25), (650, 25), (725, 25), (800, 25),
    (800, 125), (800, 200), (800, 275), (800, 350), (800, 425),
    (800, 500), (800, 575), (800, 650), (800, 725)
]

# List of classic token image filenames
TOKEN_FILES = [
    "thimble.png", "wheelbarrow.png", "iron.png", "race_car.png",
    "top_hat.png", "scottie_dog.png", "boot.png", "battleship.png"
]


class UIManager:
    """
    Handles all drawing and input for the Monopoly game.
    It is stateless regarding game logic, only reflecting the state of the GameManager.
    """
    def __init__(self, window: Window):
        self.window = window
        self.mouse = Window.get_mouse()
        self.keyboard = Window.get_keyboard()

        # Load assets
        self.board_sprite = GameImage("assets/board.png")
        self.token_sprites: Dict[Player, Sprite] = {}
        self.ui_elements: Dict[str, Sprite] = {}
        self.dialog_buttons: List[Sprite] = []
        self.token_animator: Optional[TokenAnimator] = None

        self._load_ui_elements()

    def _load_ui_elements(self):
        """Loads static UI elements like buttons and dialog boxes."""
        # Main action buttons
        self.ui_elements['roll_button'] = Sprite("assets/ui/button_roll.png")
        self.ui_elements['roll_button'].set_position(HUD_X_START + 50, 700)
        
        self.ui_elements['manage_button'] = Sprite("assets/ui/button_manage.png")
        self.ui_elements['manage_button'].set_position(HUD_X_START + 50, 760)

        # Dialog assets
        self.ui_elements['dialog_box'] = Sprite("assets/ui/dialog_box.png")
        self.ui_elements['dialog_box'].set_position(self.window.width / 2 - self.ui_elements['dialog_box'].width / 2,
                                                    self.window.height / 2 - self.ui_elements['dialog_box'].height / 2)
        
        self.ui_elements['card_dialog'] = Sprite("assets/ui/card_dialog.png")
        self.ui_elements['card_dialog'].set_position(self.window.width / 2 - self.ui_elements['card_dialog'].width / 2,
                                                     self.window.height / 2 - self.ui_elements['card_dialog'].height / 2)

    def assign_player_tokens(self, players: List[Player]):
        """Creates a token sprite for each player."""
        for i, player in enumerate(players):
            token_file = TOKEN_FILES[i % len(TOKEN_FILES)]
            sprite = Sprite(f"assets/tokens/{token_file}")
            self.token_sprites[player] = sprite
            player.token_sprite = sprite # Link sprite back to player model

    def draw_game_state(self, game_manager: GameManager):
        """The main drawing function, called every frame from the main loop."""
        self.window.set_background_color((0, 50, 0)) # Dark green background
        
        self.draw_board()
        self.draw_player_tokens(game_manager.players, game_manager.current_player)
        self.draw_player_hud(game_manager.players, game_manager.current_player)
        self.draw_dice(game_manager.dice)

        # Draw context-sensitive UI based on game state
        state = game_manager.game_state
        if state == "PLAYER_MOVING":
            if self.token_animator:
                self.token_animator.update(self.window.delta_time())
                if self.token_animator.is_finished:
                    game_manager.finish_player_movement(self.token_animator.card_move, self.token_animator.new_position)
                    self.token_animator = None
        elif state == "AWAITING_ROLL" or state == "JAIL_TURN":
            self.ui_elements['roll_button'].draw()
            self.ui_elements['manage_button'].draw()
        
        elif state == "AWAITING_BUY_DECISION":
            space = game_manager.board.get_space_at(game_manager.current_player.position)
            self.display_decision_dialog(
                title=f"Buy {space.name}?",
                message=f"Price: ${space.price}",
                options=["Buy", "Auction"]
            )
        
        elif state == "AWAITING_TAX_CHOICE":
            player = game_manager.current_player
            tax_space = game_manager.board.get_space_at(player.position)
            percentage_tax = int(player.get_total_worth() * 0.10)
            self.display_decision_dialog(
                title="Income Tax",
                message=f"Pay ${tax_space.tax_amount} or 10% (${percentage_tax})",
                options=[f"Pay ${tax_space.tax_amount}", "Pay 10%"]
            )
        
        # Add more state-based drawing calls here (e.g., for cards, auctions)

        elif state == "MANAGE_PROPERTIES":
            self.draw_manage_properties_screen(game_manager)

    def draw_board(self):
        """Draws the main game board."""
        self.board_sprite.draw()

    def start_token_animation(self, player: Player, start_pos: int, end_pos: int, card_move: bool = False):
        """Initializes and starts a token animation."""
        token_sprite = self.token_sprites[player]
        self.token_animator = TokenAnimator(token_sprite, start_pos, end_pos, SPACE_COORDS)
        self.token_animator.card_move = card_move
        self.token_animator.new_position = end_pos

    def draw_player_tokens(self, players: List[Player], current_player: Player):
        """Draws each player's token at their correct position on the board."""
        positions_count = {}
        
        # Draw static tokens first
        for player in players:
            if player.is_bankrupt:
                continue

            # If a token is animating, its sprite will be drawn separately
            if self.token_animator and player == current_player:
                continue

            pos_index = player.position
            if pos_index in positions_count:
                positions_count[pos_index] += 1
            else:
                positions_count[pos_index] = 0
            
            offset = positions_count[pos_index] * 10 # Offset tokens on the same space
            
            base_x, base_y = SPACE_COORDS[pos_index]
            token_sprite = self.token_sprites[player]
            token_sprite.set_position(base_x + offset, base_y + offset)
            token_sprite.draw()

        # Draw the animating token on top
        if self.token_animator:
            self.token_animator.sprite.draw()

    def draw_player_hud(self, players: List[Player], current_player: Player):
        """Displays information for each player in the HUD area."""
        y_pos = 20
        self.window.draw_text("Players", HUD_X_START + 10, y_pos, size=24, color=(255, 255, 0), bold=True)
        y_pos += 40

        for player in players:
            color = (255, 255, 0) if player == current_player else (255, 255, 255)
            
            if player.is_bankrupt:
                self.window.draw_text(f"{player.name} (Bankrupt)", HUD_X_START + 10, y_pos, size=18, color=(128, 128, 128))
                y_pos += 50
                continue

            self.window.draw_text(f"{player.name}", HUD_X_START + 10, y_pos, size=20, color=color, bold=(player == current_player))
            y_pos += 25
            self.window.draw_text(f"Money: ${player.money}", HUD_X_START + 20, y_pos, size=18, color=color)
            y_pos += 25
            if player.in_jail:
                self.window.draw_text(f"Status: In Jail", HUD_X_START + 20, y_pos, size=16, color=(255, 100, 100))
                y_pos += 20

            y_pos += 25 # Spacer

    def draw_dice(self, dice: Dice):
        """Displays the result of the last dice roll."""
        roll = dice.last_roll
        if roll != (0, 0):
            text = f"Roll: {roll[0]} + {roll[1]} = {sum(roll)}"
            self.window.draw_text(text, HUD_X_START + 50, 650, size=24, color=(255, 255, 255), bold=True)

    def display_decision_dialog(self, title: str, message: str, options: List[str]):
        """
        Creates an interactive dialog box with a title, message, and clickable options.
        """
        dialog_box = self.ui_elements['dialog_box']
        dialog_box.draw()
        
        # Draw text
        title_x = dialog_box.x + (dialog_box.width - len(title) * 18) / 2 # Rough centering
        self.window.draw_text(title, title_x, dialog_box.y + 20, size=32, color=(0,0,0), bold=True)
        
        msg_x = dialog_box.x + (dialog_box.width - len(message) * 10) / 2
        self.window.draw_text(message, msg_x, dialog_box.y + 80, size=20, color=(0,0,0))

        # Draw buttons
        self.dialog_buttons.clear()
        total_button_width = sum(150 for _ in options) + (len(options) - 1) * 20
        start_x = dialog_box.x + (dialog_box.width - total_button_width) / 2
        
        for option in options:
            # Assuming generic button asset, text will be drawn on top
            button = Sprite("assets/ui/button_generic.png")
            button.set_position(start_x, dialog_box.y + 150)
            button.draw()
            
            text_x = button.x + (button.width - len(option) * 10) / 2
            self.window.draw_text(option, text_x, button.y + 15, size=20, color=(0,0,0))
            
            # Store the sprite with its action name for input checking
            button.action = option.upper() 
            self.dialog_buttons.append(button)
            start_x += button.width + 20

    def display_card(self, card: Card):
        """Shows the text of a drawn Chance or Community Chest card."""
        card_box = self.ui_elements['card_dialog']
        card_box.draw()
        
        # Simple text wrapping
        words = card.text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 > 35: # Character limit per line
                lines.append(current_line)
                current_line = word
            else:
                current_line += " " + word
        lines.append(current_line)
        
        y_pos = card_box.y + 40
        for line in lines:
            line_x = card_box.x + (card_box.width - len(line.strip()) * 8) / 2
            self.window.draw_text(line.strip(), line_x, y_pos, size=18, color=(0,0,0))
            y_pos += 25
            
        # OK button
        ok_button = Sprite("assets/ui/button_generic.png")
        ok_button.set_position(card_box.x + (card_box.width - ok_button.width) / 2, card_box.y + card_box.height - 70)
        ok_button.draw()
        self.window.draw_text("OK", ok_button.x + 65, ok_button.y + 15, size=20, color=(0,0,0))
        ok_button.action = "DISMISS"
        self.dialog_buttons = [ok_button]

    def get_player_input(self, game_manager: GameManager) -> Optional[Dict]:
        """
        Checks for mouse clicks on UI elements based on the current game state
        and returns a dictionary representing the chosen action.
        """
        if not self.mouse.is_button_pressed(1):
            return None # Only process left clicks

        state = game_manager.game_state

        if state == "AWAITING_ROLL" or state == "JAIL_TURN":
            if self.mouse.is_over_object(self.ui_elements['roll_button']):
                return {'type': 'ROLL_DICE'}
            if self.mouse.is_over_object(self.ui_elements['manage_button']):
                return {'type': 'MANAGE_PROPERTIES'}

        elif state == "AWAITING_BUY_DECISION":
            for button in self.dialog_buttons:
                if self.mouse.is_over_object(button):
                    if button.action == "BUY":
                        return {'type': 'BUY_PROPERTY'}
                    elif button.action == "AUCTION":
                        return {'type': 'AUCTION_PROPERTY'}

        elif state == "AWAITING_TAX_CHOICE":
            for button in self.dialog_buttons:
                if self.mouse.is_over_object(button):
                    if "PAY $" in button.action:
                        return {'type': 'PAY_TAX', 'choice': 'flat'}
                    elif "PAY 10%" in button.action:
                        return {'type': 'PAY_TAX', 'choice': 'percentage'}
        
        # Add checks for other states with dialogs (e.g., card dismissal)
        
        elif state == "MANAGE_PROPERTIES":
            for button in self.dialog_buttons:
                if self.mouse.is_over_object(button):
                    if button.action == "BACK":
                        return {'type': 'BACK_TO_GAME'}
                    elif button.action == "BUILD":
                        return {'type': 'BUILD', 'property': button.property}
                    elif button.action == "MORTGAGE":
                        return {'type': 'MORTGAGE', 'property': button.property}

        return None

    def draw_manage_properties_screen(self, game_manager: GameManager):
        """Draws the UI for managing properties (building, mortgaging)."""
        # Draw a semi-transparent overlay
        overlay = pygame.Surface((self.window.width, self.window.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.window.screen.blit(overlay, (0, 0))

        # Title
        self.window.draw_text("Manage Properties", self.window.width / 2 - 200, 50, size=36, color=(255, 255, 255), bold=True)

        # Player's properties list
        y_pos = 120
        self.dialog_buttons.clear()
        for prop in game_manager.current_player.properties:
            self.window.draw_text(prop.name, 100, y_pos, size=24, color=(255, 255, 255))

            # Add buttons for actions
            x_pos = 400
            if isinstance(prop, Street):
                build_button = Sprite("assets/ui/button_generic.png")
                build_button.set_position(x_pos, y_pos)
                build_button.draw()
                self.window.draw_text("Build", build_button.x + 50, build_button.y + 15, size=24, color=(0, 0, 0))
                build_button.action = "BUILD"
                build_button.property = prop
                self.dialog_buttons.append(build_button)
                x_pos += 200

            mortgage_button = Sprite("assets/ui/button_generic.png")
            mortgage_button.set_position(x_pos, y_pos)
            mortgage_button.draw()
            self.window.draw_text("Mortgage", mortgage_button.x + 30, mortgage_button.y + 15, size=24, color=(0, 0, 0))
            mortgage_button.action = "MORTGAGE"
            mortgage_button.property = prop
            self.dialog_buttons.append(mortgage_button)

            y_pos += 60

        # Back button
        back_button = Sprite("assets/ui/button_generic.png")
        back_button.set_position(self.window.width / 2 - back_button.width / 2, self.window.height - 100)
        back_button.draw()
        self.window.draw_text("Back", back_button.x + 50, back_button.y + 15, size=24, color=(0, 0, 0))
        back_button.action = "BACK"
        self.dialog_buttons.append(back_button)
