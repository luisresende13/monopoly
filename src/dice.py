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