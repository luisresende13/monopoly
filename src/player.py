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
