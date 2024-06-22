# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:33:25 2024

@author: USER
"""

# Given an array, find the next greater element G[i] for every element A[i] in the array.  The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 

# More formally,

# G[i] for an element A[i] = an element A[j] such that 
#     j is minimum possible AND 
#     j > i AND
#     A[j] > A[i]
# Elements for which no greater element exist, consider next greater element as -1.

# Example:

# Input : 
    A =  [4, 5, 2, 10]
nextGreater(A)
# Output : [5, 10, 10, -1]

# Example 2:

 A = [3, 2, 1]

# Output : [-1, -1, -1]

# class Solution:
# 	# @param A : list of integers
# 	# @return a list of integers
# 	def nextGreater(self, A):
def nextGreater(A):
    # import sys
    # from collections import deque
    # deque_A= deque()
    # n_Amin1 = len(A) - 1
    # cur_max = -sys.maxsize - 1
    # result = []
    # for i in range(n_Amin1, -1, -1):
    #     cur_i = A[i]
    #     if cur_max < cur_i:
    #         cur_max = cur_i
    #     deque_A.append(cur_max)
    # for j in range(n_Amin1):
    #     if A
    n_A = len(A)
    result = A[:]
    for i in range(n_A - 1):
        # leng = 1
        cur_i = A[i]
        # isChange = False
        for j in range(i + 1, n_A) :
            cur_j = A[j]
            print(i, j, cur_i, cur_j)
            if cur_i < cur_j:
                result[i] = cur_j
                isChange = True
                break
            result[i] = -1
        # if isChange == False:
    result[n_A - 1] = -1    
    return result
        
                