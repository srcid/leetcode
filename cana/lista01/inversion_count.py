# 5. Seja A[1,...,n] um vetor com n números distintos. Dizemos que um par (i, j) é
# uma inversão de A se i < j e A[i] > A[j]. Escreva um algoritmo com complexidade
# O(n log n) qe calcula o número de inversões de A.


def inversion_count_naive(A):
    n = len(A)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                ans += 1

    return ans


def merge(A, i, k, j):
    p, q = i, k
    a = []

    cnt = 0

    while p < k and q < j:
        if A[p] < A[q]:
            a.append(A[p])
            p += 1
        else:
            a.append(A[q])
            q += 1
            cnt += k - p

    if p == k:  # left sub array is empty
        a.extend(A[q:j])
    else:  # q == j, right sub array is empty
        a.extend(A[p:k])

    A[i:j] = a

    return cnt


def merge_sort(A, i, j):
    if i < 0 or j < 0 or (j - i) < 0:  # Invalid range
        raise IndexError("Invalid range")

    if (j - i) == 0:  # Empty array
        return 0

    if (j - i) == 1:  # Single element array
        return 0

    k = i + (j - i) // 2

    cnt_l = merge_sort(A, i, k)
    cnt_r = merge_sort(A, k, j)

    cnt = merge(A, i, k, j)

    return cnt + cnt_l + cnt_r


def inversion_count(A):
    return merge_sort(A, 0, len(A))


if __name__ == "__main__":
    m = int(input())

    for _ in range(m):
        n = int(input())
        a = list(map(int, input().split(" ")))
        ans = inversion_count(a)
        print(ans)
