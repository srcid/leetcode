# Juxt
# Apply multiple functions to the same value

# Non reusable approach
def applies(val, *funcs):
    for func in funcs:
        yield func(val)

lt_10 = lambda s: len(s) < 10
gt_3 = lambda s: len(s) > 3
has_at = lambda s: '@' in s

s = 'alcides'

# Right way
def juxt(*funcs):
    def inner(val):
        for f in funcs:
            yield f(val)

    return inner


str_validator = juxt(lt_10, gt_3, has_at)

print(*(f(s) for f in (lt_10, gt_3, has_at)))
print(*applies(s, lt_10, gt_3, has_at))
print(*str_validator(s))

def compose(*funcs):
    def inner(val):
        result = val
        for f in reversed(funcs):
            result = f(result)

    return inner

def zip_with(func):
    def inner(seq_a, seq_b, /):
        yield from map(func, seq_a, seq_b)
    
    return inner

print(*map((lambda x, y: (x, y)), [1,2,3], [3,2,1]))

from operator import add, sub, mul, truediv

print(*zip_with(add)([1,2,3], [3,2,1])) 
print(*zip_with(sub)([1,2,3], [3,2,1]))
print(*zip_with(mul)([1,2,3], [3,2,1]))
print(*zip_with(truediv)([1,2,3], [3,2,1]))