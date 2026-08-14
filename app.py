from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tinkle_secure_key_2026'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client_command')
def handle_client_command(data):
    command = data.get('command', '')
    print(f"[TINKLE AI] Received Command: {command}")
    
    # هنا يتم معالجة الأمر أو توجيهه للذكاء الاصطناعي محلياً
    response_payload = {
        "status": "processing",
        "message": f"PROCESSING: {command}"
    }
    emit('server_response', response_payload, broadcast=True)

if __name__ == '__main__':
    print("[INFO] Starting Tinkle AI Core Server on http://127.0.0.1:5000 ...")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
