def distributeBandwidth(bandwidths, requests, total_bandwidth):
    """
    Parameters
    ----------
    bandwidths: list of int
        Bandwidths that each service requires
    requests: list of int
        Number of serviceable requests for each service
    total_bandwidth: int
        Maximum bandwidth that can be used

    Returns
    -------
    int:
        Maximum possible requests that can be served with total_bandwidth
    """

    n = len(bandwidths)
    dp = [[0] * (total_bandwidth + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(total_bandwidth + 1):
            dp[i][j] = dp[i-1][j]

            if j >= bandwidths[i-1]:
                dp[i][j] = max(
                    dp[i][j],
                    dp[i-1][j-bandwidths[i-1]] + requests[i-1]
                )

    return dp[n][total_bandwidth]
