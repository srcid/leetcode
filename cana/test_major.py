import pytest
from major import major, major_dp, major_linear, major_prob

cases = [
    # Majoritário à esquerda
    ([1, 1, 1, 2], 1),
    # Metade um elemento não majoritário com três valores
    ([1, 3, 2, 2], None),
    # Majoritário com o mínimo necessário
    ([1, 2, 3, 1, 3, 4, 1, 1, 1, 4, 5, 1, 1], 1),
    # Elemento majoritário simples
    ([1, 1, 1, 2, 3], 1),
    # Nenhum majoritário
    ([1, 2, 3, 4], None),
    # Majoritário exatamente na metade (inválido)
    ([1, 1, 2, 2], None),
    # Elemento único
    ([5], 5),
    # Dois elementos, um majoritário
    ([9, 9], 9),
    # Três elementos, dois iguais
    ([3, 3, 2], 3),
    # Majoritário no final
    ([4, 2, 2, 2, 2], 2),
    # Majoritário no começo
    ([7, 7, 7, 3, 4], 7),
    # Todos iguais
    ([8, 8, 8, 8], 8),
    # Majoritário espalhado
    ([1, 2, 1, 3, 1, 4, 1], 1),
    # Lista vazia
    ([], None),
    # Números negativos
    ([-1, -1, -1, 2], -1),
    # Zero como majoritário
    ([0, 0, 0, 1, 2], 0),
    # Intercalado com empate
    ([1, 2, 1, 2], None),
    # Longa com majoritário
    ([9] * 51 + [1] * 49, 9),
    # Longa sem majoritário
    ([1] * 50 + [2] * 50, None),
    # Majoritário no meio
    ([3, 4, 3, 3, 3, 5], 3),
    # Flutuação mas majoritário prevalece
    ([7, 8, 7, 8, 7, 7, 7], 7),
    # Majoritário após ruído inicial
    ([5, 6, 6, 6, 6, 6], 6),
    # Alternando com maioria clara
    ([1, 2, 1, 2, 1, 1, 1], 1),
]


# @pytest.mark.skip(reason="I want it not to run.")
@pytest.mark.parametrize("arr, expected", cases)
def test_major(arr, expected):
    assert major(arr) == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_major_prob(arr, expected):
    assert major_prob(arr) == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_major_linear(arr, expected):
    assert major_linear(arr) == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_major_dp(arr, expected):
    assert major_dp(arr) == expected
