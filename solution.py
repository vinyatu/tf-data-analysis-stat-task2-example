import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5991293770 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return (max(x) - 0.068) / (1 - alpha), \
            
