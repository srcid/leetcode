from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        boats = 0

        if limit == 1:
            return N

        people.sort(reverse=True)
        i, j = 0, N-1

        while i < j:
            if people[j] <= limit - people[i]:
                j -= 1
            
            i += 1
            boats += 1

        if j-i == 0:
            boats += 1
        
        return boats

cases = (
    ([1,2],       3),
    ([3,2,2,1],   3),
    ([3,5,3,4],   5),
    ([3,8,7,1,4], 9),
    ([3,8,4,9,2,2,7,1,6,10,6,7,1,7,7,6,4,4,10,1], 10)
)

sol = Solution()

for people, limit in cases:
    print(sol.numRescueBoats(people, limit))
    