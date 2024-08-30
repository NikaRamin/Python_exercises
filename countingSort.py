#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def countingSort(arr, n):
    if n == 0:
        return []
    max_val = max(arr)

    count = [0] * (max_val + 1)

    for i in range(n):
        count[arr[i]] += 1

    index = 0
    final = []
    for i in range(max_val + 1):
        while count[i] > 0:
            final.append(i)
            count[i] -= 1

    return final
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
