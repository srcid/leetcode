from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        M, N = map(len, (matrix, matrix[0]))

        for i in range(M):
            print(list(matrix[j][i] for j in reversed(range(N))))

            matrix.append(list(matrix[j][i] for j in reversed(range(N))))

        for i in range(M):
            matrix.pop(0)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)
