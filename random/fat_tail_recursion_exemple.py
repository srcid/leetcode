def fat(n):
    if n == 1:
        return n
    
    return n * fat(n-1)


def tail_fat(n, acc = 1):
    if n == 1:
        return acc
    
    return tail_fat(n - 1, acc * n)


tail_fat(10000)