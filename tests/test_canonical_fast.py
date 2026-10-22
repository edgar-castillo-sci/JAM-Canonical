"""Tests for canonical_key_fast (optimal computation of κ, Theorem 3.17)."""

import itertools

import numpy as np
import pytest

from canonjam import canonical_key, canonical_key_fast


def rows_for_option(option):
    """Single-layer rows for each option (mirror of validacion.rows_for_option)."""
    if option == 1:
        return [['+0', '+j', '+j']]
    if option == 2:
        return [['+0', '+j', '+k']]
    if option == 3:
        return [['+0', '+j', '-j']]
    if option == 4:
        return [['+0', '+j', '-k'], ['+0', '-j', '+k']]
    if option == 5:
        return [['+0', '*j', '(+k-k)']]
    if option == 6:
        return [['*j', '+k', '-k']]
    if option == 7:
        return [['+0', '*j', '(+k-l)'], ['+0', '*j', '(-k+l)']]
    if option == 8:
        return [['*j', '+k', '-l'], ['*j', '-k', '+l']]
    raise ValueError(f"Invalid option: {option}")


def all_chains(n, option):
    rows = rows_for_option(option)
    for combo in itertools.product(rows, repeat=n):
        yield np.array(combo, dtype=object)


@pytest.mark.parametrize("option", range(1, 9))
def test_canonical_key_fast_matches_literal(option):
    """Theorem 3.17: canonical_key_fast agrees with canonical_key."""
    for n in [2, 3]:
        for a in all_chains(n, option):
            fast = canonical_key_fast(a, option)
            literal = canonical_key(a, option)
            assert fast == literal, (
                f"Mismatch: option={option}, n={n}, "
                f"chain={a.tolist()}, fast={fast!r}, literal={literal!r}"
            )
