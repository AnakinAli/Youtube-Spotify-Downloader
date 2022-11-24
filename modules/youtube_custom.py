from dotenv import load_dotenv
import os


class Youtube:
    def __init__(self, url):
        self.url = url

    def run(self, path,is_playlist):

        if is_playlist:
            os.system(
                f'youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K -o "{path}/youtube/%(title)s.%(ext)s" --yes-playlist {url}')

        else:
            os.system(
                f'youtube-dl --extract-audio -o "{path}/youtube/%(title)s.%(ext)s" --audio-format mp3 {self.url}')
