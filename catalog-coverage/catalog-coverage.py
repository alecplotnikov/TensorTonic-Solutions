def catalog_coverage(recommendations, n_items):
    """
    Returns the fraction of catalog items that were recommended.
    """
    items = set()
    for rec in recommendations:
        items.update(rec)
    return len(items) / n_items if n_items > 0 else 0.0
