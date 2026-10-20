"""
pipeline.py

Generate all canonical classes for n layers of a given JAM option,
using canonJAM for filtering at every step.

This script replicates the generation logic of x.jam, but replaces
its pairwise filter with filter_duplicates from canonJAM.

It does not require xjam2. It only requires canonJAM and numpy.

Usage:
    python3 pipeline.py --options 1 --levels 2 3 4 5 6
"""

import argparse
import numpy as np
from itertools import permutations

from canonjam import filter_duplicates


def rows_for_option(option):
    """Return the possible single layers for the given JAM option."""
    if option == 1:
        tokens = ['+0', '+j', '+j']
    elif option == 2:
        tokens = ['+0', '+j', '+k']
    elif option == 3:
        tokens = ['+0', '+j', '-j']
    elif option == 4:
        a = ['+0', '+j', '-k']
        b = ['+0', '-j', '+k']
        rows = list(set(permutations(a, 3))) + list(set(permutations(b, 3)))
        return [list(r) for r in rows]
    elif option == 5:
        tokens = ['+0', '*j', '(+k-k)']
    elif option == 6:
        tokens = ['*j', '+k', '-k']
    elif option == 7:
        a = ['+0', '*j', '(+k-l)']
        b = ['+0', '*j', '(-k+l)']
        rows = list(set(permutations(a, 3))) + list(set(permutations(b, 3)))
        return [list(r) for r in rows]
    elif option == 8:
        a = ['*j', '+k', '-l']
        b = ['*j', '-k', '+l']
        rows = list(set(permutations(a, 3))) + list(set(permutations(b, 3)))
        return [list(r) for r in rows]
    else:
        raise ValueError(f"Invalid option: {option}")

    return [list(r) for r in set(permutations(tokens, 3))]


def generate_unique(n, option):
    """
    Generate the canonical classes of n layers using canonJAM
    for filtering at every step.
    """
    single = [np.array(r) for r in rows_for_option(option)]
    uniques = single.copy()

    for level in range(2, n + 1):
        if level == 2:
            candidates = [
                np.vstack([a, b]) for a in uniques for b in single
            ]
        else:
            down = [np.vstack([a, b]) for a in uniques for b in single]
            up = [np.vstack([b, a]) for a in uniques for b in single]
            candidates = down + up

        uniques = filter_duplicates(candidates, option)

    return uniques


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Generate canonical classes for JAM options using "
            "canonJAM for filtering."
        ),
    )
    parser.add_argument(
        "--options",
        type=int,
        nargs="+",
        default=[1],
        help="JAM options to process (default: 1)",
    )
    parser.add_argument(
        "--levels",
        type=int,
        nargs="+",
        default=[2, 3, 4, 5],
        help="Layer counts to process (default: 2 3 4 5)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    for option in args.options:
        print(f"Option {option}:")
        for n in args.levels:
            uniques = generate_unique(n, option)
            print(f"  n={n}: {len(uniques)} classes")
        print()
