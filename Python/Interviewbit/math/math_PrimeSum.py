# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:46:04 2024

@author: USER
"""

# Problem Description 

# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.
# If there is more than one solution possible, return the lexicographically smaller solution i.e.
# If [a, b] is one solution with a <= b,
# and [c,d] is another solution with c <= d, then

# [a, b] < [c, d] 
# If a < c OR ( a == c AND b < d ).
# NOTE: A solution will always exist. read Goldbach's conjecture

# Problem Constraints
# 1 <= A <= 2 * 107

# Input Format
# The first argument is an integer A.

# Output Format
# Return an array of integers.

# Example Input
# 4

# Example Output[2, 2]

# Example Explanation
# 2 + 2 equals 4, which is the lexicographically smaller solution

# class Solution:
# 	# @param A : integer
# 	# @return a list of integers
# 	def primesum(self, A):

def primesum(A):
    mid = A // 2
    result = [0, 0]
    def check_prime(curr_num):
        if (curr_num == 2 or curr_num == 3):
            return True
        mid = curr_num // 2
        for div in range(2, mid + 2):
            if(curr_num % div == 0):
                return False
        return True
    for i in range(2, mid + 2):
        curr_1 = i
        curr_2 = A - i
        if ((check_prime(curr_1) == True) and (check_prime(curr_2) == True)):
            result = [curr_1, curr_2]
            return result
                    
        
    return result 

# Testing cases:
for i in range(4, 8):
    print(primesum(i))
        
primesum(378)


##############################
# Editoral:
    # Python
# import math

# class Solution:
#     def primesum(self, n: int) -> 'List[int]':
#         is_prime = [True] * (n + 1)
#         is_prime[0], is_prime[1] = False, False

#         for i in range(2, int(math.sqrt(n)) + 1):
#             if is_prime[i]:
#                 for j in range(i * 2, n + 1, i):
#                     is_prime[j] = False

#         for i in range(2, n):
#             if is_prime[i] and is_prime[n - i]:
#                 return [i, n - i]

#         return []

    # Scala
# class Solution {
#     def primesum(A: Int): Array[Int]  = {  
#       def sieve(n: Int): Array[Boolean] = {
#         val arr = Array.fill[Boolean](n + 1)(true)
#         arr(0) = false
#         arr(1) = false
#         var i = 2
#         while (i * i <= n) {
#           if (arr(i)) {
#             for (j <- i * 2 to n by i) arr(j) = false
#           }
#           i = i + 1
#         }
#         arr
#       }
    
#       val arr = sieve(A)
#       for (i <- 0 until A) {
#         if (arr(i) && arr(A - i)) return Array(i, A - i)
#       }
#       Array()
#     }
# }

    # c++ 
# vector<int> Solution::primesum(int A) {
#     int n=A;
#     int i,j;
    
#     vector<bool>v(n+1, true);
#     v[0] = false;
#     v[1] = false;
    
#     vector<int>m(2,0);
    
#     for(i=2;i<=n;i++)
#     {
#         if (i > n/i) {
#             break;
#         }
#         if(v[i])
#         {
#             //m.push_back(i);
#             for(j=i*i;j<=n;j+=i)
#             {
#                 v[j]=false;
#             }
#         }
#     }
    
#     for (i = 2; i <= A/2; ++i) {
#         if (v[i] && v[A-i]) {
#             m[0] = i;
#             m[1] = A-i;
#             return m;
#         }
#     }
    
#     return m;
# }