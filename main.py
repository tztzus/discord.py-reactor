import discord

ACCOUNT_TOKEN = ""  # Put your account token here, NOT A BOT TOKEN
TARGET_CHANNEL_ID = s  # Put your channel ID here. Server channels, DMs, and GCs also work.

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("=========================================")
    print("        Script by @zus.s on Discord       ")
    print("=========================================")
    print(f"Logged in as {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message):
    if message.channel.id == TARGET_CHANNEL_ID:
        try:
            await message.add_reaction("🍍")
            await message.add_reaction("🥧")
            await message.add_reaction("🏳️‍⚧️")  # You can add your own emojis here
            await message.add_reaction("🏳️‍🌈")
            for emoji in "🇫🇪🇲🇧🇴🇾":
                await message.add_reaction(emoji)
        except Exception as e:
            print(f"Failed to add reaction: {e}")

client.run(ACCOUNT_TOKEN, bot=False)
