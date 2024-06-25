# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:32:23 2024

@author: USER
"""

# Problem Description

# Given an array of integers A, sort the array into a wave-like array and return it. 
# In other words, arrange the elements into a sequence such that

# a1 >= a2 <= a3 >= a4 <= a5..... 
# NOTE: If multiple answers are possible, return the lexicographically smallest one.
# roblem Constraints
# 1 <= len(A) <= 106
# 1 <= A[i] <= 106

# Input Format
# The first argument is an integer array A.

# Output Format
# Return an array arranged in the sequence as described.

# Example Input
# Input 1:
A = [1, 2, 3, 4]
A = [1, 2, 3, 4, 1]
A = [1, 2, 3, 4, 5]
A = [1, 2, 3, 4, 4]
wave(A)
# Input 2:
A = [1, 2]
# Example Output
# Output 1:
# [2, 1, 4, 3]
# Output 2:
# [2, 1]

# Example Explanation
# Explanation 1:

# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
# First answer is lexicographically smallest. So, return [2, 1, 4, 3].
# Explanation 1:

# Only possible answer is [2, 1].

# class Solution:
# 	# @param A : list of integers
# 	# @return a list of integers
# 	def wave(self, A):
def wave(A):
    n_A = len(A)
    A.sort()
    ix = 1
    for i in range(ix, n_A, 2):
        A[i-1], A[i] = A[i], A[i-1]
    # if n_A % 2 == 1:
        # if A[n_A]
    return A

# EDitorial:
#     class Solution:
# 	# @param A : list of integers
# 	# @return a list of integers
# 	def wave(self, A):
# 	    # For the answer to be the lexicographically smallest,
# 	    # we want the first element to be the second smallest,
# 	    # the 2nd element to be the smallest, and so on with
# 	    # the rest of the sequence.
# 	    A = sorted(A)
# 	    for i in range(0, len(A)-1, 2):
# 	        A[i], A[i+1] = A[i+1], A[i]
# 	    return A
# vector<int> Solution::wave(vector<int> &A) {
#     sort(A.begin(), A.end());
#     for(int i=0; i<A.size()-1; i+=2) swap(A[i], A[i+1]);
#     return A;
# }

# class Solution {
#     def wave(A: Array[Int]): Array[Int]  = {
#         val sorted = A.sorted
#         for (i <- 1 until sorted.length by 2) {
#             val tmp = sorted(i - 1)
#             sorted(i - 1) = sorted(i)
#             sorted(i) = tmp
#         }
#         sorted
#     }
# }
#  import "sort"
# func wave(A []int )  ([]int) {
#     if len(A)== 1{
#         return A
#     }
    
#     sort.Ints(A)
#     for i:=1;i<len(A); i+=2 {
#         A[i-1], A[i] = A[i], A[i-1]    
#     }
#     return A
# }
