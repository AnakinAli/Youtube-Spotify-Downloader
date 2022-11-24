import os
from colored import fg, attr, style
from dotenv import load_dotenv
from modules.spotify_custom import Spotify
from modules.youtube_custom import Youtube


# returns welcome screen
def load_screen():
    spotify_text = open('./welcome_screen/spotify.txt', 'r').readlines()
    youtube_text = open('./welcome_screen/youtube.txt', 'r').readlines()
    download_text = open('./welcome_screen/download.txt', 'r').read()

    for line in range(0, len(spotify_text) - 1):
        spotify_line = spotify_text[line].split('\n')
        youtube_line = youtube_text[line].split('\n')

        for spotify_symb in spotify_line:
            print(f'{fg("green")}{style.BOLD}{spotify_symb}{attr("reset")}', end='')

        for youtube_symb in youtube_line:
            if line == 0:
                print(f'{fg("red")}{style.BOLD}       {youtube_symb}{attr("reset")}', end='')
            else:
                print(f'{fg("red")}{style.BOLD}{youtube_symb}{attr("reset")}', end='')
        print()

    print(f'{fg("turquoise_4")}{style.BOLD}{download_text}{attr("reset")}')


if __name__ == "__main__":
    load_screen()
    load_dotenv()

    print(attr("reset"))
    url = input(f'{fg("red")}Enter Link: {attr("reset")}')

    change_directory = input(
        f'{fg("yellow")}Do you want to change the directory from "~/Music" [Y/n]: {attr("reset")}').lower()

    if change_directory == 'y':
        songs_path = str(input(f'{fg("green")}New path(~/ included): '))
    else:
        songs_path = str('~/Music')

    songs_path = songs_path.replace('~/', os.getenv('SONG_PATH'))
    print(f'{fg("spring_green_4")}{style.BOLD}Save Folder Path: {songs_path}{attr("reset")}')

    if 'www.youtube.com' in url:
        youtube = Youtube(url=url)
        youtube.run(songs_path,'playlist' in url)
    elif 'spotify.com' in url:
        spotify = Spotify(url=url)
        spotify.run(songs_path)
    else:
        print(f'{fg("red")}Invalid Link must be spotify/youtube{attr("reset")}')
        exit(0)

    # sudo vi /etc/profile.d/song_downloader_from_python.sh
    # source  /etc/profile.d/song_downloader_from_python.sh
