class UnionFind:
    def __init__(self) -> None:
        self.sets: list[set] = []

    def makeset(self, e):
        s = {e}
        self.sets.append(s)
        return s

    def find(self, e):
        for _set in self.sets:
            if e in _set:
                return _set

        return self.makeset(e)

    def union(self, r: set, s: set):
        self.sets.remove(s)
        self.sets.remove(r)
        self.sets.append((r | s))
