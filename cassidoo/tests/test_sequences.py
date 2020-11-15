import pytest

from cassidoo.sequences import count_even_sequences


@pytest.mark.parametrize("n, answer", ((1, 0), (2, 2), (3, 13), (4, 128), (5, 1562)))
def test_returns_total_number_of_even_sequences(n, answer):
    count = count_even_sequences(n)
    assert count == answer
