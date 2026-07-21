import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))
    c = Counter(x)
    mx = max(c.values())
    modes = [val for val, count in c.items() if count == mx]
    mode = float(min(modes))
    
    return mean, median, mode
    