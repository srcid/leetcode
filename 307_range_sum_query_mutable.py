from typing import List

from collections import namedtuple

Interval = namedtuple('interval', ['start', 'end'])
Node = namedtuple('node', ['key', 'interval'])


class NumArray:
    def __init__(self, nums: List[int]):
        N = len(nums)
        self.nums = nums
        self.interval = Interval(0, N-1)
        self.values = [None] * (4 * N)
        self.populate(0, self.interval)

    @staticmethod
    def mid(i):
        return i.start + (i.end - i.start) // 2

    @staticmethod
    def left(idx):
        return 2 * idx + 1

    @staticmethod
    def right(idx):
        return 2 * idx + 2

    def populate(self, idx, i):
        if i.end - i.start == 0:
            self.values[idx] = Node(self.nums[i.start], i)
            return self.values[idx].key

        MID = self.mid(i)
        left = self.populate(self.left(idx), Interval(i.start, MID))
        right = self.populate(self.right(idx), Interval(MID+1, i.end))
        self.values[idx] = Node(left + right, i)

        return self.values[idx].key

    def sum(self, idx, i):
        key, ni = self.values[idx]

        if ni == i:
            return key

        MID = self.mid(ni)

        if ni.start <= i.start and i.end <= MID:
            return self.sum(self.left(idx), i)

        if MID+1 <= i.start and i.end <= ni.end:
            return self.sum(self.right(idx), i)

        return (
            self.sum(self.left(idx), Interval(i.start, MID))
            + self.sum(self.right(idx), Interval(MID+1, i.end))
        )

    def upgrade(self, idx, i, newKey):
        _, ni = self.values[idx]

        if ni == i:
            self.values[idx] = Node(newKey, ni)
            return newKey

        MID = self.mid(ni)

        if ni.start <= i.start and i.end <= MID:
            self.values[idx] = Node(
                self.upgrade(self.left(idx), i, newKey) + self.values[self.right(idx)].key,
                ni
            )
        elif MID + 1 <= i.start and i.end <= ni.end:
            self.values[idx] = Node(
                self.upgrade(self.right(idx), i, newKey) + self.values[self.left(idx)].key,
                ni
            )
        
        return self.values[idx].key 

    def update(self, index: int, val: int) -> None:
        self.values[0] = Node(
            self.upgrade(0, Interval(index, index), val),
            self.interval
        )

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(0, Interval(left, right))


if __name__ == '__main__':
    nums = [1,3,5,7,9,11]
    narr = NumArray(nums)
    print(narr.sumRange(1,5))
    narr.update(5, 13)
    print(narr.sumRange(1,5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
