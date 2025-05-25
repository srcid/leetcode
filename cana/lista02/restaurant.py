def orders(nclients: int, time: list[int]) -> list[int]:
    """order in which clients should be served

    Args:
        nclients (int): number of clients
        time (list[int]): time to serve client i

    Returns:
        list[int]: sequence of clients in order to be served
    """

    ans = [idx for idx, _ in sorted(zip(range(nclients), time), key=lambda e: e[1])]

    return ans
