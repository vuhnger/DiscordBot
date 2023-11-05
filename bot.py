import discord
import responses

async def send_message(message: str, user_message: str, is_private: bool) -> str:
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():

    TOKEN = 'MTE3MDUzMjE4NTk1OTMwMTIxMg.GFTzug.b_GjIZiTp_9DEFhxh5rp17D9r4M8H8pK1UNAhY'

    client = discord.client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)