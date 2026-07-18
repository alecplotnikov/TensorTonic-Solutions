import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    ans = 0.0
    if len(y) > 0:
        c = np.unique(y, return_counts=True)
        freq = []
        t = sum(c[1])
        for f in c[1]:
            freq.append(f / t)
        ans = 0
        for f in freq:
            if f > 0:
                ans += (-f) * np.log2(f)
    return ans