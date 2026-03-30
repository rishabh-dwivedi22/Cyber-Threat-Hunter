import numpy as np

def calculate_normalized_score(total_reward, max_possible_reward, min_possible_reward):
    """Score ko 0.0 se 1.0 ke scale par laane ke liye formula"""
    if total_reward <= min_possible_reward:
        return 0.0
    elif total_reward >= max_possible_reward:
        return 1.0
    else:
        return (total_reward - min_possible_reward) / (max_possible_reward - min_possible_reward)

def easy_grader(env_log):
    
    total_reward = sum(env_log['rewards'])
    
    
    max_reward = 1.0 
    min_reward = -0.5 
    
    score = calculate_normalized_score(total_reward, max_reward, min_reward)
    print(f"[SOC SYSTEM] Easy Task Evaluation: {score:.2f}/1.0")
    return score

def medium_grader(env_log):
    
    total_reward = sum(env_log['rewards'])
    servers_crashed = env_log['final_state'].count(3) 
    
    
    if servers_crashed > 0:
        return 0.0
        
    max_reward = 3.0 
    min_reward = -1.5 
    
    score = calculate_normalized_score(total_reward, max_reward, min_reward)
    print(f"[SOC SYSTEM] Medium Task Evaluation: {score:.2f}/1.0")
    return score

def hard_grader(env_log):
    
    total_reward = sum(env_log['rewards'])
    servers_crashed = env_log['final_state'].count(3)
    
    
    if servers_crashed >= 2:
        return 0.0 
        
    max_reward = 5.0 
    min_reward = -3.0
    
    score = calculate_normalized_score(total_reward, max_reward, min_reward)
    print(f"[SOC SYSTEM] Hard Task Evaluation: {score:.2f}/1.0")
    return score