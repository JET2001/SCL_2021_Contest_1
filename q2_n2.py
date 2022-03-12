import math
import itertools
import collections
import sys
from bisect import bisect as upper_bound ## for bisection algorithms
import operator
import heapq
import functools
import decimal
import fractions
import random
import queue
import typing
### Declare any constants
POS_INF = float('inf')
NEG_INF = float('-inf')
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

### Declare any type aliases here
Queue = queue.Queue
Stack = queue.LifoQueue

#### UTILITY FUNCTIONS
### Creating a Matrix in Python
def create_matrix(rows, cols, default_val = 0):
    """
    Creates a matrix filled with default_val
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(default_val)

    return M
def create_adjacency_list(num_of_nodes):
    """
    Initialises an adjacency list
    """
    adj_list = list()
    i = 0
    while (i < num_of_nodes):
        adj_list.append(list())
        i += 1
    return adj_list
## =========== DEFINE ANY USER DEFINED CLASSES HERE ===============

#[1,3,4] k = 3
#=>[-2,0,1]
#=>(-2),(0),(1),(-2,0),(0,1),(-2,0,1)
#=>(1) ,(3),(4),(1 ,3),(3,4),(1 ,3,4)
#=>      *   *           *
## 1 3 4

#two pointer: O(n^2)
[-2, 0, 1, 3, 4, 5]

#### ========== MAIN IMPLEMENTATION ===========
### O(n^2) time | O(1) space
def question2(n: int, k: int, values: list):
    ### Parse input
    values = [x-k for x in values]
    shoffee = 0
    if values[-1] >= 0: shoffee += 1
    for i in range(n-1):
        sum = values[i]
        if sum >= 0:
            shoffee += 1
            # print("Shoffee:", values[i])
        for j in range(i+1,n):
            sum += values[j]
            if sum >= 0:
                # print("Shoffee:", values[i:j+1])
                shoffee += 1
    return shoffee

## Elusive O(n log n) attempt
# def question2_v2(n: int, k:int, values: list):
#     values = [x-k for x in values]
#     shoffee = 0
#     ## Calculate the prefix sum of the subarray
#     prefix = [0] * n
#     prefix[0] = values[0]
#     ## Loop to find the prefix sum
#     for i in range(1,n):
#         prefix[i] = values[i] + prefix[i-1]
#         if (prefix[i] >= 0): shoffee +=1

#     if (prefix[0] >= 0): shoffee +=1

#     ## sort prefix sum array
#     prefix = sorted(prefix)

#     ## Loop to find upperbound for each element
#     for i in range(n):
#         shoffee += n - upper_bound(prefix, prefix[i])

#     return shoffee




### Read first line of input
n, k = map(int, sys.stdin.readline().split()) ### template for input with test case
### INPUT HERE
##### First line of test case
values = list(map(int, sys.stdin.readline().split()))
### PRINT OUTPUT
output = question2(n, k, values) ## EDIT PARAMS
print(output)
