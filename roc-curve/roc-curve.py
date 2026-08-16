import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=int)
    y_score = np.asarray(y_score, dtype=float)
    P = int(np.sum(y_true == 1))
    N = int(np.sum(y_true == 0))
    order = np.lexsort((y_true, -y_score))
    y_true_sorted = y_true[order]
    y_score_sorted = y_score[order]
    fprs, tprs, thresholds = [0.0], [0.0], [float("inf")]
    tp, fp, i = 0, 0, 0
    n_items = len(y_true_sorted)
    while i < n_items:
        j = i
        while j < n_items and y_score_sorted[j] == y_score_sorted[i]:
            if y_true_sorted[j] == 1:
                tp += 1
            else:
                fp += 1
            j += 1
        fprs.append(fp / N if N > 0 else 0.0)
        tprs.append(tp / P if P > 0 else 0.0)
        thresholds.append(float(y_score_sorted[i]))
        i = j
    return fprs, tprs, thresholds