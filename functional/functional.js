function pipe(...funcs) {
    function inner(val) {
        funcs.forEach(
            (f) => {val = f(val)}
        )

        return val
    }

    return inner
}

const pipe = (...funcs) => (x) => funcs.reduce((v, f) => f(v), x)
