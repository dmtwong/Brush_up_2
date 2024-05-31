# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:33:40 2024

@author: USER
"""

# Following code tries to figure out if a number is prime ( Wiki )

# However, it has a bug in it.

# Please correct the bug and then submit the code.

# class Solution:
#     # @param A : integer
#     # @return an integer
#     def isPrime(self, A):
# 	upperLimit = int(A**0.5)
# 	for i in xrange(2, upperLimit + 1):
# 		if i < A and A % i == 0:
# 			return 0
# 	return 1

def isPrime(A):
    if A <= 1: 
        return 0
    erLimit = int(A**0.5)
    for i in range(2, erLimit + 1):
        if i < A and A % i == 0:
            return 0
    return 1
isPrime(1)
isPrime(13)
isPrime(19)
isPrime(20)

##############################
# Editoral:
    # Python
    
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def isPrime(self, A):
#         if A <= 1:
#             return 0
# 	upperLimit = int(A**0.5)
# 	for i in xrange(2, upperLimit + 1):
# 		if i < A and A % i == 0:
# 			return 0
# 	return 1

    # c++
# // Return 1 if A is prime, else 0
# int Solution::isPrime(int A) {
#     if(A == 1) return 0;
# 	int upperLimit = (int)(sqrt(A));
# 	while(upperLimit*upperLimit<= A)
# 	    upperLimit++;
# 	for (int i = 2; i <= upperLimit; i++) {
# 		if (i < A && A % i == 0) return 0;
# 	}
# 	return 1;
# }
