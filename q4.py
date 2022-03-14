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
####
#     A[0]      A[1]                  A[2]              A[3]
# k=0 INF     --->
# k=1 A[0] sum(0..1)*(1-0+1) sum(0..2)*(2-0+1) sum(0..3) * (3-0+1)
# k=2 INF  A[1][0] + A[1][1]   min(A[2][1] + A[2]*1,
# ####
# For each person, determine if the person should be in his own group or join the old group
# -- Index of new person
# -- Number of partitions left

# Recursive solution
## Memoize the solution


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
###
# all_groups = dict()

## =========== DEFINE ANY USER DEFINED CLASSES HERE ===============
# def q4_helper(currIdx: int, n: int, num_groups_left: int):







def noise(arr, idx1, idx2):
    return sum(arr[idx1:idx2+1])*(idx2-idx1+1)


#### ========== MAIN IMPLEMENTATION ===========
all_groups = dict()     #(starting, groups): minimum noise level for swes[starting:] splitting into group groups
## currGroup --> the index of the first member of the current group
## groups --> number of groups left
def question4(swes: list, currIdx: int, currGroup: int, groups: int):    #minimum noise value for list[starting:] splitting into groups groups
    print("currIdx = {} | currGroup = {} | Groups_Left: {}".format(currIdx, currGroup, groups))
    if groups == 1: return noise(swes, currGroup, len(swes)-1)
    elif groups > 1 and currIdx == len(swes)-1: return POS_INF ## not allowed
    elif groups == len(swes)-1-currGroup: return sum(swes[currIdx:]) ## the number of people left == the number of groups left
    ## everyone remaining will be in 1 group
    elif (currGroup, groups) in all_groups:
        print("Result cached!")
        return all_groups[(currGroup, groups)]   ## Decide to add to current groups # the key - is a tuple. The value is the minimum noise level when there are group groups left.
    else:
        #Noise after adding an engineer to a new group
        ## Conclude the group with the previously considered engineer (currIdx -1) and calculate the noise factor.
        ## Create a new group with the current engineer (currIdx)
        ## Recursive call to the new group to see if the remaining number of groups is 1 or the number of remaining
        ## engineers.
        min_noise = 0
        option1 = noise(swes, currGroup, currIdx-1) + question4(swes, currIdx+1, currIdx, groups-1)
        ## Noise after he adds an engineer to a current group
        option2 = question4(swes, currIdx+1, currGroup, groups)
        min_noise = min(option1, option2)
        all_groups[(currGroup, groups)] = min_noise

        return min_noise



### Read first line of input
n, k = map(int, sys.stdin.readline().split())
### INPUT HERE
##### Noise level of each engineer
engineers = [int(num) for num in sys.stdin.readline().split()]

## =================================================
### PRINT OUTPUT
output = question4(engineers, 0, 0, k) ## EDIT PARAMS
print(output)
