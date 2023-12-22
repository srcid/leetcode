def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contagem da frequência de ocorrência de cada dígito
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Cálculo das posições corretas dos dígitos no array de saída
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Ordenação dos elementos com base nos dígitos
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia os elementos ordenados de volta para o array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1

    # Iteração pelos dígitos, chamando o counting_sort para cada dígito
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

# Exemplo de uso:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)

arr = [124,202,97,33,99,2,100]
sorted_arr = radix_sort(arr)
print(sorted_arr)
