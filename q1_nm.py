import math
import itertools
import collections
import sys
import bisect ## for bisection algorithms
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






def get_max(trees: list, direction: int):
    summ = 0
    max_sum_so_far = 0
    if direction == 0:
        for i in range(len(trees)):
            summ += trees[i]
            max_sum_so_far = summ if max_sum_so_far < summ else max_sum_so_far
    else:
        i = len(trees)-1
        while(i >= 0):
            summ += trees[i]
            max_sum_so_far = summ if max_sum_so_far < summ else max_sum_so_far
            i -=1
    return max_sum_so_far
# dp(n, ending on left/right)
# 3 options:
# 1. stay at the same side: dp(n,left) = dp(n-1,left) + 0
# 2. moving k cells and moving back: dp(n,left)=dp(n-1,left)+ maximum_you_can_get form traversing from left for day n --> O(m)
# 3. moving across: dp(n,left) = dp(n-1,right)+total score for the day

# dp(n,left) = max(dp(n-1,left), dp(n-1,left)+ maximum_you_can_get form traversing from left for day n, dp(n-1,right)+total score for the day)
#dp[days][] = dp[day][left],dp[day][right]
#### ========== MAIN IMPLEMENTATION ===========
def question1(n: int, m: int, trees):
    ### Parse input
    maxscore = create_matrix(n,2)

    maxscore[0][0] = max(0, get_max(trees[0],0))
    maxscore[0][1] = sum(trees[0])
    for i in range(1,n):
        sum_for_day = sum(trees[i])
        maxscore[i][0] = max(maxscore[i-1][0] + get_max(trees[i],0), maxscore[i-1][1] + sum_for_day)
        maxscore[i][1] = max(maxscore[i-1][1] + get_max(trees[i],1), maxscore[i-1][0] + sum_for_day)

    return max(maxscore[n-1])

### Read first line of input
num_test_cases = int(sys.stdin.readline()) ### template for input with test cases
for i in range(num_test_cases):
    ### INPUT HERE
    ##### First line of test case
    num_days , num_trees  = map(int,sys.stdin.readline().split())
    trees = []
    for day in range(num_days):
        trees.append(list(map(int, sys.stdin.readline().split())))
    print(trees)
    ### PRINT OUTPUT
    output = question1(num_days, num_trees, trees) ## EDIT PARAMS
    print(output)
