from flask import Flask, jsonify, request
from cyber_env import CyberThreatEnv
import numpy as np

app = Flask(__name__)


env = CyberThreatEnv()

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

if __name__ == '__main__':
    
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)