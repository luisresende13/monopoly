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