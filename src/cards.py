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
