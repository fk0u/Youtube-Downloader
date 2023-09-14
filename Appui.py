from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__, template_folder="C:\Users\KOU\Documents\GitHub\Youtube-Downloader\templates")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        link = data.get('link')
        resolution = data.get('resolution')
        is_mp3 = data.get('is_mp3')
        
        output_path = "C:\\download\\youtube_downloader"  # Ganti sesuai dengan direktori output yang Anda inginkan

        if not link:
            return jsonify({"success": False, "error": "Please provide a valid YouTube video URL."})

        yt = YouTube(link)

        if is_mp3:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=output_path)
            return jsonify({"success": True})
        else:
            video_stream = yt.streams.filter(res=resolution).first()
            video_stream.download(output_path=output_path)
            return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
