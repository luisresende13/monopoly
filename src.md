## Tree for src
```
├── constants.py
├── dice.py
├── board.py
├── token_animator.py
├── ui_manager.py
├── cards.py
├── game_manager.py
├── main.py
├── spaces.py
├── player.py
└── bank.py
```

## File: constants.py
```python
# constants.py

"""
This file centralizes all static data from the "Additional Information" document.
It avoids "magic numbers" in the code and makes the game easier to maintain.
"""

# Game Parameters
STARTING_MONEY = 1500
GO_SALARY = 200
JAIL_FINE = 50
INCOME_TAX_FLAT = 200
INCOME_TAX_PERCENTAGE = 0.10
LUXURY_TAX = 75
MORTGAGE_INTEREST_RATE = 0.10
TOTAL_HOUSES = 32
TOTAL_HOTELS = 12
BOARD_SIZE = 40
JAIL_POSITION = 10

# Board Data: A list of dictionaries, one for each space on the board.
BOARD_DATA = [
    {'type': 'Corner', 'name': 'GO', 'corner_type': 'GO'},
    {'type': 'Street', 'name': 'Mediterranean Avenue', 'color_group': 'Brown', 'price': 60, 'rent_levels': [2, 10, 30, 90, 160, 250], 'mortgage': 30, 'house_cost': 50},
    {'type': 'Card', 'name': 'Community Chest', 'deck_type': 'Community Chest'},
    {'type': 'Street', 'name': 'Baltic Avenue', 'color_group': 'Brown', 'price': 60, 'rent_levels': [4, 20, 60, 180, 320, 450], 'mortgage': 30, 'house_cost': 50},
    {'type': 'Tax', 'name': 'Income Tax', 'tax_amount': 200},
    {'type': 'Railroad', 'name': 'Reading Railroad', 'price': 200, 'mortgage': 100},
    {'type': 'Street', 'name': 'Oriental Avenue', 'color_group': 'Light Blue', 'price': 100, 'rent_levels': [6, 30, 90, 270, 400, 550], 'mortgage': 50, 'house_cost': 50},
    {'type': 'Card', 'name': 'Chance', 'deck_type': 'Chance'},
    {'type': 'Street', 'name': 'Vermont Avenue', 'color_group': 'Light Blue', 'price': 100, 'rent_levels': [6, 30, 90, 270, 400, 550], 'mortgage': 50, 'house_cost': 50},
    {'type': 'Street', 'name': 'Connecticut Avenue', 'color_group': 'Light Blue', 'price': 120, 'rent_levels': [8, 40, 100, 300, 450, 600], 'mortgage': 60, 'house_cost': 50},
    {'type': 'Corner', 'name': 'Jail / Just Visiting', 'corner_type': 'Jail'},
    {'type': 'Street', 'name': 'St. Charles Place', 'color_group': 'Pink', 'price': 140, 'rent_levels': [10, 50, 150, 450, 625, 750], 'mortgage': 70, 'house_cost': 100},
    {'type': 'Utility', 'name': 'Electric Company', 'price': 150, 'mortgage': 75},
    {'type': 'Street', 'name': 'States Avenue', 'color_group': 'Pink', 'price': 140, 'rent_levels': [10, 50, 150, 450, 625, 750], 'mortgage': 70, 'house_cost': 100},
    {'type': 'Street', 'name': 'Virginia Avenue', 'color_group': 'Pink', 'price': 160, 'rent_levels': [12, 60, 180, 500, 700, 900], 'mortgage': 80, 'house_cost': 100},
    {'type': 'Railroad', 'name': 'Pennsylvania Railroad', 'price': 200, 'mortgage': 100},
    {'type': 'Street', 'name': 'St. James Place', 'color_group': 'Orange', 'price': 180, 'rent_levels': [14, 70, 200, 550, 750, 950], 'mortgage': 90, 'house_cost': 100},
    {'type': 'Card', 'name': 'Community Chest', 'deck_type': 'Community Chest'},
    {'type': 'Street', 'name': 'Tennessee Avenue', 'color_group': 'Orange', 'price': 180, 'rent_levels': [14, 70, 200, 550, 750, 950], 'mortgage': 90, 'house_cost': 100},
    {'type': 'Street', 'name': 'New York Avenue', 'color_group': 'Orange', 'price': 200, 'rent_levels': [16, 80, 220, 600, 800, 1000], 'mortgage': 100, 'house_cost': 100},
    {'type': 'Corner', 'name': 'Free Parking', 'corner_type': 'FreeParking'},
    {'type': 'Street', 'name': 'Kentucky Avenue', 'color_group': 'Red', 'price': 220, 'rent_levels': [18, 90, 250, 700, 875, 1050], 'mortgage': 110, 'house_cost': 150},
    {'type': 'Card', 'name': 'Chance', 'deck_type': 'Chance'},
    {'type': 'Street', 'name': 'Indiana Avenue', 'color_group': 'Red', 'price': 220, 'rent_levels': [18, 90, 250, 700, 875, 1050], 'mortgage': 110, 'house_cost': 150},
    {'type': 'Street', 'name': 'Illinois Avenue', 'color_group': 'Red', 'price': 240, 'rent_levels': [20, 100, 300, 750, 925, 1100], 'mortgage': 120, 'house_cost': 150},
    {'type': 'Railroad', 'name': 'B. & O. Railroad', 'price': 200, 'mortgage': 100},
    {'type': 'Street', 'name': 'Atlantic Avenue', 'color_group': 'Yellow', 'price': 260, 'rent_levels': [22, 110, 330, 800, 975, 1150], 'mortgage': 130, 'house_cost': 150},
    {'type': 'Street', 'name': 'Ventnor Avenue', 'color_group': 'Yellow', 'price': 260, 'rent_levels': [22, 110, 330, 800, 975, 1150], 'mortgage': 130, 'house_cost': 150},
    {'type': 'Utility', 'name': 'Water Works', 'price': 150, 'mortgage': 75},
    {'type': 'Street', 'name': 'Marvin Gardens', 'color_group': 'Yellow', 'price': 280, 'rent_levels': [24, 120, 360, 850, 1025, 1200], 'mortgage': 140, 'house_cost': 150},
    {'type': 'Corner', 'name': 'Go To Jail', 'corner_type': 'GoToJail'},
    {'type': 'Street', 'name': 'Pacific Avenue', 'color_group': 'Green', 'price': 300, 'rent_levels': [26, 130, 390, 900, 1100, 1275], 'mortgage': 150, 'house_cost': 200},
    {'type': 'Street', 'name': 'North Carolina Avenue', 'color_group': 'Green', 'price': 300, 'rent_levels': [26, 130, 390, 900, 1100, 1275], 'mortgage': 150, 'house_cost': 200},
    {'type': 'Card', 'name': 'Community Chest', 'deck_type': 'Community Chest'},
    {'type': 'Street', 'name': 'Pennsylvania Avenue', 'color_group': 'Green', 'price': 320, 'rent_levels': [28, 150, 450, 1000, 1200, 1400], 'mortgage': 160, 'house_cost': 200},
    {'type': 'Railroad', 'name': 'Short Line', 'price': 200, 'mortgage': 100},
    {'type': 'Card', 'name': 'Chance', 'deck_type': 'Chance'},
    {'type': 'Street', 'name': 'Park Place', 'color_group': 'Dark Blue', 'price': 350, 'rent_levels': [35, 175, 500, 1100, 1300, 1500], 'mortgage': 175, 'house_cost': 200},
    {'type': 'Tax', 'name': 'Luxury Tax', 'tax_amount': 75},
    {'type': 'Street', 'name': 'Boardwalk', 'color_group': 'Dark Blue', 'price': 400, 'rent_levels': [50, 200, 600, 1400, 1700, 2000], 'mortgage': 200, 'house_cost': 200},
]

# Chance Card Data
CHANCE_CARD_DATA = [
    {'text': "Advance to Go (Collect $200)", 'action_type': 'MOVE_TO_SPACE', 'action_data': {'space_index': 0}},
    {'text': "Advance to Illinois Ave. - If you pass Go, collect $200", 'action_type': 'MOVE_TO_SPACE', 'action_data': {'space_index': 24}},
    {'text': "Advance to St. Charles Place – If you pass Go, collect $200", 'action_type': 'MOVE_TO_SPACE', 'action_data': {'space_index': 11}},
    {'text': "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.", 'action_type': 'MOVE_TO_NEAREST', 'action_data': {'type': 'UTILITY'}},
    {'text': "Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.", 'action_type': 'MOVE_TO_NEAREST', 'action_data': {'type': 'RAILROAD_PAY_DOUBLE'}},
    {'text': "Bank pays you dividend of $50", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 50}},
    {'text': "Get Out of Jail Free – This card may be kept until needed, or traded/sold.", 'action_type': 'ADD_GET_OUT_OF_JAIL_FREE_CARD', 'action_data': {}},
    {'text': "Go Back 3 Spaces", 'action_type': 'MOVE_BACK', 'action_data': {'steps': 3}},
    {'text': "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200", 'action_type': 'GO_TO_JAIL', 'action_data': {}},
    {'text': "Make general repairs on all your property – For each house pay $25 – For each hotel pay $100", 'action_type': 'PAY_REPAIRS', 'action_data': {'house_cost': 25, 'hotel_cost': 100}},
    {'text': "Pay poor tax of $15", 'action_type': 'PAY_BANK', 'action_data': {'amount': 15}},
    {'text': "Take a trip to Reading Railroad – If you pass Go, collect $200", 'action_type': 'MOVE_TO_SPACE', 'action_data': {'space_index': 5}},
    {'text': "Take a walk on the Boardwalk – Advance token to Boardwalk", 'action_type': 'MOVE_TO_SPACE', 'action_data': {'space_index': 39}},
    {'text': "You have been elected Chairman of the Board – Pay each player $50", 'action_type': 'PAY_EACH_PLAYER', 'action_data': {'amount': 50}},
    {'text': "Your building and loan matures – Collect $150", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 150}},
    {'text': "You have won a crossword competition - Collect $100", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 100}},
]

# Community Chest Card Data
COMMUNITY_CHEST_CARD_DATA = [
    {'text': "Advance to Go (Collect $200)", 'action_type': 'MOVE_TO_SPACE', 'action_data': {'space_index': 0}},
    {'text': "Bank error in your favor – Collect $200", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 200}},
    {'text': "Doctor's fee – Pay $50", 'action_type': 'PAY_BANK', 'action_data': {'amount': 50}},
    {'text': "From sale of stock you get $50", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 50}},
    {'text': "Get Out of Jail Free – This card may be kept until needed, or traded/sold.", 'action_type': 'ADD_GET_OUT_OF_JAIL_FREE_CARD', 'action_data': {}},
    {'text': "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200", 'action_type': 'GO_TO_JAIL', 'action_data': {}},
    {'text': "Grand Opera Night – Collect $50 from every player for opening night seats", 'action_type': 'RECEIVE_FROM_EACH_PLAYER', 'action_data': {'amount': 50}},
    {'text': "Holiday Fund matures – Receive $100", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 100}},
    {'text': "Income tax refund – Collect $20", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 20}},
    {'text': "It is your birthday - Collect $10 from each player", 'action_type': 'RECEIVE_FROM_EACH_PLAYER', 'action_data': {'amount': 10}},
    {'text': "Life insurance matures – Collect $100", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 100}},
    {'text': "Pay hospital fees of $100", 'action_type': 'PAY_BANK', 'action_data': {'amount': 100}},
    {'text': "Pay school fees of $50", 'action_type': 'PAY_BANK', 'action_data': {'amount': 50}},
    {'text': "Receive $25 consultancy fee", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 25}},
    {'text': "You are assessed for street repairs – $40 per house – $115 per hotel", 'action_type': 'PAY_REPAIRS', 'action_data': {'house_cost': 40, 'hotel_cost': 115}},
    {'text': "You have won second prize in a beauty contest – Collect $10", 'action_type': 'RECEIVE_FROM_BANK', 'action_data': {'amount': 10}},
]
```
## File: dice.py
```python
# dice.py

"""
This file defines the Dice class, which handles the logic for rolling
two six-sided dice.
"""

import random
from typing import Tuple


class Dice:
    """Manages the rolling of two six-sided dice."""
    def __init__(self):
        self.last_roll: Tuple[int, int] = (0, 0)

    def roll(self) -> Tuple[int, int]:
        """
        Rolls two dice, updates the last_roll attribute, and returns the result.
        """
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.last_roll = (die1, die2)
        return self.last_roll

    def get_total(self) -> int:
        """Returns the sum of the last dice roll."""
        return sum(self.last_roll)

    def is_doubles(self) -> bool:
        """Returns True if the last roll was doubles, False otherwise."""
        # Ensure it's not the initial state of (0, 0)
        if self.last_roll[0] == 0:
            return False
        return self.last_roll[0] == self.last_roll[1]
```
## File: board.py
```python
# board.py

"""
This file defines the Board class, which is responsible for creating and managing
the collection of all 40 Space objects that make up the game board.
"""

from typing import List
import constants
from spaces import (Space, Street, Railroad, Utility, CardSpace, TaxSpace, CornerSpace)


class Board:
    """
    Creates and manages the game board, which is a collection of 40 spaces.
    """
    def __init__(self):
        """
        Initializes the board by creating all 40 space objects based on the
        data defined in the constants.py file.
        """
        self.spaces: List[Space] = []
        self._create_board()

    def _create_board(self):
        """
        Populates the spaces list by iterating through BOARD_DATA and instantiating
        the appropriate Space subclass for each entry.
        """
        for i, space_data in enumerate(constants.BOARD_DATA):
            space_type = space_data['type']
            name = space_data['name']

            if space_type == 'Street':
                space = Street(
                    name=name,
                    index=i,
                    price=space_data['price'],
                    mortgage_value=space_data['mortgage'],
                    color_group=space_data['color_group'],
                    rent_levels=space_data['rent_levels'],
                    house_cost=space_data['house_cost']
                )
            elif space_type == 'Railroad':
                space = Railroad(
                    name=name,
                    index=i,
                    price=space_data['price'],
                    mortgage_value=space_data['mortgage']
                )
            elif space_type == 'Utility':
                space = Utility(
                    name=name,
                    index=i,
                    price=space_data['price'],
                    mortgage_value=space_data['mortgage']
                )
            elif space_type == 'Card':
                space = CardSpace(
                    name=name,
                    index=i,
                    deck_type=space_data['deck_type']
                )
            elif space_type == 'Tax':
                space = TaxSpace(
                    name=name,
                    index=i,
                    tax_amount=space_data['tax_amount']
                )
            elif space_type == 'Corner':
                space = CornerSpace(
                    name=name,
                    index=i,
                    corner_type=space_data['corner_type']
                )
            else:
                raise ValueError(f"Unknown space type '{space_type}' at index {i}")

            self.spaces.append(space)

    def get_space_at(self, index: int) -> Space:
        """
        Returns the space object at a given board index.
        
        Args:
            index: The integer index of the space (0-39).
        
        Returns:
            The Space object at the specified index.
        """
        if 0 <= index < len(self.spaces):
            return self.spaces[index]
        raise IndexError("Board index out of range.")

    def __repr__(self) -> str:
        return f"Board(spaces={len(self.spaces)})"
```
## File: token_animator.py
```python
# token_animator.py

"""
This file defines the TokenAnimator class, which is responsible for animating
a player's token sprite from a starting board position to an ending position.
It calculates the path and moves the token incrementally each frame.
"""

import math
from pplay.sprite import Sprite
from typing import List, Tuple

class TokenAnimator:
    """
    Manages the smooth movement animation of a single token sprite.
    """
    def __init__(self,
                 sprite: Sprite,
                 start_pos_idx: int,
                 end_pos_idx: int,
                 space_coords: List[Tuple[int, int]],
                 speed: float = 200.0):
        """
        Initializes the animator.

        Args:
            sprite (Sprite): The token sprite to be animated.
            start_pos_idx (int): The starting board space index.
            end_pos_idx (int): The ending board space index.
            space_coords (List[Tuple[int, int]]): A list of all space coordinates.
            speed (float): The speed of the token in pixels per second.
        """
        self.sprite = sprite
        self.space_coords = space_coords
        self.speed = speed
        self.is_finished = False

        self.path = self._calculate_path(start_pos_idx, end_pos_idx)
        self.target_node_idx = 0
        self._set_next_target()

    def _calculate_path(self, start_idx: int, end_idx: int) -> List[Tuple[int, int]]:
        """Calculates the sequence of coordinates the token must travel through."""
        path_coords = []
        current_idx = start_idx
        while current_idx != end_idx:
            current_idx = (current_idx + 1) % len(self.space_coords)
            path_coords.append(self.space_coords[current_idx])
        
        # If the list is empty, it means we are not moving
        if not path_coords:
            path_coords.append(self.space_coords[start_idx])

        return path_coords

    def _set_next_target(self):
        """Sets the next coordinate in the path as the current target."""
        if self.target_node_idx >= len(self.path):
            self.is_finished = True
            return

        self.target_x, self.target_y = self.path[self.target_node_idx]
        self.target_node_idx += 1

    def update(self, delta_time: float):
        """
        Updates the token's position. This should be called every frame.

        Args:
            delta_time (float): The time elapsed since the last frame.
        """
        if self.is_finished:
            return

        # Calculate vector towards target
        dx = self.target_x - self.sprite.x
        dy = self.target_y - self.sprite.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 1.0:
            # Reached the target node, set the next one
            self.sprite.set_position(self.target_x, self.target_y)
            self._set_next_target()
            return

        # Move sprite towards target
        move_dist = self.speed * delta_time
        if move_dist > distance:
            move_dist = distance

        self.sprite.x += (dx / distance) * move_dist
        self.sprite.y += (dy / distance) * move_dist
```
## File: ui_manager.py
```python
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
```
## File: cards.py
```python
# cards.py

"""
This file defines the Card and CardDeck classes to model the
Chance and Community Chest decks in the game.
"""

import random
from typing import List, Dict, Any


class Card:
    """Represents a single Chance or Community Chest card."""
    def __init__(self, text: str, action_type: str, action_data: Dict[str, Any]):
        self.text = text
        self.action_type = action_type
        self.action_data = action_data

    def __repr__(self) -> str:
        return f"Card(text='{self.text}')"


class CardDeck:
    """Represents a deck of cards, either Chance or Community Chest."""
    def __init__(self, card_data: List[Dict[str, Any]]):
        self.cards: List[Card] = [Card(**data) for data in card_data]
        self.discards: List[Card] = []
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck of cards randomly."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draws the top card from the deck."""
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck.")
        return self.cards.pop(0)

    def return_card_to_bottom(self, card: Card):
        """Returns a card to the bottom of the deck."""
        self.cards.append(card)
```
## File: game_manager.py
```python
# game_manager.py

"""
This file defines the GameManager, the core of the game's logic. It acts as a
state machine, managing the game flow, player turns, and enforcing the rules.
"""

from typing import List, Optional, Union, Dict, Any
import time
import math

# Import all custom game modules
import constants
from player import Player
from board import Board
from bank import Bank
from dice import Dice
from cards import CardDeck, Card
from spaces import Space, Property, Street, Railroad, Utility, TaxSpace, CardSpace, CornerSpace

# Define Game States for the State Machine
STATE_PRE_GAME = "PRE_GAME"
STATE_AWAITING_ROLL = "AWAITING_ROLL"
STATE_PLAYER_MOVING = "PLAYER_MOVING"
STATE_ACTION_PHASE = "ACTION_PHASE"
STATE_END_OF_TURN = "END_OF_TURN"
STATE_GAME_OVER = "GAME_OVER"
STATE_JAIL_TURN = "JAIL_TURN"
STATE_AWAITING_BUY_DECISION = "AWAITING_BUY_DECISION"
STATE_AUCTION = "AUCTION"
STATE_AWAITING_TAX_CHOICE = "AWAITING_TAX_CHOICE"
STATE_MANAGE_PROPERTIES = "MANAGE_PROPERTIES" # New state for building/mortgaging


class GameManager:
    """
    The brain of the game, connecting all components and managing the game state.
    """
    def __init__(self, num_players: int, ui_manager):
        if not 2 <= num_players <= 8:
            raise ValueError("Number of players must be between 2 and 8.")
        self.ui_manager = ui_manager
        self.board: Board = Board()
        self.bank: Bank = Bank()
        self.dice: Dice = Dice()
        self.chance_deck: CardDeck = CardDeck(constants.CHANCE_CARD_DATA)
        self.community_chest_deck: CardDeck = CardDeck(constants.COMMUNITY_CHEST_CARD_DATA)
        self.players: List[Player] = [Player(f"Player {i + 1}", None) for i in range(num_players)]
        self.current_player_index: int = -1
        self.current_player: Optional[Player] = None
        self.doubles_counter: int = 0
        self.game_state: str = STATE_PRE_GAME

    # --- Core Game Flow Methods (from previous steps, with minor updates) ---

    def start_game(self):
        print("Determining starting player...")
        highest_roll = -1
        starters = []
        while len(starters) != 1:
            rolls = {}
            players_to_roll = self.players if not starters else [self.players[i] for i in starters]
            for i, player in enumerate(players_to_roll):
                roll = self.dice.roll()
                total = self.dice.get_total()
                rolls[i] = total
                print(f"{player.name} rolled a {total} {roll}")
                time.sleep(0.1)
            highest_roll = max(rolls.values())
            starters = [i for i, total in rolls.items() if total == highest_roll]
            if len(starters) > 1:
                print(f"Tie for the highest roll ({highest_roll}). Tied players will re-roll.")
        self.current_player_index = starters[0]
        self.current_player = self.players[self.current_player_index]
        self.game_state = STATE_AWAITING_ROLL
        print(f"\n{self.current_player.name} wins the roll and will start the game!")

    def next_turn(self):
        self.doubles_counter = 0
        active_players = [p for p in self.players if not p.is_bankrupt]
        if len(active_players) <= 1:
            self.game_state = STATE_GAME_OVER
            print(f"\n--- GAME OVER! The winner is {active_players[0].name}! ---")
            return
        while True:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            if not self.players[self.current_player_index].is_bankrupt:
                break
        self.current_player = self.players[self.current_player_index]
        if self.current_player.in_jail:
            self.game_state = STATE_JAIL_TURN
        else:
            self.game_state = STATE_AWAITING_ROLL
        print(f"\n--- It is now {self.current_player.name}'s turn. (Money: ${self.current_player.money}) ---")

    def update(self, action: Optional[Dict[str, Any]] = None):
        """
        The main update loop for the game's state machine.
        It processes a player action or advances the state if no action is needed.
        """
        # --- 1. Process Player Actions ---
        if action:
            action_type = action.get('type')

            # State-specific actions from UI
            if self.game_state in [STATE_AWAITING_ROLL, STATE_JAIL_TURN] and action_type == 'ROLL_DICE':
                if self.game_state == STATE_AWAITING_ROLL:
                    self.handle_roll()
                else: # STATE_JAIL_TURN
                    self.handle_jail_turn()
            elif self.game_state == STATE_AWAITING_BUY_DECISION:
                space = self.board.get_space_at(self.current_player.position)
                if action_type == 'BUY_PROPERTY':
                    if self.current_player.money >= space.price:
                        self.process_buy_property(self.current_player, space)
                    else:
                        # This case should ideally be handled by disabling the button in the UI
                        print(f"Cannot buy {space.name}, not enough money. Auction will start.")
                        self.process_auction(space)
                elif action_type == 'AUCTION_PROPERTY':
                    self.process_auction(space)
            elif self.game_state == STATE_AWAITING_TAX_CHOICE and action_type == 'PAY_TAX':
                self.process_tax(self.current_player, self.board.get_space_at(self.current_player.position), action['choice'])
            elif action_type == 'MANAGE_PROPERTIES':
                self.game_state = STATE_MANAGE_PROPERTIES
            elif self.game_state == STATE_MANAGE_PROPERTIES:
                if action_type == 'BACK_TO_GAME':
                    self.game_state = STATE_AWAITING_ROLL
                elif action_type == 'BUILD':
                    self.process_building_request(self.current_player, action['property'])
                elif action_type == 'MORTGAGE':
                    self.process_mortgage_request(self.current_player, action['property'])

        # --- 2. Automatic State Progression (no player input needed) ---
        # This part of the loop runs continuously after a player action or on its own.
        if self.game_state == STATE_ACTION_PHASE:
            self.handle_landed_on_space()
        elif self.game_state == STATE_END_OF_TURN:
            if self.dice.is_doubles() and not self.current_player.in_jail:
                print(f"{self.current_player.name} rolled doubles and gets to go again!")
                self.game_state = STATE_AWAITING_ROLL
            else:
                self.next_turn()

    def handle_roll(self):
        roll = self.dice.roll()
        total = self.dice.get_total()
        print(f"{self.current_player.name} rolled a {total} {roll}")
        if self.dice.is_doubles():
            self.doubles_counter += 1
            if self.doubles_counter == 3:
                print("Caught speeding! Rolled doubles 3 times in a row.")
                self.process_go_to_jail(self.current_player)
                return
        else: self.doubles_counter = 0
        
        old_position = self.current_player.position
        steps = self.dice.get_total()
        new_position = (old_position + steps) % constants.BOARD_SIZE
        
        self.ui_manager.start_token_animation(self.current_player, old_position, new_position)
        self.game_state = STATE_PLAYER_MOVING

    def finish_player_movement(self, card_move=False, new_position=None):
        """Called by the UIManager when the token animation is complete."""
        if not card_move:
            steps = self.dice.get_total()
            old_position = self.current_player.position
            new_position = (old_position + steps) % constants.BOARD_SIZE
            
            self.current_player.position = new_position
            print(f"{self.current_player.name} moves {steps} spaces.")
            
            if new_position < old_position:
                print(f"{self.current_player.name} passed GO and collects ${constants.GO_SALARY}.")
                self.bank.pay_go_salary(self.current_player)
            self.game_state = STATE_ACTION_PHASE
        else:
            self.current_player.position = new_position

            # After a card move, check the space to determine the next state
            space = self.board.get_space_at(self.current_player.position)
            if isinstance(space, CornerSpace) and space.corner_type == 'Jail':
                self.game_state = STATE_END_OF_TURN
            else:
                self.game_state = STATE_ACTION_PHASE
        
        if not card_move:
            self.game_state = STATE_ACTION_PHASE

    def handle_landed_on_space(self):
        space = self.board.get_space_at(self.current_player.position)
        print(f"{self.current_player.name} landed on {space.name}.")
        if isinstance(space, Property): self.process_property_landing(self.current_player, space)
        elif isinstance(space, TaxSpace):
            if space.name == "Income Tax": self.game_state = STATE_AWAITING_TAX_CHOICE
            else: self.process_tax(self.current_player, space)
        elif isinstance(space, CardSpace): self.process_card_draw(self.current_player, space.deck_type)
        elif isinstance(space, CornerSpace) and space.corner_type == 'GoToJail': self.process_go_to_jail(self.current_player)
        else: self.game_state = STATE_END_OF_TURN

    def handle_jail_turn(self, player: Optional[Player] = None):
        if player is None: player = self.current_player
        print(f"{player.name} is in Jail. {player.jail_turns_remaining} turns remaining.")
        if player.get_out_of_jail_cards:
            print("Using a 'Get Out of Jail Free' card.")
            card_origin = player.use_get_out_of_jail_card()
            # Find the card object to return it to the deck
            deck = self.chance_deck if card_origin == 'Chance' else self.community_chest_deck
            card_to_return = next((c for c in deck.discards if c.action_type == 'ADD_GET_OUT_OF_JAIL_FREE_CARD'), None)
            if card_to_return:
                deck.return_card_to_bottom(card_to_return)
                deck.discards.remove(card_to_return) # Ensure it's not in discards anymore
            player.get_out_of_jail()
            self.game_state = STATE_AWAITING_ROLL
            return
        roll = self.dice.roll()
        print(f"{player.name} rolls {roll} to get out of jail.")
        if self.dice.is_doubles():
            print("Rolled doubles! You are out of jail.")
            player.get_out_of_jail()
            self.game_state = STATE_PLAYER_MOVING
        else:
            player.jail_turns_remaining -= 1
            if player.jail_turns_remaining <= 0:
                print("Failed to roll doubles for 3 turns. Must pay the fine.")
                if not self.check_for_bankruptcy(player, self.bank, constants.JAIL_FINE):
                    player.remove_money(constants.JAIL_FINE)
                    player.get_out_of_jail()
                    self.game_state = STATE_PLAYER_MOVING
            else:
                print("Failed to roll doubles. Turn ends.")
                self.game_state = STATE_END_OF_TURN

    # --- Player Action Methods (from previous steps, updated for bankruptcy) ---

    def process_rent(self, payer: Player, prop: Property):
        owner = prop.owner
        rent = 0
        if isinstance(prop, Street):
            is_monopoly = self._player_has_monopoly(owner, prop.color_group)
            rent = prop.calculate_rent()
            if is_monopoly and prop.num_houses == 0: rent *= 2
        elif isinstance(prop, Railroad):
            num_owned = sum(1 for p in owner.properties if isinstance(p, Railroad))
            num_owned = sum(1 for p in owner.properties if isinstance(p, Railroad))
            rent = 25 * (2 ** (num_owned - 1))
        elif isinstance(prop, Utility):
            num_owned = sum(1 for p in owner.properties if isinstance(p, Utility))
            multiplier = 10 if num_owned == 2 else 4
            rent = self.dice.get_total() * multiplier
        print(f"Rent is ${rent}. {payer.name} must pay {owner.name}.")
        if not self.check_for_bankruptcy(payer, owner, rent):
            payer.remove_money(rent)
            owner.add_money(rent)
            self.game_state = STATE_END_OF_TURN

    def process_tax(self, player: Player, tax_space: TaxSpace, choice: Optional[str] = None):
        tax_due = 0
        if tax_space.name == "Luxury Tax":
            tax_due = tax_space.tax_amount
            print(f"{player.name} pays Luxury Tax of ${tax_due}.")
        else: # Income Tax
            if choice == 'flat':
                tax_due = tax_space.tax_amount
                print(f"{player.name} chooses to pay the flat tax of ${tax_due}.")
            elif choice == 'percentage':
                tax_due = int(player.get_total_worth() * constants.INCOME_TAX_PERCENTAGE)
                print(f"{player.name} chooses to pay 10% of their worth, which is ${tax_due}.")
            else:
                # This should not happen if the UI is working correctly
                print("Error: Invalid tax choice. Defaulting to flat tax.")
                tax_due = tax_space.tax_amount

        if not self.check_for_bankruptcy(player, self.bank, tax_due):
            player.remove_money(tax_due)
            self.game_state = STATE_END_OF_TURN

    # --- Step 5: Advanced Mechanics Implementation ---

    def _get_color_group_properties(self, color_group: str) -> List[Street]:
        """Helper to get all properties of a specific color group."""
        return [s for s in self.board.spaces if isinstance(s, Street) and s.color_group == color_group]

    def _player_has_monopoly(self, player: Player, color_group: str) -> bool:
        """Helper to check if a player owns all properties in a color group."""
        group_props = self._get_color_group_properties(color_group)
        return all(p.owner == player for p in group_props)

    def process_building_request(self, player: Player, prop: Street, build_hotel: bool = False):
        """Handles a player's request to build a house or hotel."""
        if not self._player_has_monopoly(player, prop.color_group):
            print(f"Error: Cannot build on {prop.name}. You do not own the monopoly.")
            return
        
        group_props = self._get_color_group_properties(prop.color_group)
        if any(p.is_mortgaged for p in group_props):
            print(f"Error: Cannot build. One or more properties in the {prop.color_group} group are mortgaged.")
            return

        if build_hotel:
            if prop.num_houses != 4:
                print(f"Error: Must have 4 houses on {prop.name} before building a hotel.")
                return
            if self.bank.hotels <= 0:
                print("Error: The Bank is out of hotels.")
                return
            if player.money < prop.house_cost:
                print("Error: Not enough money to build a hotel.")
                return
            self.bank.sell_hotel(player, prop)
            print(f"Built a hotel on {prop.name}.")
        else: # Build a house
            if prop.num_houses >= 4:
                print(f"Error: {prop.name} already has 4 houses. Build a hotel instead.")
                return
            # Check for even building
            if any(prop.num_houses > p.num_houses for p in group_props):
                print(f"Error: Must build evenly. Other properties in the group have fewer houses.")
                return
            if self.bank.houses <= 0:
                print("Error: The Bank is out of houses.")
                return
            if player.money < prop.house_cost:
                print("Error: Not enough money to build a house.")
                return
            self.bank.sell_house(player, prop)
            print(f"Built a house on {prop.name}.")

    def process_selling_building_request(self, player: Player, prop: Street, sell_hotel: bool = False):
        """Handles selling buildings back to the bank."""
        group_props = self._get_color_group_properties(prop.color_group)
        if sell_hotel:
            if prop.num_houses != 5:
                print(f"Error: There is no hotel on {prop.name} to sell.")
                return
            self.bank.buy_back_hotel(player, prop)
            print(f"Sold the hotel on {prop.name} for ${prop.house_cost // 2}.")
        else: # Sell a house
            if prop.num_houses == 0:
                print(f"Error: There are no houses on {prop.name} to sell.")
                return
            # Check for even selling
            if any(prop.num_houses < p.num_houses for p in group_props):
                print(f"Error: Must sell evenly. Other properties in the group have more houses.")
                return
            self.bank.buy_back_house(player, prop)
            print(f"Sold a house on {prop.name} for ${prop.house_cost // 2}.")

    def process_mortgage_request(self, player: Player, prop: Property):
        """Mortgages a property."""
        if prop.is_mortgaged:
            print(f"Error: {prop.name} is already mortgaged.")
            return
        if isinstance(prop, Street):
            group_props = self._get_color_group_properties(prop.color_group)
            if any(p.num_houses > 0 for p in group_props):
                print(f"Error: Cannot mortgage. All properties in the {prop.color_group} group must be unimproved.")
                return
        
        player.add_money(prop.mortgage_value)
        prop.is_mortgaged = True
        print(f"{player.name} mortgaged {prop.name} and received ${prop.mortgage_value}.")

    def process_unmortgage_request(self, player: Player, prop: Property):
        """Lifts a mortgage on a property."""
        if not prop.is_mortgaged:
            print(f"Error: {prop.name} is not mortgaged.")
            return
        
        cost = math.ceil(prop.mortgage_value * (1 + constants.MORTGAGE_INTEREST_RATE))
        if player.money < cost:
            print(f"Error: Not enough money to unmortgage. Cost: ${cost}.")
            return
        
        player.remove_money(cost)
        prop.is_mortgaged = False
        print(f"{player.name} paid ${cost} to unmortgage {prop.name}.")

    def process_trade_request(self, player1: Player, player2: Player, offer: Dict[str, Any]):
        """
        Processes a trade between two players based on an offer dictionary.
        Example offer: {'from_p1': {'money': 50, 'properties': [prop1]}, 'from_p2': {'properties': [prop2]}}
        """
        p1_offer = offer.get('from_p1', {})
        p2_offer = offer.get('from_p2', {})

        # Validate that traded properties are unimproved
        for prop in p1_offer.get('properties', []) + p2_offer.get('properties', []):
            if isinstance(prop, Street) and any(p.num_houses > 0 for p in self._get_color_group_properties(prop.color_group)):
                print(f"Error: Trade failed. {prop.name}'s color group has buildings on it.")
                return

        # Validate funds
        if player1.money < p1_offer.get('money', 0) or player2.money < p2_offer.get('money', 0):
            print("Error: Trade failed. A player does not have enough money for the offer.")
            return

        # Execute trade
        # Money transfer
        player1.remove_money(p1_offer.get('money', 0))
        player2.add_money(p1_offer.get('money', 0))
        player2.remove_money(p2_offer.get('money', 0))
        player1.add_money(p2_offer.get('money', 0))

        # Property transfer
        for prop in p1_offer.get('properties', []):
            player1.properties.remove(prop)
            player2.properties.append(prop)
            prop.owner = player2
        for prop in p2_offer.get('properties', []):
            player2.properties.remove(prop)
            player1.properties.append(prop)
            prop.owner = player1
        
        print(f"Trade between {player1.name} and {player2.name} was successful.")

    def check_for_bankruptcy(self, debtor: Player, creditor: Union[Player, Bank], amount_owed: int) -> bool:
        """
        Checks if a player can pay a debt. If not, handles the bankruptcy process.
        Returns True if the player went bankrupt, False otherwise.
        """
        if debtor.money >= amount_owed:
            return False # Can pay, not bankrupt

        print(f"{debtor.name} cannot pay ${amount_owed} with cash on hand. Attempting to raise funds...")
        
        # Attempt to raise funds by selling buildings and mortgaging properties
        # Sell buildings (hotels first, then houses, from most expensive groups to cheapest)
        sellable_streets = sorted([p for p in debtor.properties if isinstance(p, Street) and p.num_houses > 0], key=lambda x: x.house_cost, reverse=True)
        for street in sellable_streets:
            while street.num_houses > 0:
                if street.num_houses == 5: # Hotel
                    self.process_selling_building_request(debtor, street, sell_hotel=True)
                else: # House
                    self.process_selling_building_request(debtor, street, sell_hotel=False)
                if debtor.money >= amount_owed:
                    print("Funds raised successfully.")
                    return False

        # Mortgage properties (most valuable first)
        mortgageable_props = sorted([p for p in debtor.properties if not p.is_mortgaged], key=lambda x: x.mortgage_value, reverse=True)
        for prop in mortgageable_props:
            self.process_mortgage_request(debtor, prop)
            if debtor.money >= amount_owed:
                print("Funds raised successfully.")
                return False

        # If still not enough money, player is bankrupt
        print(f"{debtor.name} is bankrupt!")
        debtor.is_bankrupt = True
        creditor_name = "the Bank" if isinstance(creditor, Bank) else creditor.name

        if isinstance(creditor, Player):
            # Transfer all assets to the creditor player
            creditor.add_money(debtor.money)
            debtor.money = 0
            for prop in list(debtor.properties): # Use list copy for safe removal
                debtor.properties.remove(prop)
                creditor.properties.append(prop)
                prop.owner = creditor
                # New owner must immediately handle mortgaged properties
                if prop.is_mortgaged:
                    interest = math.ceil(prop.mortgage_value * constants.MORTGAGE_INTEREST_RATE)
                    print(f"{creditor.name} received mortgaged property {prop.name}. Must pay 10% interest (${interest}).")
                    # Forcing payment, could be a choice in UI
                    creditor.remove_money(interest)
            creditor.get_out_of_jail_cards.extend(debtor.get_out_of_jail_cards)
            debtor.get_out_of_jail_cards.clear()
        else: # Creditor is the Bank
            # Return Get Out of Jail Free cards to decks
            for card_origin in debtor.get_out_of_jail_cards:
                deck = self.chance_deck if card_origin == 'Chance' else self.community_chest_deck
                card_to_return = next((c for c in deck.discards if c.action_type == 'ADD_GET_OUT_OF_JAIL_FREE_CARD'), None)
                if card_to_return:
                    deck.return_card_to_bottom(card_to_return)
                    deck.discards.remove(card_to_return) # Remove from discards so it can't be returned again
            debtor.get_out_of_jail_cards.clear()

            # Turn over all assets to the Bank
            for prop in list(debtor.properties):
                prop.owner = None
                prop.is_mortgaged = False
                if isinstance(prop, Street): prop.num_houses = 0
                # The Bank will auction these properties
                print(f"{prop.name} is returned to the Bank and will be auctioned.")
                self.process_auction(prop) # Simplified auction

        print(f"{debtor.name} has been eliminated from the game. Their assets go to {creditor_name}.")
        self.game_state = STATE_END_OF_TURN
        return True

    # --- Methods from previous steps that need to be here for completeness ---
    # (These are simplified and might not be called in the non-interactive flow)
    def process_property_landing(self, player: Player, prop: Property):
        if prop.owner is None: self.game_state = STATE_AWAITING_BUY_DECISION
        elif prop.owner == player: self.game_state = STATE_END_OF_TURN
        elif prop.is_mortgaged:
            print(f"{prop.name} is owned by {prop.owner.name} but is mortgaged. No rent is due.")
            self.game_state = STATE_END_OF_TURN
        else: self.process_rent(player, prop)
    def process_buy_property(self, player: Player, prop: Property):
        print(f"{player.name} buys {prop.name} for ${prop.price}.")
        player.remove_money(prop.price)
        prop.owner = player
        player.properties.append(prop)
        self.game_state = STATE_END_OF_TURN
    def process_auction(self, prop: Property):
        print(f"Auctioning {prop.name}.")
        bidders = [p for p in self.players if not p.is_bankrupt and p.money >= prop.price]
        if not bidders:
            print("No one can afford the property. It remains unowned.")
            self.game_state = STATE_END_OF_TURN
            return
        winner = max(bidders, key=lambda p: p.money)
        price = prop.price
        print(f"{winner.name} wins the auction for ${price}.")
        winner.remove_money(price)
        prop.owner = winner
        winner.properties.append(prop)
        self.game_state = STATE_END_OF_TURN
    def process_card_draw(self, player: Player, deck_type: str):
        deck = self.chance_deck if deck_type == 'Chance' else self.community_chest_deck
        card = deck.draw_card()
        print(f"{player.name} drew a {deck_type} card: \"{card.text}\"")
        action_type, data = card.action_type, card.action_data
        if action_type == 'MOVE_TO_SPACE':
            old_position = player.position
            new_position = data['space_index']
            if old_position > new_position:
                self.bank.pay_go_salary(player)
            
            self.ui_manager.start_token_animation(player, old_position, new_position, card_move=True)
            self.game_state = STATE_PLAYER_MOVING

        elif action_type == 'GO_TO_JAIL':
            self.process_go_to_jail(player)
        elif action_type == 'RECEIVE_FROM_BANK':
            player.add_money(data['amount'])
            self.game_state = STATE_END_OF_TURN
        elif action_type == 'PAY_BANK':
            if not self.check_for_bankruptcy(player, self.bank, data['amount']):
                player.remove_money(data['amount'])
                self.game_state = STATE_END_OF_TURN
        elif action_type == 'ADD_GET_OUT_OF_JAIL_FREE_CARD':
            player.add_get_out_of_jail_card(deck_type)
            deck.discards.append(card) # Keep track of it to return later
            self.game_state = STATE_END_OF_TURN
            return # Don't return this card to the bottom yet
        else:
            print(f"Card action '{action_type}' not fully implemented yet.")
            self.game_state = STATE_END_OF_TURN
        deck.return_card_to_bottom(card)
    def process_go_to_jail(self, player: Player):
        print(f"{player.name} is going to Jail!")
        old_position = player.position
        player.go_to_jail()
        new_position = player.position
        
        self.ui_manager.start_token_animation(player, old_position, new_position, card_move=True)
        self.game_state = STATE_PLAYER_MOVING
```
## File: main.py
```python
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
```
## File: spaces.py
```python
# spaces.py

"""
This file models the 40 spaces on the game board using an inheritance structure.
Each class represents a different type of space with its specific attributes and behaviors.
"""

from typing import List, Optional

# Forward declaration for type hinting to avoid circular imports
if False:
    from player import Player


class Space:
    """Base class for all spaces on the board."""
    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', index={self.index})"


class Property(Space):
    """Base class for all ownable properties (Streets, Railroads, Utilities)."""
    def __init__(self, name: str, index: int, price: int, mortgage_value: int):
        super().__init__(name, index)
        self.price = price
        self.mortgage_value = mortgage_value
        self.owner: Optional['Player'] = None
        self.is_mortgaged: bool = False

    def calculate_rent(self, dice_roll: Optional[int] = None) -> int:
        """
        Calculates the rent for this property.
        This method is intended to be overridden by subclasses.
        The full rent logic (e.g., monopolies) is handled by the GameManager.
        """
        raise NotImplementedError("Subclasses must implement calculate_rent")


class Street(Property):
    """Represents a standard street property that can be developed with houses and hotels."""
    def __init__(self, name: str, index: int, price: int, mortgage_value: int,
                 color_group: str, rent_levels: List[int], house_cost: int):
        super().__init__(name, index, price, mortgage_value)
        self.color_group = color_group
        self.rent_levels = rent_levels  # [rent, 1 house, 2 houses, 3 houses, 4 houses, hotel]
        self.house_cost = house_cost
        self.num_houses: int = 0  # 0-4 for houses, 5 for a hotel

    def calculate_rent(self, dice_roll: Optional[int] = None) -> int:
        """Calculates rent based on the number of houses. Monopoly double rent is handled by GameManager."""
        return self.rent_levels[self.num_houses]


class Railroad(Property):
    """Represents a railroad property."""
    def __init__(self, name: str, index: int, price: int, mortgage_value: int):
        super().__init__(name, index, price, mortgage_value)
        self.base_rent = 25

    def calculate_rent(self, dice_roll: Optional[int] = None) -> int:
        """
        Returns the base rent. The GameManager is responsible for calculating the
        actual rent based on the number of railroads the owner possesses.
        """
        return self.base_rent


class Utility(Property):
    """Represents a utility property (Electric Company, Water Works)."""
    def __init__(self, name: str, index: int, price: int, mortgage_value: int):
        super().__init__(name, index, price, mortgage_value)

    def calculate_rent(self, dice_roll: Optional[int] = None) -> int:
        """
        Calculates rent based on the dice roll. The GameManager determines the
        correct multiplier (4x or 10x).
        """
        if dice_roll is None:
            raise ValueError("Dice roll must be provided for Utility rent calculation.")
        # Base case multiplier is 4x. GameManager will adjust if owner has both utilities.
        return dice_roll * 4


class CardSpace(Space):
    """Represents a Chance or Community Chest space."""
    def __init__(self, name: str, index: int, deck_type: str):
        super().__init__(name, index)
        if deck_type not in ['Chance', 'Community Chest']:
            raise ValueError("deck_type must be 'Chance' or 'Community Chest'")
        self.deck_type = deck_type


class TaxSpace(Space):
    """Represents a tax space (Income Tax, Luxury Tax)."""
    def __init__(self, name: str, index: int, tax_amount: int):
        super().__init__(name, index)
        self.tax_amount = tax_amount


class CornerSpace(Space):
    """Represents one of the four corner spaces."""
    def __init__(self, name: str, index: int, corner_type: str):
        super().__init__(name, index)
        if corner_type not in ['GO', 'Jail', 'FreeParking', 'GoToJail']:
            raise ValueError("Invalid corner_type specified.")
        self.corner_type = corner_type
```
## File: player.py
```python
# player.py

"""
This file defines the Player class, which represents a player in the game,
tracking their assets, position, and status.
"""

from typing import List
from pplay.sprite import Sprite
import constants
from spaces import Property, Street


class Player:
    """Represents a player in the Monopoly game."""
    def __init__(self, name: str, token_sprite: Sprite):
        self.name: str = name
        self.token_sprite: Sprite = token_sprite
        self.money: int = constants.STARTING_MONEY
        self.properties: List[Property] = []
        self.position: int = 0
        self.in_jail: bool = False
        self.jail_turns_remaining: int = 0
        self.get_out_of_jail_cards: List[str] = []  # Stores 'Chance' or 'Community Chest'
        self.is_bankrupt: bool = False

    def add_get_out_of_jail_card(self, deck_type: str):
        """Adds a 'Get Out of Jail Free' card from a specific deck."""
        self.get_out_of_jail_cards.append(deck_type)

    def use_get_out_of_jail_card(self) -> str:
        """Uses a 'Get Out of Jail Free' card and returns its deck of origin."""
        if not self.get_out_of_jail_cards:
            return None
        return self.get_out_of_jail_cards.pop(0)

    def add_money(self, amount: int):
        """Adds a specified amount of money to the player's total."""
        if amount > 0:
            self.money += amount

    def remove_money(self, amount: int):
        """Removes a specified amount of money from the player's total."""
        if amount > 0:
            self.money -= amount

    def get_total_worth(self) -> int:
        """
        Calculates the player's total worth according to the rules for the 10% Income Tax option.
        Worth = cash + printed prices of unmortgaged properties + mortgage value of mortgaged properties + purchase price of all buildings.
        """
        worth = self.money

        for prop in self.properties:
            if prop.is_mortgaged:
                worth += prop.mortgage_value
            else:
                worth += prop.price
                if isinstance(prop, Street):
                    # 5 houses represents a hotel
                    num_buildings = prop.num_houses if prop.num_houses < 5 else 5
                    worth += num_buildings * prop.house_cost
        return worth

    def move(self, steps: int):
        """Updates the player's position on the board. Does not handle passing GO or board wrapping."""
        self.position += steps

    def go_to_jail(self):
        """Sets the player's status to 'in jail'."""
        self.position = constants.JAIL_POSITION
        self.in_jail = True
        self.jail_turns_remaining = 3

    def get_out_of_jail(self):
        """Removes the player's 'in jail' status."""
        self.in_jail = False
        self.jail_turns_remaining = 0

    def __repr__(self) -> str:
        return f"Player(name='{self.name}', money=${self.money}, position={self.position})"
```
## File: bank.py
```python
# bank.py

"""
This file defines the Bank class, which manages the central assets of the game,
including the supply of houses and hotels, and handles direct monetary
transactions with players.
"""

import constants
from player import Player
from spaces import Street

class Bank:
    """
    Manages the Bank's assets and transactions in the Monopoly game.
    The Bank never goes bankrupt.
    """
    def __init__(self):
        """Initializes the Bank with the starting number of houses and hotels."""
        self.houses: int = constants.TOTAL_HOUSES
        self.hotels: int = constants.TOTAL_HOTELS

    def sell_house(self, player: Player, property_obj: Street) -> bool:
        """
        Sells a house to a player for a given property, if available.
        Assumes validation (e.g., even building) is done by the GameManager.
        """
        if self.houses > 0:
            player.remove_money(property_obj.house_cost)
            property_obj.num_houses += 1
            self.houses -= 1
            return True
        return False

    def sell_hotel(self, player: Player, property_obj: Street) -> bool:
        """
        Sells a hotel to a player for a given property, if available.
        This action returns 4 houses to the bank's supply.
        Assumes validation is done by the GameManager.
        """
        if self.hotels > 0 and property_obj.num_houses == 4:
            player.remove_money(property_obj.house_cost)
            property_obj.num_houses += 1  # 5 houses represents a hotel
            self.hotels -= 1
            self.houses += 4  # 4 houses are returned to the bank
            return True
        return False

    def buy_back_house(self, player: Player, property_obj: Street):
        """
        Buys a house back from a player at half price.
        Assumes validation (e.g., even selling) is done by the GameManager.
        """
        player.add_money(property_obj.house_cost // 2)
        property_obj.num_houses -= 1
        self.houses += 1

    def buy_back_hotel(self, player: Player, property_obj: Street):
        """
        Buys a hotel back from a player at half price.
        A hotel is converted back into 4 houses on the property, and the
        physical hotel piece is returned to the bank.
        """
        player.add_money(property_obj.house_cost // 2)
        property_obj.num_houses = 4  # Hotel becomes 4 houses
        self.hotels += 1
        self.houses -= 4  # 4 houses are taken from the bank's supply

    def pay_go_salary(self, player: Player):
        """Pays the standard $200 salary to a player for passing GO."""
        player.add_money(constants.GO_SALARY)

    def collect_from_player(self, player: Player, amount: int):
        """Collects a specified amount of money from a player."""
        player.remove_money(amount)

    def pay_player(self, player: Player, amount: int):
        """Pays a specified amount of money to a player."""
        player.add_money(amount)

    def __repr__(self) -> str:
        return f"Bank(houses={self.houses}, hotels={self.hotels})"
```
