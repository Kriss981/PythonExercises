#!/usr/bin/env python3
"""
Data Structures and Algorithms for CL 3, Assignment 6
See <https://https://dsacl3-2022.github.io/a6/> for detailed instructions.
Author:      Pun Ching Nei
Honor Code:  I pledge that this program represents my work.
I received help from: no one in designing and debugging my program.
"""
import random


def cyclic_hash(s, shift=5, size=32, start=0x877218c4430b9321):
    """ Calcualte a hash for a given string with cyclic-shift.

    Parameters
    ----
    s       The string to be hashed
    shift   The amount of shift
    size    The size of the returned hash in bits
    start   Initial constant for hashing (helps producing independent
            hash functions with the same amount of shift)
    """
    h = 0
    mask = (1 << size) - 1
    print(mask)

    for character in s:
        h ^= ord(character)
        h = (h << shift & mask) | (h >> (size - shift))
    # print(h)
    return h


class BloomFilter:
    def __init__(self, filter_size=70000):
        """ The object that holds the bloom filter.

        Parameters
        ----
        filter_size  The size of the filter. You need to adjust this for
                     successful tests. Note that the size (in bits) should
                     not be larger than the space needed storing a set of
                     hash codes for the words in our lexicon.txt.
        """
        # Initialize the Bloom filter. Note that we can normally use a
        # bit array, but for the sake of exercise we are using a list
        # of Booleans.
        self.bfilter = [False] * filter_size
        h0 = lambda x: cyclic_hash(x, shift=5)
        h1 = lambda x: cyclic_hash(x, shift=4)
        h2 = lambda x: cyclic_hash(x, shift=3)
        h3 = lambda x: cyclic_hash(x, shift=2)
        self.my_hashes = [h0, h1, h2, h3]


    def add(self, s):
        """ Add s to the Bloom filter.

        Add the string 's' to the filter, return True if 's' was
        already in the filter, False otherwise.
        """
        flag = True
        for i in self.my_hashes:
            temp = i(s) % len(self.bfilter)
            if not self.bfilter[temp]:
                self.bfilter[temp] = True
                flag = False
        return flag


if __name__ == "__main__":
    # Example use
    words_dup = open('lexicon-dup.txt', 'rt').read().strip().split()
    nodups = []
    bf = BloomFilter()
    for w in sorted(words_dup):
        if not bf.add(w):
            nodups.append(w)
