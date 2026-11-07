import discord
from bot_logic import gen_pass 
from bot_logic import coin_flip
from bot_logic import rps_game
from bot_logic import dice_roll
# intents variable stores the permissions of the bot
intents = discord.Intents.default()
# Enable the permission to read message content
intents.message_content = True
# Create a bot and pass the intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('?coinflip'):
        await message.channel.send(coin_flip())
    elif message.content.startswith('?rps'):
        await message.channel.send(rps_game())
    elif message.content.startswith('?add'):
        parts = message.content.split()
        total = int(parts[1]) + int(parts[2])
        await message.channel.send(str(total))
    elif message.content.startswith("?"):
        count, sides = message.content[1:].lower().split("d")
        result = dice_roll(int(count or 1), int(sides))
        await message.channel.send(result)
    else:
        await message.channel.send(message.content)


client.run("TOKEN")
