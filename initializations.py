import discord
from discord.ext import commands
from secret_file import bot_token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = bot_token

GUILD = discord.Object(id=1286991310657683569)
