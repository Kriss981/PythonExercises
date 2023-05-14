#!/usr/bin/env python3
""" Data Structures and Algorithms for CL 3, Assignment 2
    See <https://https://dsacl3-2022.github.io/a2/> for detailed
    instructions.
    Author: Pun Ching Nei
    Honor Code:  I pledge that this program represents my work.
    I received help from: no one in designing and debugging my program.
"""

import numpy as np


def palindrome_matrix(string):
    """
    Ex. 2.1

    Return an n x n matrix (2-dimensional numpy array) where n is the length of the input string.
    palindrome_matrix[i][j] is True iff the substring between indices i and j (both INCLUSIVE) is a palindrome, otherwise
    False.

    For example, given the string "aba", the function should return the following matrix:

    [[ True, False, True  ]
     [ False, True, False ]
     [ False, False, True ]]

    Parameters
    ____
    string: the input string
    """

    # Initialize matrix with all False
    length = len(string)

    palind_mtrx = np.array([[False for _ in range(length)] for _ in range(length)])
    for column in range(length):
        for row in range(length):
            if column >= row:
                temp = string[row:column + 1]
                if temp == temp[::-1]:
                    palind_mtrx[row][column] = True
    # print(palind_mtrx)
    return palind_mtrx


def min_seg(string, palind_mtrx=None, start=None, end=None, substr_to_min=None):
    """
    Ex. 2.2

    Given a string, return the minimum number of segmentations such that all resulting substrings are palindromes.
    For example, for the string "aab", the function should return 1.

    Use a dynamic programming approach.

    An implementation has been started for you.

    Parameters
    ____
    string: the input string that we want the minimum segmentations from.
    palind_mtrx: the palindrome matrix for the string as described in ex. 2.1.
    start: the first index of the substring being considered. Equivalent to i in palind_mtrx[i][j].
    end: the last index of the substring being considered. Equivalent to j in palind_mtrx[i][j].
    substr_to_min: a dictionary for the purposes of dynamic programming. A substring is mapped to its minimum
    segmentations
    """
    cordin = []
    if palind_mtrx is None:
        palind_mtrx = palindrome_matrix(string)

    if start is None:
        start = 0

    if end is None:
        end = len(string) - 1

    substr = string

    if substr_to_min is None:
        substr_to_min = {}  # a dict to keep record of the minimum splits required for a given substring

    # If the substring is not in the dictionary, add it. Else, just fetch it in constant time
    if substr not in substr_to_min.keys():
        if palind_mtrx[start][end]:
            substr_to_min[substr] = 0
            result = 0
        else:
            while end >= 0:
                for start in range(len(string)):
                    if palind_mtrx[start][end] and start != end:
                        x = start
                        y = end
                        cordin.append((x, y))
                end -= 1

            j = len(cordin)-1
            while j > 0:
                if cordin[0][0] < cordin[j][1]:
                    cordin.pop(j)
                    j -= 1
                else:
                    j -= 1

            for x in range(len(cordin)):
                result = len(string) - (cordin[x][1] - cordin[x][0] + 1)

        substr_to_min[substr] = result

    return substr_to_min[substr]


if __name__ == "__main__":
    # palindrome_matrix("anitalavalatina")
    # min_seg("anitalavalatina")
    pass
