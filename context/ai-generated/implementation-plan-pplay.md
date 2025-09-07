This is a detailed, multi-step implementation plan to develop the Monopoly game using the PPLay module, designed to be followed by an AI developer.

---

### **Monopoly Game Implementation Plan**

#### **Project Overview**

This plan outlines the complete development of a classic Monopoly game using the PPLay Python module. The architecture will be based on Object-Oriented Programming (OOP) principles to create a modular, maintainable, and extensible codebase. The game will adhere strictly to the rules and data provided in the "Complete and Consolidated Rules of Monopoly" and "Monopoly Game Data and Asset Specifications" documents.

The implementation is divided into seven logical steps, starting with the foundational data structures and progressively building up to the game logic, user interface, and final integration.

#### **File Structure**

The project will be organized into the following file structure:

```
monopoly/
├── main.py                 # Main game loop and initialization
├── constants.py            # All static game data (from the additional info doc)
├── game_manager.py         # Core game logic, state machine, and turn management
├── ui_manager.py           # Handles all rendering, UI elements, and user input via PPLay
├── player.py               # Player class definition
├── board.py                # Board class that holds all the spaces
├── spaces.py               # Definitions for all types of board spaces (Property, Tax, etc.)
├── cards.py                # Definitions for Chance/Community Chest cards and decks
├── dice.py                 # Dice rolling logic
├── bank.py                 # Bank logic for managing assets
└── assets/                 # Directory for all game images (board, tokens, cards, etc.)
    ├── board.png
    ├── tokens/
    │   ├── car.png
    │   └── ...
    ├── cards/
    │   ├── chance_back.png
    │   └── ...
    └── ui/
        ├── button.png
        └── ...
```

---

### **Step 1: Core Data Structures and Foundation**

**Objective:** Define the fundamental classes that represent the game's entities. These classes will primarily hold data and have simple methods. No complex game logic will be implemented in this step.

1.  **`constants.py`**
    *   **Purpose:** To centralize all static data from the "Additional Information" document. This avoids "magic numbers" and makes the code easier to maintain.
    *   **Implementation:**
        *   Create constants for game parameters: `STARTING_MONEY`, `GO_SALARY`, `JAIL_FINE`, `TOTAL_HOUSES`, `TOTAL_HOTELS`, etc.
        *   Create a list of dictionaries or tuples named `BOARD_DATA` to represent all 40 spaces, containing all information from the board layout table (name, type, price, rents, etc.).
        *   Create two lists of dictionaries, `CHANCE_CARD_DATA` and `COMMUNITY_CHEST_CARD_DATA`, containing the text and action details for each card.

2.  **`spaces.py`**
    *   **Purpose:** To model the 40 spaces on the game board using inheritance.
    *   **Classes to Implement:**
        *   **`Space` (Base Class):**
            *   **Attributes:** `name`, `index`.
        *   **`Property(Space)`:**
            *   **Attributes:** `price`, `mortgage_value`, `owner` (will hold a `Player` object, initially `None`), `is_mortgaged` (boolean).
            *   **Methods:** `calculate_rent(dice_roll=None)` (to be overridden by subclasses).
        *   **`Street(Property)`:**
            *   **Attributes:** `color_group`, `rent_levels` (list of rents for 0-4 houses, 1 hotel), `house_cost`, `num_houses` (integer, 0-4 for houses, 5 for a hotel).
            *   **Methods:** `calculate_rent()`: Implements rent calculation based on `num_houses` and monopoly status.
        *   **`Railroad(Property)`:**
            *   **Methods:** `calculate_rent()`: Implements rent calculation based on how many railroads the owner possesses.
        *   **`Utility(Property)`:**
            *   **Methods:** `calculate_rent(dice_roll)`: Implements rent calculation based on the dice roll and whether the owner has one or both utilities.
        *   **`CardSpace(Space)`:**
            *   **Attributes:** `deck_type` (string: 'Chance' or 'Community Chest').
        *   **`TaxSpace(Space)`:**
            *   **Attributes:** `tax_amount`.
        *   **`CornerSpace(Space)`:**
            *   **Attributes:** `corner_type` (string: 'GO', 'Jail', 'FreeParking', 'GoToJail').

3.  **`player.py`**
    *   **Purpose:** To represent a player in the game.
    *   **Class to Implement:**
        *   **`Player`:**
            *   **Attributes:** `name`, `token_sprite` (a `PPlay.Sprite` object), `money`, `properties` (list of `Property` objects), `position` (integer board index), `in_jail` (boolean), `jail_turns_remaining` (integer), `get_out_of_jail_cards` (integer), `is_bankrupt` (boolean).
            *   **Methods:** `add_money(amount)`, `remove_money(amount)`, `get_total_worth()`, `move(steps)`, `go_to_jail()`, `get_out_of_jail()`.

