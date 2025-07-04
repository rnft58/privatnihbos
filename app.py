from flask import Flask, render_template, request, redirect, url_for, flash
import base64
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secretkey123'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Maks 5MB upload

# Foto disimpan di folder utama project
PHOTO_FOLDER = os.path.dirname(os.path.abspath(__file__))

VALID_USERNAME = 'noxzy'
VALID_PASSWORD = 'noxzy001'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    photo_data = request.form.get('photo')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        if photo_data:
            try:
                header, encoded = photo_data.split(",", 1)
                imgdata = base64.b64decode(encoded)
                filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
                filepath = os.path.join(PHOTO_FOLDER, filename)
                with open(filepath, "wb") as f:
                    f.write(imgdata)
                flash(f'Login berhasil! Foto tersimpan: {filename}', 'success')
            except Exception as e:
                flash(f'Login berhasil, tapi gagal simpan foto: {e}', 'warning')
        else:
            flash('Login berhasil! Namun foto tidak ditemukan.', 'info')
        return redirect(url_for('index'))
    else:
        flash('Username atau password salah!', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
