# Print a chess board modeled as graph using graphviz


def adj(i: int, j: int) -> tuple[tuple[int, int], ...]:
    return ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))


def isv(i: int, j: int) -> bool:
    return (0 <= i < 8) and (0 <= j < 8)


w, b = [], []

for i in range(8):
    for j in range(8):
        if (i + j) % 2:  # white
            w.append((i, j))
        else:  # black
            b.append((i, j))

print(",".join(map(lambda e: f"{e[0]}.{e[1]}", w)) + " [style=filled,fillcolor=white]")
print(
    ",".join(map(lambda e: f"{e[0]}.{e[1]}", b))
    + " [style=filled, fillcolor=black, fontcolor=white]"
)
print()

for i in range(8):
    for j in range(8):
        print(f"{i}.{j} -- " + ",".join(f"{p}.{q}" for p, q in adj(i, j) if isv(p, q)))
