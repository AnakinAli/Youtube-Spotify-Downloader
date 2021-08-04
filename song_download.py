#!/usr/bin/env python3
import os
from termcolor import colored
from dotenv import dotenv_values


def check_is_youtube_platform(url):
    domain = url.split('/')[2]
    if 'youtube' in domain:
        print(f'Domain: {colored("Youtube", "red")}')
        return True
    elif 'spotify' in domain:
        print(f'Domain: {colored("Spotify", "green")}')
        return False
    return True


def check_if_playlist(url):
    is_playlist = url.split('/')[3].split('?')[0] == 'playlist'
    print('Playlist: ', end="")

    if is_playlist:
        print(colored('True', 'green'))
    else:
        print(colored('False', 'red'))
    return url.split('/')[3].split('?')[0] == 'playlist'


if __name__ == "__main__":

    # Load .env
    config = dotenv_values('.env')

    url = input(colored('Link: ', "blue"))

    change_directory = input(colored('Do you want to change the directory from "~/Music" [Y/n]: ', 'yellow')).lower()
    if change_directory == 'y':
        songs_path = str(input(colored('New path: ', 'green')))
    else:
        songs_path = '~/Music'

    # from ~/ to /home/username
    songs_path = songs_path.replace('~/', config.get('SONGS_PATH'))

    is_playlist = check_if_playlist(url)
    is_youtube = check_is_youtube_platform(url)

    if is_youtube:
        if is_playlist:
            os.system(
                f'youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K -o "{songs_path}/youtube/%(title)s.%(ext)s" --yes-playlist {url}')

        else:
            os.system(
                f'youtube-dl --extract-audio -o "{songs_path}/youtube/%(title)s.%(ext)s" --audio-format mp3 {url}')
    else:

        os.system(f'export SPOTIPY_CLIENT_ID=5b0c015af53d43ed8d5f4317c1f76e83 &&'
                  f' export SPOTIPY_CLIENT_SECRET=04d8fe2163ba46ef826cb05607ee265f &&'
                  f' spotify_dl -l {url} -o {songs_path}/spotify')

# sudo vi /etc/profile.d/song_downloader_from_python.sh
# source  /etc/profile.d/song_downloader_from_python.sh
