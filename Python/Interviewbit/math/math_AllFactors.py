# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:47:12 2024

@author: USER
"""

# Problem Description 
# Given a number A, find all factors of A.

# Problem Constraints
# 1 <= A <= 109

# Input Format
# The first argument is an integer A.

# Output Format
# Return an array of all factors of A.
# Example Input
A = 6
A = 1
A = 2
A = 3
A = 263086834 # Exceed Time
allFactors(A)
# Example Output
# [1, 2, 3, 6]
# Example Explanation
# For the given A = 6, its factors are 1, 2, 3, and 6, hence returning an array of them

# class Solution:
# 	# @param A : integer
# 	# @return a list of integers
# 	def allFactors(self, A):

def allFactors(A):
    from math import sqrt
    n_A = int(sqrt(A)) + 1
    result = [1]
    if A < 2:
        return result
    # for i in range(2, A//2+1):
    for i in range(2, n_A):
        if (A % i) == 0:
            temp = A // i 
            if i not in result:
                result.append(i)
            if temp not in result:
                result.append(A//i)
    result.sort()
    if A not in result:
        result.append(A)
    return result

# # Editorial:
#     # divmod(13, 2)
#     import math

# class Solution:
# 	# @param A : integer
# 	# @return a list of integers
# 	def allFactors(self, A):
# 	    factors = []
# 	    factors2 = []
# 	    # brute force
# 	    for x in range(1, int(math.sqrt(A))+1):
# 	        d, m = divmod(A, x)
# 	        if m == 0:
# 	            factors.append(x)   # sorted
# 	            if d != x:
# 	               factors2.append(d) # reverse sort
# 	               
# 	    factors2.reverse()
# 	    return factors + factors2

# vector<int> Solution::allFactors(int A) {
     
#     vector<int> v;
    
#     for(int i=1;i*i<=A;i++) if(A%i==0) {if(i*i!=A){v.push_back(i);v.push_back(A/i);}else{v.push_back(i);}}
#     sort(v.begin(),v.end());
#     return v;
# }

# class Solution {
#     def allFactors(A: Int): Array[Int]  = {
#     ((for (i <- 2 to Math.sqrt(A).toInt if A % i == 0) yield (i, A / i)).toList.flatMap(p => List(p._1, p._2)).toSet ++ Set(1, A)).toArray.sorted
#     }
# }
#  import "sort"
# func allFactors(A int) []int {
#     var factors []int
#     for i := 1; i*i <= A; i++ {
#         if A%i == 0 {
#             factors = append(factors, i)
#             if i*i != A {
#                 factors = append(factors, A/i)
#             }
#         }
#     }

#     sort.Ints(factors)
#     return factors

# }