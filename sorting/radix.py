def radix(mod: int, arr: list[int]) -> list[int]:
    buckets = {
        i: [] for i in range(10)
    }

    for x in arr:
        buckets[(x // mod) % 10].append(x)

    for i in range(10):
        if len(buckets[i]) > 1:
            buckets[i] = radix(mod // 10, buckets[i])

    return [ v for i in range(10) for v in buckets[i] ]

arr = [124,202,97,33,99,2,100]
mod = 10**(len(f'{max(arr)}')-1)

print(radix(mod, arr))

#print(radix([5,0,3,2,1,5,6,9,4,7,8]))