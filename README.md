# YouTube to MP3 Converter 🎵

## Overview

This is a simple Flask web application that allows users to convert YouTube videos into MP3 audio files. The app takes a YouTube video URL as input, processes the audio extraction using `yt-dlp`, and provides the MP3 file for download.

## Features 🚀

- 🎶 Converts YouTube videos to MP3 format
- ⚡ Uses `yt-dlp` for audio extraction
- 🌐 Flask-based web interface
- 📂 Automatic file organization in a `downloads` directory

## Requirements 📌

Ensure you have the following dependencies installed before running the application:

- 🐖 Python 3.x
- 🔥 Flask
- 🎮 yt-dlp
- 🎧 FFmpeg (required for audio extraction)

## Installation 🛠️

1. Clone this repository:

   ```bash
   git clone https://github.com/Asuratcp/youtube-mp3-flask.git
   cd youtube-mp3-flask
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg (if not already installed):

   - **Windows:** Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **MacOS:** Install via Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **Linux:** Install via package manager:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```

## Usage ▶️

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open a web browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

3. Enter a YouTube video URL and click "Convert" to download the MP3 file.

## Project Structure 📂

```
/your_project_directory
│── app.py                # Main Flask application
│── templates/
│   └── index.html        # HTML template for UI
│── downloads/            # Directory to store MP3 files
└── README.md             # Project documentation
```

## Troubleshooting 🛠️

- ❌ **`yt-dlp`** not found? Ensure it's installed via `pip install yt-dlp`.
- ⚠️ **FFmpeg errors?** Confirm that FFmpeg is correctly installed and accessible in your system's PATH.
- 🔑 **Permission issues?** Run the script with appropriate permissions or try running as an administrator.

## License 🐜

This project is open-source and available under the MIT License.

## Author ✨

Tara Chandra Pandey - [Profile](https://github.com/Asuratcp)

