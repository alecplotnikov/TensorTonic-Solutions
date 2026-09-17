import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    values = np.asarray(V, dtype=float).copy()
    target = r + gamma * values[s_next]
    values[s] += alpha * (target - values[s])
    return values
