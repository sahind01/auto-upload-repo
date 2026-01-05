from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Dosyaların bulunduğu klasörler
base_dir = os.path.abspath(os.path.dirname(__file__))
downloads_dir = os.path.join(base_dir, "downloads")  # yandim.mp3 burada

@app.route('/')
def index():
    return send_from_directory(base_dir, 'index4.html')

# /yandim.mp3 isteğini downloads klasöründen al
@app.route('/yandim.mp3')
def yandim():
    return send_from_directory(downloads_dir, 'yandim.mp3')

# Diğer statik dosyalar
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4400))  # Render port'u alır, yoksa 4400
    print(f"Sunucu başlatıldı: http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
