# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:56:24 2024

@author: USER
"""

# Given an integer array A of length N. Where Ai is the cost of stepping on the ith stair.
# From ith stair, you can go to i+1th or i+2th numbered stair.
# Initially, you are at 1st stair find the minimum cost to reach Nth stair.

# Input Format
# The first and only argument is an integer array A.


# Output Format
# Return an integer.

# class Solution:
    # @param A : list of integers
    # @return an integer
    # def solve(self, A):

# def solve(A):
#     # result = A[0]
#     len_A = len(A)    
#     if len_A == 1: 
#         return A[0] # result
#     elif len_A == 2:
#         return A[1] + A[0]
#     result_step_1 = solve(A[:len_A-1]) # + A[len_A-1]
#     # print(result_step_1)
#     result_step_2 = solve(A[:len_A-2]) # + A[len_A-1]
#     # result_step_2 = 999
#     # print(result_step_2, A[len_A-1])    
#     print(A, result_step_1, result_step_2)
#     return min(result_step_1, result_step_2) + A[len_A-1]

# counter = 0
def solve(A):
    # global counter
    # counter += 1
    # print(counter)
    copy_A = A[:]
    copy_A[1] += copy_A[0]
    # print(A, copy_A)
    for i in range(2, len(copy_A)):
        copy_A[i] += min(copy_A[i-1], copy_A[i-2])
    return copy_A[-1]
A_1 = [1, 2, 1, 3]
A_2 = [1, 2, 3, 4]
A_3 = [2, 76, 46]
solve(A_1)
solve(A_2)
solve(A_3)