import os
from dotenv import load_dotenv


load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
MISP_URL = os.getenv('MISP_URL')
MISP_KEY = os.getenv('MISP_API_KEY')

# suite a faire