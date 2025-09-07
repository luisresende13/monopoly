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