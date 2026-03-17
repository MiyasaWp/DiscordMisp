import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True 


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f' Bot connecté en tant que : {bot.user.name}')
    
  
    if CHANNEL_ID:
        channel = bot.get_channel(int_channel_id := int(CHANNEL_ID))
        if channel:
            await channel.send("Le bot MISP est en ligne et prêt à surveiller !")
        else:
            print(f"Erreur : Impossible de trouver le salon avec l'ID {CHANNEL_ID}")

@bot.command()
async def ping(ctx):
    await ctx.send("Le bot répond bien.")

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Erreur : Aucun TOKEN Discord trouvé dans le fichier .env")