"""Processing for Day 09"""

def mirage_maintenance(report: str, reverse: bool) -> int:
    """Take the report and return the appropriate value"""

    prediction = 0

    for history in report.splitlines():
        history = [int(value) for value in history.split(" ")]
        if reverse:
            history = history[::-1]
        while sum(history):
            prediction += history[-1]
            for i in range(len(history) - 1):
                history[i] = history[i + 1] - history[i]
            history = history[0:-1]

    return prediction
