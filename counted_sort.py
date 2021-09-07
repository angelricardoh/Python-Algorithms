#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def count_sort(arr):
    
    max_element = -1
    for array in arr:
        if int(array[0]) > max_element:
            max_element = int(array[0])
            
    # sorted_lists = [[]] * (max_element + 1)
    sorted_lists = [[] for i in range(max_element + 1)]

    mid = int(len(arr) / 2)
    for i in range(0, mid):
        sorted_lists[int(arr[i][0])].append('-')
        
    for i in range(mid, len(arr)):
        sorted_lists[int(arr[i][0])].append(arr[i][1])
    
    for list in sorted_lists:
        for element in list:
            print(element, end=" ")
    return sorted_lists

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    count_sort(arr)
