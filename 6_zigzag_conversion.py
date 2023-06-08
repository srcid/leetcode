def convert(s: str, numRows: int) -> str:
    n = numRows
    m = len(s)
    k = 2*n - 2 # number of elements in a block
    res = ""

    if (n==1):
        return s
    elif (n==2):
        return s[0:m:2] + s[1:m:2]
    elif (n==3):
        return s[0:m:4] + s[1:m:2] + s[2:m:4]

    for i in range(n):
        first_idx = i

        while first_idx < m:
            res += s[first_idx]

            if i != 0 and i != n-1:
                chars_in_between = k - 2*i
                second_idx = first_idx + chars_in_between

                if second_idx < m:
                    res += s[second_idx]

            first_idx += k

    return res

print(convert("PAYPALISHIRING", 4))