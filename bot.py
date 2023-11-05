import discord
import responses
from discord.ext.commands import Bot
from discord.ext import commands
from config import TOKEN

async def send_message(message: str, user_message: str, is_private: bool) -> str:
    try:
        response = responses.handle_response(user_message)

        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():

    # Token is imported from config

    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):

        # Ignore messages sent by bot itself
        if message.author == client.user:
            return
        
        username: str = str(message.author)
        user_message: str = str(message.content)
        channel: str = str(message.channel)

        # Console log the message traffic
        print(f'{username} said: {user_message} ({channel})')

        # Process command sign
        if user_message.startswith('?'):
            user_message = user_message[1:]
            await(send_message(message=message, user_message=user_message, is_private=False))
        else:
            await send_message(message=message, user_message=user_message, is_private=True)

    client.run(TOKEN)