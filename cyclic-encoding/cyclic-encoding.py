import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    # Write code here
    ans = []
    for v in values:
        angle = 2 * math.pi * v / period
        ans.append([math.sin(angle), math.cos(angle)])
    return ans