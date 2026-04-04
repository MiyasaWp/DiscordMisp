import os
import yaml
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self, path="config.yaml"):
        with open(path) as f:
            self._cfg = yaml.safe_load(f)

        self.misp_url = os.getenv("MISPurl", self._cfg["misp"]["url"])
        self.misp_key = os.getenv("MISPapiKey")
        self.discord_token = os.getenv("LeToken")
        self.poll_interval = self._cfg["misp"].get("poll_interval", 300)
        self.channels = self._cfg["discord"]["channels"]
        self.filters = self._cfg.get("filters", {})