import pafy
import os
import sys


URL = "https://www.youtube.com/playlist?list=PLmpGtLvjAdA0TzC6v2NNT1VfasV5EkjXg"

def load_playlist(url):
    playlist = pafy.get_playlist(url)
    i = 0
    list_video = playlist['items']
    while i < len(list_video):
        try : 
            video_id = list_video[i]['playlist_meta']['encrypted_id']
            load_video(video_id)
            i += 1
        except OSError:
            i += 1
    return 1

def load_video(url):
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download(filepath = os.getcwd() + "/Download/" + video.title + ".mp3" )
    return 1

if __name__ == "__main__":
    os.makedirs("Download", mode=0o777, exist_ok=True)

    if URL[24] == 'p':
        try:
            playlist = pafy.get_playlist(URL)
        except:
            print("Why load a playlist of 1 sound?! Loads the sound directly")
            sys.exit()
        load_playlist(URL)
    elif URL[24] == 'w':
        load_video(URL)
    else:
        pass
