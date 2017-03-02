import youtube_dl

def download_mp3(url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    download_mp3("https://www.youtube.com/watch?v=lBwtKSrFyjI")
