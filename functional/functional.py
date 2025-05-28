def flip(f):
    def inner(*args):
        return f(*reversed(args))

    return inner


def compose(*funcs):
    def inner(val):
        for f in reversed(funcs):
            val = f(val)

        return val

    return inner


def pipe(*funcs):
    def inner(val):
        for f in funcs:
            val = f(val)

        return val

    return inner


def zip_with2(func):
    def inner(seq_a, seq_b, /):
        yield from map(func, seq_a, seq_b)

    return inner


def zip_with(func):
    def inner(*iters):
        yield from map(func, *iters)

    return inner


def juxt(*funcs):
    def inner(val):
        for f in funcs:
            yield f(val)

    return inner
