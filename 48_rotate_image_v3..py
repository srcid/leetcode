from typing import List


# this was the fast approach
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        M, N = map(len, (matrix, matrix[0]))

        for i in range(M // 2):
            matrix[i], matrix[M - i - 1] = matrix[M - i - 1], matrix[i]

        for i in range(M):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)
