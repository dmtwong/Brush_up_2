# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:07:33 2024

@author: USER
"""

# Problem Description

# Write a function that takes an integer and returns the number of 1 bits it has.

# Problem Constraints
# 0 <= A <= 4294967295

# Input Format
# First and only argument contains integer A

# Output Format
# Return an integer as the answer

# Example Input
# Input1:
    # 11
# Example Output
# Output1:
# 3

# Example Explanation
# Explaination1:
# 11 is represented as 1101 in binary 

# class Solution:
#     # @param A : integer
#     # @return an integer
#     def numSetBits(self, A):
    # 11%2  +=1 
    # 5%2  += 1
    # 2%2 
    # 1%2 +=1 
    
def numSetBits(A):
    ans = 0
    while A > 0:
        if A % 2 == 1:
            ans += 1
        A //= 2
    return ans
A = 11
numSetBits(A)
A = 4294967295
A = 0

# # #     # Editoral:
# # #         # Python 
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def numSetBits(self, A):
#         ret = 0
#         while A != 0:
#             if A&1:
#                 ret += 1
#             A = A >> 1
#         return ret
# C++
# int Solution::numSetBits(unsigned int A) {
#     assert(A >= 0 && A <= UINT_MAX );
#     unsigned int total_ones = 0;
#     while (A != 0) {
#         A = A & (A-1);
#         total_ones++;
#     }
#     return total_ones;
# }