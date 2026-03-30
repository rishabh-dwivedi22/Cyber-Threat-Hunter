from cyber_env import CyberThreatEnv
import time

def run_baseline_test():
    env = CyberThreatEnv()
    state, info = env.reset()
    print("--- Cyber SOC Environment Started ---")
    print(f"Initial Network State: {state}")

    total_reward = 0
    done = False
    step_count = 0

    while not done:
        step_count += 1
        
        action = env.state.argmax() if 1 in env.state else env.np.random.randint(0, 5)
        
        state, reward, done, info = env.step(action)
        total_reward += reward
        
        print(f"Step {step_count}: Action (Patch Server {action}) | Reward: {reward} | New State: {state}")
        time.sleep(0.5) 

    print("--- Simulation Finished ---")
    print(f"Total Reward: {total_reward}")

if __name__ == "__main__":
    run_baseline_test()