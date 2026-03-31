from flask import Flask, jsonify, request, send_from_directory
from cyber_env import CyberThreatEnv
import os

app = Flask(__name__)
env = CyberThreatEnv()


def get_index_path():
    paths = [
        os.path.join(os.getcwd(), 'frontend', 'dist'),
        os.path.join(os.getcwd(), 'dist'),
        os.getcwd() # Agar file bahar hi padi hai
    ]
    for p in paths:
        if os.path.exists(os.path.join(p, 'index.html')):
            return p
    return os.getcwd()

app.static_folder = get_index_path()

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/state', methods=['GET'])
def get_state():
    current_state = env.reset() 
    return jsonify(state=current_state.tolist())

@app.route('/step', methods=['POST'])
def take_step():
    data = request.json or {}
    action = data.get('action', 0) 
    next_state, reward, done, info = env.step(action)
    return jsonify(state=next_state.tolist(), reward=reward, done=done)


@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)