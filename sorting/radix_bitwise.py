from numpy.random import randint
from time import time_ns

def radix(arr, bit=2**31):
    if len(arr) < 2:
        return arr
    
    zeros = list(filter(lambda e: not e & bit, arr))
    ones = list(filter(lambda e: e & bit, arr))

    # Negative numbers will have the most significant bit set to one
    if bit == 2**31:
        zeros, ones = ones, zeros

    if nextbit := bit // 2:
        zeros = radix(zeros, bit=nextbit) 
        ones = radix(ones, bit=nextbit)
    
    return zeros + ones

arr = randint(-100, 100, size=1_000_000)

start = time_ns()
radix(arr)
elapsed = time_ns() - start
print(f'radix took {round(elapsed * 1e-9, 2)} seconds')

start = time_ns()
sorted(arr)
elapsed = time_ns() - start
print(f'sorted took {round(elapsed * 1e-9, 2)} seconds')
