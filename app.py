from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__, template_folder='templates')

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        yt_url = request.form['url']
        output_path = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")

        # Download audio using yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(yt_url, download=True)
            mp3_path = os.path.join(DOWNLOAD_FOLDER, f"{info['title']}.mp3")

        return send_file(mp3_path, as_attachment=True, mimetype="audio/mpeg")

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
