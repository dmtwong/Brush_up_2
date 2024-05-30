# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:30:18 2024

@author: USER
"""
# Problem Description

# Given a number A. Find the fatorial of the number.

# Problem Constraints
# 1 <= A <= 100

# Input Format
# First and only argument is the integer A.

# Output Format
# Return a string, the factorial of A.

# Example Input
# Input 1:

# A = 2
# Input 2:

# A = 3
# Example Output
# Output 1:
#  2
# Output 2:
#  6

# Example Explanation
# Explanation 1:

# 2! = 2 .
# Explanation 2:
# 3! = 6 .

# class Solution:
#     # @param A : integer
#     # @return a strings
#     def solve(self, A):
def solve(A):
    def helper_gen():
        lag_1 = 1 # start as fib(n-1)
        n = 1
        while True:
            next = n * lag_1 
            # print("at n = %d, fib(n-1) = %d, fib(n) = %d " %(n-1, lag_1, next))
            yield next
            n += 1
            lag_1 = next                  
    count = 0
    for n in helper_gen():
        count += 1 
        if count == A:
            return str(n)
solve(2)
solve(3)
solve(100)
