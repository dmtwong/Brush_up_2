# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:33:38 2024

@author: USER
"""

# Given a sorted array of integers, find the number of occurrences of a given target value.

# Your algorithm’s runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return 0

# **Example : **

# Given [5, 7, 7, 8, 8, 10] and target value 8,
A = [5, 7, 7, 8, 8, 10]
A.index(8)
A.index(1)
A.rindex(8)
findCount(A, 8)
findCount(A, 1)
# return 2.

# PROBLEM APPROACH :

# For complete solution, look at the hint.

# class Solution:
# 	# @param A : tuple of integers
# 	# @param B : integer
# 	# @return an integer
# 	def findCount(self, A, B):
# 1,2,3,4,5,6,7 mid = 4
def findCount(A, B):
    n_A = len(A)
    # mid = (B - A) //2    
    try:
        first_ix = A.index(B)
    except:
        return 0
    # last_ix = A.rindex(B)
    count = 1
    for i in range(first_ix+1, n_A):
        if A[i] == B:
            count += 1
            continue
        else:
            return count
    return count
    

# # # # #     # Editoral:
# # # # # # Python:

# class Solution:
#     # @param A : tuple of integers
#     # @param B : integer
#     # @return an integer
#     def findCount(self, A, B):
#         n=len(A)
#         def bs1(A,low,high):
#             while(low<=high):
#                 mid1=(low+high)//2
#                 if A[mid1]==B:
#                     ans=mid1
#                     high=mid1-1
#                 elif A[mid1]>B:
#                     high=mid1-1
#                 else:
#                     low=mid1+1
#             return ans
#         def bs2(A,low,high):
#             while(low<=high):
#                 mid1=(low+high)//2
#                 if A[mid1]==B:
#                     ans1=mid1
#                     low=mid1+1
#                 elif A[mid1]>B:
#                     high=mid1-1
#                 else:
#                     low=mid1+1
#             return ans1
#         lo=0
#         hi=n-1
#         while(lo<=hi):
#             mid=(lo+hi)//2
#             if A[mid]==B:
#                 t=bs1(A,0,mid)
#                 t1=bs2(A,mid,n-1)
#                 return t1-t+1
                    
#             elif A[mid]>B:
#                 hi=mid-1
#             else:
#                 lo=mid+1
#         return 0
#         # if flag==1:
#         #     if ans==-1 and 

# C++
# int Solution::findCount(const vector<int> &A, int B) {
#     int st = lower_bound(A.begin(), A.end(), B)-A.begin();
#     int ed = upper_bound(A.begin(), A.end(), B)-A.begin();
#     return ed-st;
# }

# Scala:
# class Solution {
#     def findCount(A: Array[Int], B: Int): Int  = {
#         var (lo, hi) = (0, A.length-1)
#         while(lo <= hi){
#             val mid = (lo+hi)/2
#             if (A(mid) == B) hi = mid-1
#             else if (B < A(mid)) hi = mid-1
#             else lo = mid + 1
#         }
#         (lo until A.length).takeWhile(A(_) == B).length
#     }
# }
# GO:
#     /**
#  * @input A : Integer array
#  * @input B : Integer
#  *
#  * @Output Integer
#  */
# func findCount(numbers []int , number int) (int) {
# 	idx := binarySearch(numbers, number, 0, len(numbers) - 1)
# 	if idx == - 1 {
# 		return 0
# 	}
# 	
# 	i := idx - 1
# 	count := 1
# 	for i >= 0 && numbers[i] == number {
# 		count++
# 		i--
# 	}
# 	
# 	i = idx + 1
# 	for i < len(numbers) && numbers[i] == number {
# 		count++
# 		i++
# 	}
# 	return count
# }

# func binarySearch(numbers []int, number, left, right int) int {
# 	
# 	if left <= right {
# 		mid := left + ((right - left) / 2)
# 		if numbers[mid] == number {
# 			return mid
# 		} else if numbers[mid] > number {
# 			return binarySearch(numbers, number, left, mid - 1)
# 		} else {
# 			return binarySearch(numbers, number, mid + 1, right)
# 		}
# 	}
# 	
# 	return -1
# }