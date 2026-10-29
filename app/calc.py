def uptime_percent(up, total):
    """Percent of checks that were UP, rounded to 2 decimals.

    If there are no checks yet (total == 0), uptime is 0.0.
    """
    return round(up / total * 100, 2)
