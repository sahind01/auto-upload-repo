from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Dosyaların bulunduğu klasör (index.html ve yandim.mp3 burada olmalı)
base_dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def index():
    return send_from_directory(base_dir, 'index4.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    print("Sunucu başlatıldı: http://127.0.0.1:5004")
    app.run(debug=True, port=5004)

