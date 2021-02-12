# Author: Santigie Sankoh

import math
import os
import random
import re
import sys
import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closest_nums(arr):
    q_lst = []
    arr = sorted(arr)
    minimumVal = 10 ** 9
    for i in range(1, len(arr)):
        diffVal = abs(arr[i - 1] - arr[i])
        if diffVal < minimumVal:
            q_lst = [(arr[i - 1], arr[i])]
            minimumVal = diffVal

        elif diffVal == minimumVal:
            q_lst.append((arr[i - 1], arr[i]))

    Lst = [i for sublist in q_lst for i in sublist]
    return Lst


if __name__ == '__main__':
    Tiw = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input( ))

    arr = list(map(int, input( ).rstrip( ).split( )))

    exp_result = closest_nums(arr)

    Tiw.write(' '.join(map(str, exp_result)))
    Tiw.write('\n')

    Tiw.close( )
