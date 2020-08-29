import math
import os
import random
import re
import sys


def isValid(s):
    freq = dict()

    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    freq_set = set(freq.values())
    if len(freq_set) == 1:
        return "YES"
    elif len(freq_set) == 2:
        elems = list(freq_set)
        count_freq = dict()
        count_freq[elems[0]] = 0
        count_freq[elems[1]] = 0
        for c in freq:
            count_freq[freq[c]] += 1
        larger_elem = max(elems)
        smaller_elem = min(elems)
        if count_freq[larger_elem] == 1 and larger_elem - smaller_elem == 1:
            return "YES"
        elif 1 in count_freq and count_freq[1] == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':

    s = input()

    print(isValid(s))
