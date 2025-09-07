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
STATE_SHOWING_CARD = "SHOWING_CARD"
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
        """
        Determines the starting player by having players roll the dice.
        Handles ties by making only the tied players re-roll until a single
        winner is determined.
        """
        print("Determining starting player...")
        
        # The indices of players who need to roll. Starts with everyone.
        players_to_roll_indices = list(range(len(self.players)))

        while True:
            rolls = {}
            for player_index in players_to_roll_indices:
                player = self.players[player_index]
                self.dice.roll()
                total = self.dice.get_total()
                rolls[player_index] = total
                print(f"{player.name} rolled a {total} {self.dice.last_roll}")
                time.sleep(0.1)

            if not rolls:
                print("Error: No players left to roll. Cannot determine starter.")
                # Fallback: start with player 0 if something goes wrong
                self.current_player_index = 0
                break

            highest_roll = max(rolls.values())
            starters = [index for index, total in rolls.items() if total == highest_roll]

            if len(starters) == 1:
                # We have a single winner
                self.current_player_index = starters[0]
                break
            
            # If we are here, there was a tie. Only tied players roll next.
            players_to_roll_indices = starters
            print(f"Tie for the highest roll ({highest_roll}). Tied players will re-roll.")
        
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
            elif self.game_state == STATE_JAIL_TURN and action_type == 'PAY_FINE':
                self.process_pay_jail_fine()
            elif self.game_state == STATE_JAIL_TURN and action_type == 'MANAGE_PROPERTIES':
                self.game_state = STATE_MANAGE_PROPERTIES
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
            elif self.game_state == STATE_SHOWING_CARD and action_type == 'DISMISS_CARD':
                self.handle_card_action(action['card'])
            elif self.game_state == STATE_MANAGE_PROPERTIES:
                if action_type == 'BACK_TO_GAME':
                    # If returning from management, go back to the correct state
                    if self.current_player.in_jail:
                        self.game_state = STATE_JAIL_TURN
                    else:
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
            
            # Start the movement animation
            old_position = player.position
            steps = self.dice.get_total()
            new_position = (old_position + steps) % constants.BOARD_SIZE
            self.ui_manager.start_token_animation(player, old_position, new_position)
            
            self.game_state = STATE_PLAYER_MOVING
        else:
            player.jail_turns_remaining -= 1
            if player.jail_turns_remaining <= 0:
                print("Failed to roll doubles for 3 turns. Must pay the fine.")
                if not self.check_for_bankruptcy(player, self.bank, constants.JAIL_FINE):
                    player.remove_money(constants.JAIL_FINE)
                    player.get_out_of_jail()

                    # The player now moves the amount of their last roll
                    old_position = player.position
                    steps = self.dice.get_total()
                    new_position = (old_position + steps) % constants.BOARD_SIZE
                    self.ui_manager.start_token_animation(player, old_position, new_position)

                    self.game_state = STATE_PLAYER_MOVING
            else:
                print("Failed to roll doubles. Turn ends.")
                self.game_state = STATE_END_OF_TURN

    def process_pay_jail_fine(self):
        """Handles the player's choice to pay the jail fine to get out early."""
        player = self.current_player
        # The UI should prevent this if the player can't afford it, but we double-check.
        if player.money >= constants.JAIL_FINE:
            print(f"{player.name} pays ${constants.JAIL_FINE} to get out of jail.")
            # check_for_bankruptcy will return False if they can pay.
            if not self.check_for_bankruptcy(player, self.bank, constants.JAIL_FINE):
                player.remove_money(constants.JAIL_FINE)
                player.get_out_of_jail()
                self.game_state = STATE_AWAITING_ROLL # Player is out and can now roll
        else:
            # This case should be prevented by the UI, but is here as a safeguard.
            print(f"Error: {player.name} cannot afford the ${constants.JAIL_FINE} fine.")

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
        
        # Transition to showing the card and let the UI handle it
        self.ui_manager.display_card(card)
        self.game_state = STATE_SHOWING_CARD

    def handle_card_action(self, card: Card):
        """Processes the action of a card after it has been displayed and dismissed."""
        player = self.current_player
        deck_type = 'Chance' if card in self.chance_deck.cards or card in self.chance_deck.discards else 'Community Chest'
        deck = self.chance_deck if deck_type == 'Chance' else self.community_chest_deck

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
