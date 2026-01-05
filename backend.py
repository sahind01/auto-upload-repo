from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Dosyaların bulunduğu klasör
base_dir = os.path.abspath(os.path.dirname(__file__))
downloads_dir = os.path.join(base_dir, "downloads")  # yandim.mp3 için

@app.route('/')
def index():
    return send_from_directory(base_dir, 'index4.html')

@app.route('/downloads/<path:filename>')
def serve_downloads(filename):
    return send_from_directory(downloads_dir, filename)

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4400))  # Render port'u alır, yoksa 4400
    print(f"Sunucu başlatıldı: http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
