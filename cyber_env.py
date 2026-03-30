import numpy as np

class CyberThreatEnv:
    def __init__(self):
        self.num_servers = 5
        self.state = np.zeros(self.num_servers) 
        self.steps_taken = 0
        self.max_steps = 20

    def reset(self):
        #starting Envirment
        
        self.state = np.zeros(self.num_servers)
        
        self.state[np.random.randint(0, self.num_servers)] = 1
        self.steps_taken = 0
        return self.state, {}

    def step(self, action):
    
        self.steps_taken += 1
        reward = 0.0
        done = False

        
        if self.state[action] == 1:
            reward = 1.0  
            self.state[action] = 0 
        else:
            reward = -0.1 

        
        if np.random.rand() > 0.7:
            idx = np.random.randint(0, self.num_servers)
            if self.state[idx] < 3: self.state[idx] += 1

        
        if self.steps_taken >= self.max_steps or np.all(self.state == 0):
            done = True

        return self.state, reward, done, {}

    def get_state(self):
        return self.state