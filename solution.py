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
    xmin = x.min()
    xmax = x.max()
    n = len(x)
    c = np.power(alpha, -1/(n-1)) - 1
    R = xmax - xmin
    xmax + c * R
    return xmax, xmax + c * R