4.  **`cards.py`**
    *   **Purpose:** To model the Chance and Community Chest cards and their decks.
    *   **Classes to Implement:**
        *   **`Card`:**
            *   **Attributes:** `text`, `action_type` (e.g., `MOVE_TO_SPACE`), `action_data` (e.g., `{'space_index': 24}`).
        *   **`CardDeck`:**
            *   **Attributes:** `cards` (a list of `Card` objects).
            *   **Methods:** `shuffle()`, `draw_card()`, `return_card_to_bottom(card)`.

5.  **`dice.py`**
    *   **Purpose:** To manage dice rolls.
    *   **Class to Implement:**
        *   **`Dice`:**
            *   **Attributes:** `last_roll` (tuple: `(die1, die2)`).
            *   **Methods:** `roll()`, `get_total()`, `is_doubles()`.

---

### **Step 2: Game World Initialization**

**Objective:** Create the classes responsible for setting up and holding the state of the game world.

1.  **`board.py`**
    *   **Purpose:** To create and manage the collection of 40 `Space` objects.
    *   **Class to Implement:**
        *   **`Board`:**
            *   **Attributes:** `spaces` (a list of 40 `Space` subclass instances).
            *   **Methods:** `__init__()`: This constructor will read `constants.BOARD_DATA` and instantiate the correct `Space` subclass for each of the 40 positions, populating the `spaces` list. `get_space_at(index)`: Returns the space object at a given index.

2.  **`bank.py`**
    *   **Purpose:** To manage the central assets of the game. This can be implemented as a class that is instantiated once.
    *   **Class to Implement:**
        *   **`Bank`:**
            *   **Attributes:** `houses` (integer, starts at 32), `hotels` (integer, starts at 12).
            *   **Methods:** `sell_house(player, property)`, `sell_hotel(player, property)`, `buy_back_house(property)`, `buy_back_hotel(property)`, `pay_go_salary(player)`, `collect_from_player(player, amount)`, `pay_player(player, amount)`.

---

### **Step 3: Core Game Logic and State Management**

**Objective:** Implement the central `GameManager` which will control the flow of the game, manage turns, and enforce the rules.

1.  **`game_manager.py`**
    *   **Purpose:** To act as the brain of the game, connecting all other components.
    *   **Class to Implement:**
        *   **`GameManager`:**
            *   **Attributes:**
                *   `players` (list of `Player` objects).
                *   `board` (a `Board` object).
                *   `bank` (a `Bank` object).
                *   `dice` (a `Dice` object).
                *   `chance_deck`, `community_chest_deck` (`CardDeck` objects).
                *   `current_player_index` (integer).
                *   `current_player` (a `Player` object).
                *   `doubles_counter` (integer).
                *   `game_state` (an enum or string to manage the game flow, e.g., `AWAITING_ROLL`, `PLAYER_MOVING`, `ACTION_PHASE`, `END_OF_TURN`).
            *   **Methods:**
                *   `__init__(num_players)`: Initializes all game components. Creates players, the board, bank, and decks. Shuffles decks.
                *   `start_game()`: Determines the starting player and sets the initial game state.
                *   `next_turn()`: Advances to the next player, resets turn-specific variables (like `doubles_counter`), and sets the game state to `AWAITING_ROLL`.
                *   `update()`: The main logic loop called from `main.py`. It will contain a state machine based on `game_state` to call the appropriate handler methods.
                *   `handle_roll()`: Rolls the dice, checks for doubles, handles the "3 doubles go to jail" rule, and initiates player movement.
                *   `handle_player_movement()`: Updates the player's position on the board, checking for passing GO.
                *   `handle_landed_on_space()`: The core action dispatcher. It inspects the space the player landed on and triggers the correct logic (rent, buy, draw card, tax, etc.). This will be a large method with conditional logic for each space type.

---

### **Step 4: Implementing Player Actions and Interactions**

**Objective:** Flesh out the methods within `GameManager` and other classes to handle the primary player actions that occur after landing on a space.

1.  **`game_manager.py` (continued)**
    *   **Methods to Implement:**
        *   `process_property_landing(player, property)`: Checks if the property is owned. If unowned, sets state to `AWAITING_BUY_DECISION`. If owned by another, calls `process_rent()`.
        *   `process_rent(payer, property)`: Calculates rent using the property's `calculate_rent` method and facilitates the transaction. Checks for bankruptcy if the player cannot pay.
        *   `process_buy_property(player, property)`: Handles the transaction for a player buying a property from the bank.
        *   `process_auction(property)`: Sets the game state to `AUCTION` and manages the auction logic (this will require UI interaction planned in Step 6).
        *   `process_card_draw(player, deck_type)`: Draws a card, shows it to the player (via UI), and executes its action. This will involve a large dispatcher to handle all 16 card action types.
        *   `process_tax(player, tax_space)`: Handles tax payment, including the 10% or $200 choice for Income Tax.
        *   `process_go_to_jail(player)`: Moves the player to jail and ends their turn.
        *   `handle_jail_turn(player)`: Manages the options for a player in jail (pay fine, use card, roll for doubles).

