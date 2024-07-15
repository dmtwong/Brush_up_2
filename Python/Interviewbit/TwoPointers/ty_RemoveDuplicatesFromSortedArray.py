# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:50:34 2024

@author: USER
"""

# Problem Description
# Given a sorted array A consisting of duplicate elements.
# Your task is to remove all the duplicates and return the length of the sorted array of distinct elements consisting of all distinct elements present in A.
# Note: You need to update the elements of array A by removing all the duplicates

# Problem Constraints
# 1 <= |A| <= 106
# 1 <= Ai <= 2 * 109

# Input Format
# First and only argurment containing the integer array A.

# Output Format
# Return a single integer, as per the problem given.

# Example Input
# Input 1:
A = [1, 1, 2]
# Input 2:
A = [1, 2, 2, 3, 3]
removeDuplicates(A)
# Example Output
# Output 1:
# 2
# Output 2:
# 3
# Example Explanation
# Explanation 1:
# Updated Array: [1, 2, X] after rearranging. Note that there could be any number in place of x since we dont need it.
# We return 2 here.
# Explanation 2:
# Updated Array: [1, 2, 3, X, X] after rearranging duplicates of 2 and 3.
# We return 3 from here.

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def removeDuplicates(self, A):

# temp = OrderedDict()    
# temp[1] = 1
# temp[1] += 1
# temp[2] = 1
# temp[3] = 1
# temp[3] += 1
# temp
# temp.values()
# ix_list = []
# val_list = list(temp.values())
# key_list = list(temp.keys())
# key_list
# for i in range(len(val_list)):
#     if val_list[i] > 1:
#         ix_list.append(i)
# ix_list

# def removeDuplicates(A):
#     from collections import OrderedDict
#     od_A = OrderedDict()    
#     n_A = len(A)    
#     if n_A == 0:
#         return A
#     else:
#         cur_A = A[0]
#         od_A[cur_A] = 1
#     for i in A[1:]:
#         if i == cur_A:
#             od_A[cur_A] += 1
#         else:
#             cur_A = i
#             od_A[i] = 1          
    
#     val_list = list(od_A.values())
#     key_list = list(od_A.keys())
#     # print('a', val_list)
#     # print('a', key_list)
#     key_dup = []
#     val_dup = []
#     for i in range(len(val_list)):
#         cur_val = val_list[i]
#         if cur_val > 1:
#             val_dup.append(cur_val)
#             key_dup.append(key_list[i])
#     # print(val_dup)
#     # print(key_dup)
#     for i in range(len(val_dup)):
#         cur_dup = val_dup[i]
#         cur_key = key_dup[i]
#         while cur_dup > 1:
#             # print(A)
#             ix_cur = A.index(cur_key)
#             A.pop(ix_cur)
#             cur_dup -= 1
#     return len(A)
def removeDuplicates(A):
    n = len(A)
    if n == 0 or n == 1:
        return n
    j = 0
    for i in range(n - 1):
        if A[i] != A[i + 1]:
            A[j] = A[i]
            j += 1
    A[j] = A[n - 1]
    return j + 1
    
# # Editorial:
# int Solution::removeDuplicates(vector<int> &A) {
#     assert(A.size() >= 1 && A.size() <= 1e6);
#     int count = 0, n = A.size();
# 	for (int i = 0; i < n; i++) { 
# 	    assert(A[i] >= 0 && A[i] <= 2e9);
# 		if (i < n - 1 && A[i] == A[i+1]) continue;
# 		else {
# 			A[count] = A[i];
# 			count++;
# 		}
# 	}
# 	return count;
# }    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    