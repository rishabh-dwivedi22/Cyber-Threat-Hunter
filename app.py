from flask import Flask, jsonify, request, send_from_directory
from cyber_env import CyberThreatEnv
import numpy as np
import os


app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')

env = CyberThreatEnv()


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/state', methods=['GET'])
def get_state():
    current_state = env.reset() 
    return jsonify(state=current_state.tolist())

@app.route('/step', methods=['POST'])
def take_step():
    data = request.json
    action = data.get('action') 
    next_state, reward, done, info = env.step(action)
    
    return jsonify(
        state=next_state.tolist(),
        reward=reward,
        done=done
    )


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)