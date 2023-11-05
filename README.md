# DiscordBot

This Discord bot is written in Python and is designed to enhance the gaming experience for Fortnite players on Discord. It simplifies the decision-making process by randomly selecting landing spots within the game.

## Features

- **Drop Spot Selector**: With a simple command, the bot selects a random drop spot from Fortnite, making the choice easier for players.
- **Help Command**: Users can get information on how to use the bot with a quick command.

## Commands

- `?drop`: Returns a random Fortnite landing spot.
- `?help`: Provides information about the bot's functionalities.

## Installation

To set up the bot for your server, follow these steps:

1. **Clone the repository**:
git clone https://github.com/yourusername/DiscordBot.git
cd DiscordBot

2. **Install dependencies**:
pip install discord


3. **Configuration**:
- Create a `config.py` file in the root directory.
- Add your Discord bot token in `config.py`:
  ```python
  TOKEN = "your_bot_token_here"
  ```
- Ensure `config.py` is listed in your `.gitignore` to keep your token secure.

4. **Run the bot**:
python main.py


## Usage

Once the bot is running on your Discord server, you can use the following commands:

- Send `?drop` in a channel where the bot is present to receive a random drop spot.
- Send `?help` to get a list of available commands.

## Contributing

Contributions to the bot are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a new Pull Request.

## License

This project is open-sourced under the MIT License.

## Acknowledgements

- A big thank you to the creators of the [discord.py](https://github.com/Rapptz/discord.py) library.

## Contact

For any queries or support, feel free to contact me at [victou@uio.no](mailto:victou@uio.no).


