from typing import List, Optional


class Solution:
    # i - j range of rows
    # p - q range of cols
    def rotate(
        self,
        matrix: List[List[int]],
        i: Optional[int] = None,
        j: Optional[int] = None,
        p: Optional[int] = None,
        q: Optional[int] = None,
    ) -> None:
        i = i or 0
        j = j or len(matrix)
        p = p or 0
        q = q or len(matrix[0])

        if j - i == q - p == 1:
            return

        if j - i == q - p == 2:
            # fmt: off
            matrix[i][p], matrix[i][p + 1], matrix[i + 1][p], matrix[i + 1][p + 1] = (
                matrix[i + 1][  p  ],
                matrix[  i  ][  p  ],
                matrix[i + 1][p + 1],
                matrix[  i  ][p + 1],
            )
            # fmt: on
            return

        self.rotate(matrix, i + 1, j - 1, p + 1, q - 1)

        left_col = [matrix[k][p] for k in reversed(range(i, j))]
        right_col = [matrix[k][q - 1] for k in reversed(range(i, j))]

        # setting left col values
        for k, e in zip(range(i, j), matrix[j - 1][p:q]):
            print(k, e)
            matrix[k][p] = e

        # setting right col values
        for k, e in zip(range(i, j), matrix[i][p:q]):
            matrix[k][q - 1] = e

        matrix[i][p:q] = left_col
        matrix[j - 1][p:q] = right_col

        """
        matrix[i] <- left_col
        matrix[j-1] <- right_col
        right_col <- matrix[i]
        left_col <- matrix[j-1]
        """


if __name__ == "__main__":
    # fmt: off
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [5,   1,  9, 11],
        [2,   4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16]
    ]
    matrix3 = [
        [1,   2,  3,  4,  5],
        [6,   7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    res3 = [
        [21, 16, 11,  6, 1],
        [22, 17, 12,  7, 2],
        [23, 18, 13,  8, 3],
        [24, 19, 14,  9, 4], 
        [25, 20, 15, 10, 5]
    ]
    # fmt: on
    s = Solution()
    s.rotate(matrix3)
    print(str(matrix3).replace("],", "],\n"))
