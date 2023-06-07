from typing import List

class Solution:
    def spiral_aux(self, i, j, p, q):
        """ i => index of first line of matrix
            j => index of first column of matrix
            p => index of last line of matrix
            q => index of last column of matrix
        """

        # case of empty matrix
        if i > p or j > q:
            return []
        
        # case of single row
        if i == p:
            return self.matrix[i][j:q+1]

        # case of single column
        if j == q:
            return [ row[j] for row in self.matrix[i:p+1] ]
        
        return (
            self.matrix[i][j:q+1] +
            [ row[q] for row in self.matrix[i+1:p] ] +
            list(reversed(self.matrix[p][j:q+1])) +
            list(reversed([ row[j] for row in self.matrix[i+1:p] ])) +
            self.spiral_aux(i+1,j+1, p-1, q-1)
        )

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])
        self.matrix = matrix

        return self.spiral_aux(0, 0, M-1, N-1)
    

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m3 = [[1,2],[3,4]]

s = Solution()
print(s.spiralOrder(m1))
print(s.spiralOrder(m2))
print(s.spiralOrder(m3))