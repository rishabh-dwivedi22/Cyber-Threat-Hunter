from flask import Flask, jsonify, request, send_from_directory
from cyber_env import CyberThreatEnv
import os

app = Flask(__name__)
env = CyberThreatEnv()

# --- STEP 1: Find where index.html is hiding ---
def find_static_folder():
    for root, dirs, files in os.walk(os.getcwd()):
        if 'index.html' in files:
            print(f"--- SUCCESS: Found index.html in: {root} ---")
            return root
    return os.getcwd()

app.static_folder = find_static_folder()

@app.route('/')
def serve():
    # Agar index.html mil gayi toh serve karo, warna error message dikhao
    if os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return "<h1>Dashboard Error: index.html not found!</h1><p>Check if your frontend is built and pushed.</p>", 404

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