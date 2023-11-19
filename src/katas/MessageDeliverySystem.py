def getMessageStatus(timestamps, messages, k):
    """
    Parameters
    ----------
    timestams: list of int
        List of the timestamps at which the messages arrive
    messages: list of str
        List of the messages which arrived at their corresponding timestamps
    k: int
        Time duration for which the messages are in memory

    Returns
    -------
    list of bool
        List of success states (whether message is delivered or not)
    """
    result = []
    tracker = {}

    for timestamp, message in zip(timestamps, messages):
        prev_arrival_time = tracker.get(message, None)

        if not prev_arrival_time:
            result.append(True)

        elif timestamp - prev_arrival_time > k:
            result.append(True)

        else:
            result.append(False)

        tracker[message] = timestamp

    return result
