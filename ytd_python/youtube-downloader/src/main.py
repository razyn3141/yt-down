# main.py

import os
import shutil
from pathlib import Path
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

        # Delete the temporary video and audio files
        if os.path.exists(video_file):
            os.remove(video_file)
        if os.path.exists(audio_file):
            os.remove(audio_file)

        # Move the final output to the Downloads folder
        downloads_folder = str(Path.home() / "Downloads")
        final_output_path = os.path.join(downloads_folder, output_file)
        shutil.move(output_file, final_output_path)

        print(f"Video and audio have been muxed successfully into {final_output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
