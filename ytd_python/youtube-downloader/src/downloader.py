import yt_dlp

class Downloader:
    def __init__(self):
        pass

    def download_video(self, url):
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]',
            'outtmpl': 'video.mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return 'video.mp4'

    def download_audio(self, url):
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]',
            'outtmpl': 'audio.m4a'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return 'audio.m4a'