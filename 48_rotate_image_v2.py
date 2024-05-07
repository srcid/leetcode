from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        M, N = map(len, (matrix, matrix[0]))

        for i in range(M):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [
        [1,   2,  3,  4,  5],
        [6,   7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    s = Solution()
    s.rotate(matrix)
    print(matrix)
    s.rotate(matrix2)
    print(matrix2)
