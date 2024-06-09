# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:14:34 2024

@author: USER
"""

# Problem Description
# Given an array A of N non-negative numbers and you are also given non-negative number B.
# You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow.

# Problem Constraints
# 1 <= N <= 104
# 1 <= A[i] <= 100
# 1 <= B <= 108

# Input Format
# First argument is an integer array A.

# Second argument is an integer B.

# Output Format
# Return an integer denoting the number of subarrays in A having sum less than B.

# Example Input
# Input 1:
#  A = [2, 5, 6]
#  B = 10
# Input 2:
#  A = [1, 11, 2, 3, 15]
#  B = 10

# Example Output
# Output 1:
#  4
#  Output 2:
#  4
# Example Explanation
# Explanation 1:
#  The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
# Explanation 2:
#  The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
def solve(A, B):
    n_A = len(A)
    ans = 0
    for i in range(n_A):
        cur_sum = 0
        j = i  
        while j <= n_A - 1:
            cur_val = A[j]
            if cur_sum + cur_val < B:
                cur_sum += cur_val
                ans += 1
                j += 1
            else:
                j = n_A
    return ans

# #     # Editoral:
# #         # Python 
# Function to find number of subarrays  
# having sum less than k. 
# def countSubarray(arr, n, k): 
#     count = 0
  
#     for i in range(0, n): 
#         sum = 0; 
#         for j in range(i, n): 
              
#             # If sum is less than k 
#             # then update sum and  
#             # increment count 
#             if (sum + arr[j] < k): 
#                 sum = arr[j] + sum
#                 count+= 1
#             else: 
#                 break
#     return count; 
  
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         return countSubarray(A,len(A),B)
    
#     # Scala:
# class Solution {
#     def solve(A: Array[Int], B: Int): Int  = {
        
#         val arr = A
#         val maxSum = B
        
#         var start = 0
#         var end = 0
        
#         var numSubArrays = 0
#         var currSum = arr(0)
        
#         while(start < arr.size && end < arr.size) {
            
#             if(currSum < maxSum) {
#                 end = end + 1
#                 if(end >= start) numSubArrays = numSubArrays + end - start
#                 if (end < arr.size) currSum = currSum + arr(end)
#             } else {
#                 currSum = currSum - arr(start)
#                 start = start + 1
#             }
#         }
        
#         numSubArrays
#     }
# }
                
# # C++
# int Solution::solve(vector<int> &A, int B) {
#     int n=A.size(),count=0,sum=0,j=0;

#     for(int i=0;i<n;i++)
#     {
#         sum+=A[i];
#         while(sum>=B)
#         {
#             sum-=A[j];
#             j++;
#         }
#         count+=i-j+1;
#     }
#     return count;
# }

# GO:
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
#  import "fmt"
#  const debug = false
# func solve(A []int , B int )  (int) {
#     currentSum, left, right, counts := 0, 0, 0, 0
#     for left <= right && right < len(A) {
#         if currentSum + A[right] < B { 
#             counts+= (right-left)+1
#             currentSum += A[right]
#             right++
#         } else {
#             if debug {fmt.Println(left, right, currentSum, counts)}
#             if left == right {
#                 left++
#                 right++
#                 currentSum = 0
#                 continue
#             }
            
#             currentSum -= A[left]
#             left++
#         }
#     }    
#     return counts
# }