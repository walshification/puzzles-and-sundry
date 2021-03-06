#!/usr/bin/env python3

"""
Given an integer n, write a function to count all possible sequences of
length n such that all the elements of the sequence are in the range
[1 to n] and the sum of the elements of the sequence is even.

Example:
countEvenSequences(3)
> 13
// All possible sequences of length 3 will be (1, 1, 2), (1, 3, 2),
// (3, 1, 2), (3, 3, 2), (1, 2, 1), (1, 2, 3), (3, 2, 1), (3, 2, 3),
// (2, 1, 1), (2, 1, 3), (2, 3, 1), (2, 3, 3) and (2, 2, 2).

The answer can get large, so be efficient with this one!
"""

import argparse
import sys


def count_even_sequences(n: int) -> int:
    """Returns a count of all possible sequences for a given integer n,
    such that all the elements of the sequence are in the range
    [1 to n] and the sum of the elements of the sequence is even.
    """
    total_sequences = n ** n
    # half the incremental sequences will be even
    evens = total_sequences / 2
    # rounded down in the case of odd numbered sequence totals
    return int(evens)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()

    count = count_even_sequences(args.n)
    print(count)
    sys.exit()
