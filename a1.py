#!/usr/bin/env python3
""" Data Structures and Algorithms for CL 3, Assignment 1
    See <https://https://dsacl3-2022.github.io/a1/> for detailed
    instructions.
    Course:      Data Structures and Algorithms for Computational Linguistics 3 WS22/23
    Author:      Pun Ching Nei, Cheng Yin-yin
    Honor Code:  I pledge that this program represents my teams' work.
    I received help from: no one in designing and debugging my program.
"""


def find_rotation(seq, start=None, end=None):
    """
    Given a previously sorted array which has been rotated, so that the n smallest values have been shifted to the end, find
    the index of the value where the rotation has occurred (e.g, the sequence [3, 4, 5, 0, 1, 2] should return 3). Do this
    by means of a binary search.

    If the sequence is correctly sorted, return -1

    You may assume the sequence does not contain duplicates.

    Parameters
    ____
    seq: The array to be searched
    start: first index of the interval being searched
    end: last index of the interval being searched
    """

    seq_copy = seq[:]
    seq_copy.sort()
    if seq == seq_copy or len(seq) == 1:
        return -1
    else:
        if start is None:
            start = 0
        if end is None:
            end = len(seq)
        if start > end:
            return None
        mid = (start + end) // 2
        if seq[mid] < seq[mid - 1]:
            return mid
        if seq[mid] > seq[0]:
            return find_rotation(seq, start=mid + 1)
        else:
            return find_rotation(seq, start, end=mid - 1)

def ternary_search(seq, val, start=None, end=None):
    """
    A function that performs a recursive ternary search on a sorted sequenceand returns the index of the searched value.
     A ternary search follows the same principle as a binary search, but instead of dividing the sequence in two, it
    does so in three.

    If the value is not found, return -1

    You may assume the sequence does not contain duplicates

    Parameters
    ____
    seq: The sequence to be searched
    val: the value to be searched for
    start: first index of the interval being searched
    end: last index of the interval being searched
    """
    if start is None:
        start = 0
    if end is None:
        end = len(seq)
    if start == end:
        return 0
    else:
        mid1 = end // 3
        mid2 = mid1 + end // 3

        if seq[mid1] == val:
            return mid1
        if seq[mid2] == val:
            return mid2
        if seq[mid1] > val:
            return ternary_search(seq, val, start, seq[mid1] - 1)
        if seq[mid2] < val:
            return ternary_search(seq, val, seq[mid2] + 1, end)
        if seq[mid1] < val < seq[mid2]:
            return ternary_search(seq, val, seq[mid1] + 1, seq[mid2] - 1)
        else:
            return -1


# You may use this space for testing your code and trying things out. It will not be corrected.
if __name__ == '__main__':
    seq = [100, 900, 901, 903, 906, 1010, 50, 55, 59, 60, 89, 90, 92, 97]
    # print(len(seq))
    print(find_rotation(seq))
    # print(ternary_search(seq, 0))
