# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:10:42 2024

@author: USER
"""

# Problem Description
 
# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
# TIP: C users, please malloc the result into a new array and return the result.

# If the number of elements initialized in A and B is m and n respectively, the resulting size of array A after your code is executed should be m + n
# Problem Constraints
# 1 <= |A|, |B| <= 105

# Input Format
# The first argument is an integer array A.
# The second argument is an integer array B.

# Output Format
# Update the array A.

# Example Input
# A : [1 5 8]
# B : [6 9]

# Example Output
# Modified A : [1 5 6 8 9]

# class Solution:
# 	# @param A : list of integers
# 	# @param B : list of integers
# 	def merge(self, A, B):
    
def merge(A, B):
    n_A, n_b = len(A), len(B)
    # n_T = n_A + n_B
    A.extend(B)
    A.sort()

# #     # Editoral:
# # # Python:
    
# class Solution:
#     # @param A : list of integers
#     # @param B : list of integers
#     def merge(self, A, B):
#         i=0
#         j=0
#         l=[]
#         while(i<len(A) and j<len(B)):
#             if(A[i]>B[j]):
#                 A.insert(i,B[j])
#                 j+=1
#             else:
#                 i+=1
#         while(j<len(B)):
#             A.append(B[j])
#             j+=1

# void Solution::merge(vector<int> &A, vector<int> &B) {
#     int m = A.size();
#     int n = B.size();
#     int temp[m+n+2];
#     int indexA = 0, indexB = 0;
#     for (int i = 0; i < m+n; i++){
#         if (indexB == n || (indexA < m && A[indexA] < B[indexB])) {
#             temp[i] = A[indexA];
#             indexA++;
#         } else {
#             temp[i] = B[indexB];
#             indexB++;
#         }
#     }
#     A.resize(m + n);
#     for (int i = 0; i < m+n; i++) {
#         A[i] = temp[i];
#     }
#     return;
# }
            
            