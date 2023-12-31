import random

fortnite_drop_spots = [
    "Junk Junction",
    "Haunted Hills",
    "Pleasant Park",
    "Snobby Shores",
    "Tilted Towers",
    "Greasy Grove",
    "Shifty Shafts",
    "Flush Factory",
    "Fatal Fields",
    "Lucky Landing",
    "Paradise Palms",
    "Retail Row",
    "Lonely Lodge",
    "Wailing Woods",
    "Risky Reels",
    "Tomato Town",
    "Loot Lake",
    "Dusty Divot",
    "Salty Springs"
]

drop_commands = {'drop', 'd', 'droppe', 'spot'}

def handle_response(message: str) -> str:
    processed_message: str = message.lower()

    if processed_message == 'help':
        return f'´Bruk ?drop for å få et landingssted fra meg.´'
    
    if processed_message in drop_commands:
        return f'{fortnite_drop_spots[random.randint(0, len(fortnite_drop_spots))]}'
    