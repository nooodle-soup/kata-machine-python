def efficientServerSetup(memory):
    """
    Parameters
    ----------
    memory: list of int
        List of data for each server

    Return
    ------
    int
        Maximum possible server efficiency
    """

    MOD = 10**7
    efficiency = 0
    mid = len(memory) // 2

    for idx in range(mid):
        min_ = min(memory[idx], memory[-1-idx])
        max_ = max(memory[idx], memory[-1-idx])

        memory[idx], memory[-1-idx] = min_, max_

    for idx, data in enumerate(memory):
        efficiency += (idx+1) * data

    return efficiency % MOD
