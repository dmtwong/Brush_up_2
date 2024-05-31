# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:37:54 2024

@author: USER
"""

# Problem Description
# Given an integer array A of size N.
# You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.
# Find and return this maximum possible sum.
# NOTE: Suppose B = 4 and array A contains 10 elements then
# You can pick the first four elements or can pick the last four elements or can pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick.

# Problem Constraints
# 1 <= N <= 105
# 1 <= B <= N
# -103 <= A[i] <= 103

# Input Format
# First argument is an integer array A.
# Second argument is an integer B.

# Output Format
# Return an integer denoting the maximum possible sum of elements you picked.

# Example Input
# Input 1:
  # A = [5, -2, 3 , 1, 2]
  # B = 3
# Input 2:
  # A = [1, 2]
  # B = 1
# Example Output
# Output 1:
#   8
# Output 2:
#   2
# Example Explanation
# Explanation 1:

#   Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
# Explanation 2:

#   Pick element 2 from end as this is the maximum we can get

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
def solve(A, B):
    curr_prefix = sum(A[:B])
    curr_suffix = 0
    curr_max = curr_prefix
    for i in range(1, B+1):
        curr_prefix -= A[B-i]
        curr_suffix += A[-i] 
        # print(curr_max)
        curr_sum = curr_suffix + curr_suffix
        # print(curr_sum)
        if curr_sum > curr_max:
            curr_max = curr_sum
    return(curr_max)

    # Editoral:
        # Python
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         n = len(A)
#         suff = [0] * (n + 1)
#         suff[n - 1] = A[n - 1]
#         for i in range(n - 2, -1, -1):
#             suff[i] = A[i] + suff[i + 1]
#         prefSum = 0
#         ans = suff[n - B]
#         for i in range(B):
#             prefSum = prefSum + A[i]
#             suffSum = suff[n - B + i + 1]
#             ans = max(ans, prefSum + suffSum)
#         return ans

    # Scala
    # class Solution {
  # def solve(A: Array[Int], B: Int): Int  = {
#     val initialSum = A.take(B).sum
#     var maxSum = initialSum
#     var curSum = initialSum
#     for (i <- B - 1 to 0 by -1) {
#       curSum = curSum - A(i) + A(A.length - 1 - (B - 1 - i))
#       if (maxSum < curSum) maxSum = curSum
#     }

#     maxSum
#   }
# }
 # C++
#  int fun(vector < int > & A, int B) {
#   int n = A.size();
#   int suff[n + 1];
#   suff[n] = 0;
#   suff[n - 1] = A[n - 1];
#   for (int i = n - 2; i >= 0; i--)
#     suff[i] = A[i] + suff[i + 1];
#   int prefSum = 0;
#   int ans = suff[n - B];
#   for (int i = 0; i < B; i++) {
#     prefSum = prefSum + A[i];
#     int suffSum = suff[n - B + (i + 1)];
#     ans = max(ans, prefSum + suffSum);
#   }
#   return ans;
# }
# int Solution::solve(vector < int > & A, int B) {
#   return fun(A, B);
# }
# GO
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# import "math"
# func solve(A []int , B int )  (int) {
#     // Check if len of B is greater than A
#     left_sum := make([]int, B)
#     right_sum := make([]int, B)
    
#     sum := 0
#     for i:= 0; i<B; i++ {
#         sum += A[i]
#         left_sum[i] = sum
#     }
    
#     sum = 0
#     for i:=0; i<B; i++ {
#         sum += A[len(A) - 1 - i]
#         right_sum[B - 1 - i] = sum
#     }
    
#     max_sum := math.MinInt64
    
#     for i:= -1; i <B; i++ {
#         var left int
#         if i == -1 {
#             left = 0
#         } else {
#             left = left_sum[i]
#         }
#         var right int
#         if i + 1 == B {
#             right = 0
#         } else {
#             right = right_sum[i+1]
#         }
#         curr := left + right
#         if curr > max_sum {
#             max_sum = curr
#         }
#     }
#     return max_sum
# }