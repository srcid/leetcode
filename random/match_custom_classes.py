class ListNode:
    __match_args__ = ("val", "button")  # required for match positional attributes

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} {self.next}"


match ListNode(1), ListNode(2):
    case ListNode(a), ListNode(b):
        print(a, b)
    case ListNode(val=a), ListNode(val=b):
        print(a, b)
    case a, b if isinstance(a, ListNode) and isinstance(b, ListNode):
        print(a, b)

match ["str", 1]:
    case int(a), int(b):
        print("dois inteiros", a, b)
    case str(a), int(b):
        print("primeiro é string", a, b)
