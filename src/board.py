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