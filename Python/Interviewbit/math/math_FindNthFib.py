# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:00:54 2024

@author: USER
"""

# Problem Description

# Given an integer A you need to find the Ath fibonacci number modulo 109 + 7.

# The first fibonacci number F1 = 1

# The first fibonacci number F2 = 1

# The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)

# Problem Constraints
# 1 <= A <= 109.



# Input Format
# First argument is an integer A.



# Output Format
# Return a single integer denoting Ath fibonacci number modulo 109 + 7.

# Example Input
# Input 1:

#  A = 4
# Input 2:

#  A = 3


def solve(A):
    if A < 0:
        return - 1
    if A == 0 or A == 1:
        return A
    # else:
    #     return solve(A-1) + solve(A-2)
    def fub_generator():
        lag_2 = 0 # start with 0 as n - 2
        lag_1 = 1 # as n - 1  
        while True:
            next = lag_2 + lag_1 
            yield next
            lag_2 = lag_1
            lag_1 = next
    count = 0
    for n in fub_generator():
        count += 1 
        if count == A-1:
            return n%(10**9 + 7)
        
    
solve(0)
solve(5)
solve(6)
solve(50)
solve(10)
solve(999)
solve(99999)
solve(1000000000) #  Time Limit Exceeded.


# ####################
# # Below are editorial solution: 
    
# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# # function that returns nth
# # Fibonacci number


# def fib(n):
#     F = [[1, 1], [1, 0]]
#     if n == 0:
#         return 0
#     power(F, n - 1)
#     return F[0][0]

# def multiply(f, m):
#     mod = 1000000007

#     a = (f[0][0] * m[0][0] % mod + f[0][1] * m[1][0] % mod) % mod
#     b = (f[0][0] * m[0][1] % mod + f[0][1] * m[1][1] % mod) % mod
#     c = (f[1][0] * m[0][0] % mod + f[1][1] * m[1][0] % mod) % mod
#     d = (f[1][0] * m[0][1] % mod + f[1][1] * m[1][1] % mod) % mod
#     f[0][0] = a
#     f[0][1] = b
#     f[1][0] = c
#     f[1][1] = d

# # Optimized version of
# # power() in method 4
# def power(F, n):
#     if n == 0 or n == 1:
#         return
#     M = [[1, 1], [1, 0]]
#     power(F, n // 2)
#     multiply(F, F)
#     if n % 2 != 0:
#         multiply(F, M)

# class Solution:

#     # @param A : integer
#     # @return an integer

#     def solve(self, A):
#         return fib(A)