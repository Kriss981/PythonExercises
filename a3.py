#!/usr/bin/env python3
""" Data Structures and Algorithms for CL 3, Assignment 3
    See <https://https://dsacl3-2022.github.io/a2/> for detailed
    instructions.
    Author:      Pun Ching Nei
    Honor Code:  I pledge that this program represents my work.
    I received help from: no one in designing and debugging my program.
"""


def find_k_highest(seq, k):
    """
    Using ideas from the quick sort algorithm and without sorting the input, find the kth highest element in an unsorted
    list.  For example, [3, 4, 2, 9, 8, 0] with k = 2 should return 8.

    If there is no k highest element, return None

    Parameters
    ____
    seq: the sequence being searched
    k: the rank being searched for
    """

    pivot = seq.pop()

    item_lower = []
    item_higher = []
    for x in seq:
        if x <= pivot and x not in item_lower:
            item_lower.append(x)
        if x > pivot and x not in item_higher:
            item_higher.append(x)
    total_length = len(item_lower) + len(item_higher) + 1

    if k > total_length:
        return None
    elif k == len(item_higher) + 1:
        # print(pivot)
        return pivot
    elif k <= len(item_higher):
        return find_k_highest(item_higher, k)
    else:
        temp_k = k - (len(item_higher) + 1)
        return find_k_highest(item_lower, temp_k)


# You may use this space to test your code:
if __name__ == "__main__":
    find_k_highest([5, 4, 2, 10, 7, 23, 9, 3, 6], 4)
