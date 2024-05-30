# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:36:50 2024

@author: USER
"""

# Problem Description
 
# Given a number A, find all prime numbers up to A (A included).
# Make sure the returned array is sorted.

# Problem Constraints
# 1 <= A <= 106

# Input Format
# The first argument is an integer A.

# Output Format
# Return array of integers.

# Example Input
# A = 7

# Example Output
# [2, 3, 5, 7]

# Example Explanation
# All primes till 7 are, 2, 3, 5 and 7


# class Solution:
# 	# @param A : integer
# 	# @return a list of integers
# 	def sieve(self, A):

        
def sieve(A):
    result = []
    def check_prime(curr_num, A):
        # print('inside helper', curr_num, A)
        if (curr_num == 2 or curr_num == 3):
            return True
        # mid = curr_num // 2
        for div in range(2, curr_num//2 + 1):
            # print('inside helper for loop', div)
            if(curr_num % div == 0):
                return False
        return True
    
    for i in range(2, A + 1):
        # print(i)
        if check_prime(i, A):            
            result.append(i)
    return result

# Testing cases:
# sieve(7)

for i in range(16):
    print(i, sieve(i))
    
sieve(100000) # Time Limit Exceeded.

##############################
# Editoral:
    # Python
    
class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        import math
        if A<2:
            return []
        result=[]
        for a in range(2,A+1):
            for i in range(2,int(math.sqrt(a))+1):
                if a%i==0:
                    break
            else:
                result.append (a)
        return result
            
    # Scala