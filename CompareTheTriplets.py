import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    new_list = [0, 0]

    for i in range(len(a)):
        if (a[i] > b[i]):
            new_list[0] += 1
        elif (a[i] < b[i]):
            new_list[1] += 1
    return new_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
