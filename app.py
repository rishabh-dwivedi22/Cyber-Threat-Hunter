from flask import Flask, jsonify, request, send_from_directory
from cyber_env import CyberThreatEnv
import os

app = Flask(__name__)
env = CyberThreatEnv()


base_path = os.getcwd()
static_path = os.path.join(base_path, 'frontend', 'dist')
if not os.path.exists(os.path.join(static_path, 'index.html')):
    static_path = os.path.join(base_path, 'dist')

app.static_folder = static_path

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


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory(os.path.join(app.static_folder, 'assets'), path)

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)