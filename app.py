import os
from flask import Flask, send_from_directory

UPLOAD_DIR = 'apk/'

app = Flask(__name__)

@app.route('/')
def main():
	return 'Service to get APK for test'

@app.route('/apk/list')
def get_apk_list():
	return os.listdir(UPLOAD_DIR)

@app.route('/apk/download/last')
# Получаем последнюю загруженную APK
def get_apk_last():
	return send_from_directory(UPLOAD_DIR, os.listdir(UPLOAD_DIR)[-1], as_attachment=True)


if __name__ == '__main__':
	app.run(host='0.0.0.0')
