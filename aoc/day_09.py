"""Processing for Day 09"""

def mirage_maintenance(report: str, reverse: bool) -> int:
    """Take the report and return the appropriate value"""

    prediction = 0

    for history in report.splitlines():
        parsed_history = [int(value) for value in history.split(" ")]
        if reverse:
            parsed_history = parsed_history[::-1]
        while sum(parsed_history):
            prediction += parsed_history[-1]
            for i in range(len(parsed_history) - 1):
                parsed_history[i] = parsed_history[i + 1] - parsed_history[i]
            parsed_history = parsed_history[0:-1]

    return prediction
