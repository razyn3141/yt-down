# YouTube Downloader

This project is a Python script that allows users to download YouTube videos in maximum quality and mux the audio to ensure compatibility with Adobe Premiere.

## Features

- Download videos in maximum quality.
- Download audio tracks separately.
- Mux video and audio into a single file compatible with Adobe Premiere.

## Project Structure

```
youtube-downloader
├── src
│   ├── main.py          # Entry point of the application
│   ├── downloader.py    # Handles downloading video and audio
│   ├── muxer.py         # Combines video and audio files
│   └── utils.py         # Utility functions for the project
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd youtube-downloader
pip install -r requirements.txt
```

## Usage

Run the main script to start downloading videos:

```bash
python src/main.py
```

Follow the prompts to enter the YouTube video URL. The script will download the video and audio, then mux them into a single file.

## Dependencies

This project requires the following Python packages:

- `pytube`: For downloading videos from YouTube.
- `moviepy`: For muxing audio and video files.

Make sure to install these packages using the `requirements.txt` file provided.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.