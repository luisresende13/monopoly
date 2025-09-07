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