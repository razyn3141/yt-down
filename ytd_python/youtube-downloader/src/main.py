# main.py

import sys
from downloader import Downloader
from muxer import Muxer

def main():
    downloader = Downloader()
    muxer = Muxer()

    video_url = input("Enter the YouTube video URL: ")

    try:
        print("Downloading video...")
        video_file = downloader.download_video(video_url)
        print("Downloading audio...")
        audio_file = downloader.download_audio(video_url)

        output_file = input("Enter the output file name (without extension): ") + ".mp4"
        print("Muxing video and audio...")
        muxer.mux(video_file, audio_file, output_file)

        print(f"Video and audio have been muxed successfully into {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()