from dotenv import load_dotenv
import os


class Spotify:
    def __init__(self, url):
        self.url = url

    def run(self, path):
        os.system(f'export SPOTIPY_CLIENT_ID={os.getenv("SPOTIPY_CLIENT_ID")} &&'
                  f' export SPOTIPY_CLIENT_SECRET={os.getenv("SPOTIPY_CLIENT_SECRET")} &&'
                  f' spotify_dl -l {self.url} -o {path}/spotify')
