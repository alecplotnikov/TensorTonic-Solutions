import numpy as np

def epsilon_greedy(q_values, epsilon, seed=0):
    values = np.asarray(q_values, dtype=float)
    rng = np.random.default_rng(seed)
    if rng.random() < epsilon:
        return int(rng.integers(values.size))
    return int(np.argmax(values))
