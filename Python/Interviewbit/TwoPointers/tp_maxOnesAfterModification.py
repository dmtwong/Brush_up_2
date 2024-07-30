# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:37:05 2024

@author: USER
"""

# Problem Description
# Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.
# Problem Constraints
#  1 <= N, B <= 105
#  A[i]=0 or A[i]=1

# Input Format
# First argument is an binary array A.
# Second argument is an integer B.

# Output Format
# Return a single integer denoting the length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.

# Example Input
# Input 1:
 A = [1, 0, 0, 1, 1, 0, 1]
  B = 1
  
solve(A, B)

# Input 2:
 A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
 B = 2

# Example Output
# Output 1:
#  4
# Output 2:
#  5
# Example Explanation
# Explanation 1:

#  Here, we should only change 1 zero(0). Maximum possible length we can get is by changing the 3rd zero in the array,
#  we get a[] = {1, 0, 0, 1, 1, 1, 1}
# Explanation 2:

#  Here, we can change only 2 zeros. Maximum possible length we can get is by changing the 3rd and 4th (or) 4th and 5th zeros.

def solve(A, B):
    n_A = len(A)
    cnt = 0
    ix = 0
    result = 0
    
    for i in range(n_A):
        if A[i] == 0:
            cnt += 1        
        while cnt > B:
            if A[ix] == 0:
                cnt -= 1
            ix += 1 
        temp = i - ix + 1
        if temp > result:
            result = temp
            
    return result

# # Editorial
# def longestSubSeg(a, n, k): 
  
#     cnt0 = 0
#     l = 0
#     max_len = 0; 
  
#     # i decides current ending point 
#     for i in range(0, n): 
#         if a[i] == 0: 
#             cnt0 += 1
  
#         # If there are more 0's move 
#         # left point for current 
#         # ending point. 
#         while (cnt0 > k): 
#             if a[l] == 0: 
#                 cnt0 -= 1
#             l += 1
          
  
#         max_len = max(max_len, i - l + 1); 
      
  
#     return max_len 
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         return longestSubSeg(A,len(A),B)

# int longestSubSeg(vector<int>& a, int n, int k) 
# { 
#     int cnt0 = 0; 
#     int l = 0; 
#     int max_len = 0; 
  
#     // i decides current ending point 
#     for (int i = 0; i < n; i++) { 
#         if (a[i] == 0) 
#             cnt0++; 
  
#         // If there are more 0's move 
#         // left point for current ending 
#         // point. 
#         while (cnt0 > k) { 
#             if (a[l] == 0) 
#                 cnt0--; 
#             l++; 
#         } 
  
#         max_len = max(max_len, i - l + 1); 
#     } 
  
#     return max_len; 
# } 
  
# int Solution::solve(vector<int> &A, int B) {
#     return longestSubSeg(A,A.size(),B);
# }


# class Solution {
#     def solve(A: Array[Int], B: Int): Int  = {
    
#         val arr = A
#         val maxUpdates = B
    
#         var currUpdates = 0
#         var start = 0
#         var end = 0
    
#         while(currUpdates < maxUpdates && end < arr.size) {
#           if(arr(end) == 0) currUpdates = currUpdates + 1
#           end = end + 1
#         }
    
#         while(end < arr.size && arr(end) == 1) end = end + 1
    
#         if(end == arr.size) return arr.size
    
#         var currSize = (end - 1) - start + 1
#         var maxSize = currSize
    
#         while(end < arr.size) {
    
#           arr(start) match {
#             case 0 => {
#               start = start + 1
#             }
#             case 1 => {
#               while(start < arr.size && arr(start) == 1) start = start + 1
#               start = start + 1
#             }
#           }
    
#           var counter = 0
#           while(end < arr.size && (counter < 1 || arr(end) == 1)) {
#             if(arr(end) == 0) counter = counter + 1
#             end = end + 1
#           }
    
#           if(end == arr.size) return Math.max(maxSize, (end - 1) - start + 1)
    
#           currSize = (end-1) - start + 1
#           maxSize = Math.max(currSize, maxSize)
#         }
    
#         maxSize
#     }
# }


# func solve(A []int , B int )  (int) {
#     maxLen,l,count:=0,0,0
#     for i:=0;i<len(A);i++{
#         if A[i]==0{
#             count++
#         }
#         for count > B{
#             if A[l]==0{
#                 count--
#             }
#             l+=1
#         }
#         currLen := i-l+1
#         if currLen > maxLen{
#             maxLen = currLen
#         }
#     }
#     return maxLen
# }
