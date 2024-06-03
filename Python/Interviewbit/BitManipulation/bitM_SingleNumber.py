# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:06:41 2024

@author: USER
"""

# Problem Description 

# Given an array of integers A, every element appears twice except for one. Find that single one.
# NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Problem Constraints
# 1 <= |A| <= 2000000
# 0 <= A[i] <= INTMAX

# Input Format
# First and only argument of input contains an integer array A.

# Output Format
# Return a single integer denoting the single element.

# Example Input
# Input 1:
  A = [1, 2, 2, 3, 1]
singleNumber(A)
# Input 2:
  A = [1, 2, 2]

# Example Output
# Output 1:
#  3
# Output 2:
#  1

# Example Explanation
# Explanation 1:

# 3 occurs once.
# Explanation 2:

# 1 occurs once.

# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def singleNumber(self, A):
def singleNumber(A):
    result = 0
    n_A = len(A)
    for i in range(n_A):
        # print(i, A[i], result)
        result = result ^ A[i]
        # print(result)
    return result


# #     # Editoral:
# #         # Python 
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def singleNumber(self, A):
#         from scipy import stats
#     print(stats.bernoulli.rvs(size=10,p=0.3))

#     # C++
# int Solution::singleNumber(const vector<int> &A) {
    
#        int n = A.size();
#        int result = 0;
#        for (int i = 0; i < n; i++) {
# 	       result ^= A[i];
#        }
#        return result;
    
# }

#     # Scala:
#     class Solution {
#     def singleNumber(A: Array[Int]): Int  = {
#         var res = 0
#         A.foreach(ai => res = res ^ ai)
#         res
#     }
# }

#     # GO
# /**
#  * @input A : Integer array
#  *
#  * @Output Integer
#  */
# func singleNumber(numbers []int) (int) {
# 	number := 0
# 	for i := 0; i < len(numbers); i++ {
# 		number ^= numbers[i]
# 	}
# 	
# 	return number
# }