type Node = int | str
type Cost = int | float
type Edge = tuple[Node, Node, Cost] 
type Adjancency = tuple[Node, Cost]
type AdjacencyList = dict[Node, list[Adjancency]]
type EdgesList = list[Edge]