---

### **Step 5: Advanced Game Mechanics**

**Objective:** Implement the more complex systems of property management, trading, and bankruptcy.

1.  **`game_manager.py` (continued)**
    *   **Methods to Implement:**
        *   `process_building_request(player, property, build_house)`: Handles a player's request to build a house or hotel. Must validate all rules: monopoly ownership, no mortgages in the group, building evenly, and bank supply.
        *   `process_selling_building_request(player, property, sell_house)`: Handles selling buildings back to the bank, enforcing the "sell evenly" rule.
        *   `process_mortgage_request(player, property)`: Mortgages a property. Validates that there are no buildings on any property in its color group.
        *   `process_unmortgage_request(player, property)`: Lifts a mortgage, including the 10% interest payment.
        *   `process_trade_request(player1, player2, offer)`: Manages the logic for player-to-player trades. This will be heavily reliant on the UI.
        *   `check_for_bankruptcy(debtor, creditor, amount_owed)`: The central bankruptcy handler. If a player is bankrupt, this method will manage the transfer of all assets to the creditor (another player or the bank) according to the rules, including handling mortgaged properties. It will then remove the bankrupt player from the game.

---

### **Step 6: User Interface (UI) Implementation with PPLay**

**Objective:** Create a visual and interactive layer for the game using the PPLay module. This component will read the state from the `GameManager` and render it, while also capturing user input and passing it back to the manager.

1.  **`ui_manager.py`**
    *   **Purpose:** To handle all drawing and input. It should be stateless regarding game logic.
    *   **Class to Implement:**
        *   **`UIManager`:**
            *   **Attributes:** `window` (`PPlay.Window`), `mouse` (`PPlay.Mouse`), `keyboard` (`PPlay.Keyboard`), `board_sprite` (`PPlay.Sprite`), `token_sprites` (dictionary mapping players to their sprites), `ui_elements` (e.g., buttons, dialog boxes).
            *   **Methods:**
                *   `__init__(window)`: Initializes UI components and loads assets.
                *   `draw_game_state(game_manager)`: The main drawing function. It calls all other specific draw methods.
                *   `draw_board()`: Draws the main game board.
                *   `draw_player_tokens(players)`: Draws each player's token at their correct position on the board.
                *   `draw_player_hud(players, current_player)`: Displays information for each player (money, properties). Highlights the current player.
                *   `draw_dice(dice_roll)`: Displays the result of a dice roll.
                *   `display_decision_dialog(title, message, options)`: A generic function to create interactive dialogs (e.g., "Buy for $60 or Auction?", with "Buy" and "Auction" buttons). Returns the user's choice. This will use `PPlay.GameImage` for the dialog box and `PPlay.Sprite` for buttons.
                *   `display_card(card)`: Shows the text of a drawn Chance or Community Chest card.
                *   `get_player_input(game_manager)`: Checks for mouse clicks on UI elements (like the "Roll Dice" button) and keyboard input. Based on the current `game_state`, it determines what input is valid and returns an action to the `GameManager`.

---

### **Step 7: Final Integration and Main Loop**

**Objective:** Tie all the components together in the main entry point of the application.

1.  **`main.py`**
    *   **Purpose:** To initialize the game and run the main game loop.
    *   **Implementation:**
        *   Import necessary PPLay modules and all custom game classes.
        *   Set up the PPLay window (`width`, `height`, `title`).
        *   **Game Setup Phase:**
            *   Display a main menu to select the number of players.
        *   **Initialization:**
            *   Instantiate `GameManager(num_players)`.
            *   Instantiate `UIManager(window)`.
            *   Call `game_manager.start_game()`.
        *   **Main Game Loop (`while True`):**
            1.  `action = ui_manager.get_player_input(game_manager)`: Poll for and process user input. This is non-blocking.
            2.  `game_manager.update(action)`: Pass the user's action to the game manager to update the game's logical state.
            3.  `ui_manager.draw_game_state(game_manager)`: Render the current state of the game to the screen.
            4.  `window.update()`: Refresh the PPLay window.
            5.  Check for a win condition (only one player not bankrupt). If met, display a victory screen and end the loop.