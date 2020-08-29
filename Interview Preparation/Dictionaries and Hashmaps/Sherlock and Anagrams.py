#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    letters = list(s)
    anagram_count = 0

    for comb_length in range(1, len(s) + 1):
        dict_subs = {}
        substring_map = ["".join(sorted(letters[j:j + comb_length])) for j in range(0, len(s) + 1 - comb_length)]
        for subs in substring_map:
            if dict_subs.__contains__(subs):
                dict_subs[subs] += 1
            else:
                dict_subs[subs] = 1
        for keys in dict_subs:
            anagram_count += dict_subs[keys]*(dict_subs[keys] - 1)/2
            anagram_count = int(anagram_count)
    return anagram_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
