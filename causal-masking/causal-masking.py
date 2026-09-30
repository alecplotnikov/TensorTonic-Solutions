import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    scores = np.asarray(scores, dtype=float)
    sequence_length = scores.shape[-1]
    future = np.triu(
        np.ones((sequence_length, sequence_length), dtype=bool),
        k=1,
    )
    masked = scores.copy()
    masked[..., future] = mask_value
    return masked
