def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    ans = x0
    for _ in range(steps):
        ans = ans - lr * (2 * a * ans + b)
    return ans