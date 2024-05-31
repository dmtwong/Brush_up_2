# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:37:20 2024

# @author: USER
# """

# Problem Description

# Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

# NOTE: You should make minimum number of comparisons.

# Problem Constraints
# 1 <= N <= 105
# -109 <= A[i] <= 109
# Input Format
# First and only argument is an integer array A of size N.

# Output Format
# Return an integer denoting the sum Maximum and Minimum element in the given array.

# Example Input
# Input 1:

A1 = [-2, 1, -4, 5, 3]
# Input 2:

A2 = [1, 3, 4, 1]
# Example Output
# Output 1:
#  1
# Output 2:
#  5

# Example Explanation
# Explanation 1:
#  Maximum Element is 5 and Minimum element is -4. (5 + (-4)) = 1. 
# Explanation 2:
#  Maximum Element is 4 and Minimum element is 1. (4 + 1) = 5.

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
        

def solve(A):
    min_A = A[0]
    max_A = min_A 
    
    n_A = len(A)
    
    if n_A == 1:
        return(min_A + max_A)
    
    for i in range(1, n_A):
        temp = A[i]
        small = temp < min_A
        large = temp > max_A
        if not small and not large:
            continue
        elif temp < min_A:
            min_A = temp
        elif temp > max_A:
            max_A = temp
    
    return min_A + max_A

solve(A1)
solve(A2)

##############################
# Editoral:
    # Python
    
# def getMinMax(low, high, A): 
#     arr_max = A[low] 
#     arr_min = A[low] 
      
#     # If there is only one element  
#     if low == high: 
#         arr_max = A[low] 
#         arr_min = A[low] 
#         return (arr_max, arr_min) 
          
#     # If there is only two element 
#     elif high == low + 1: 
#         if A[low] > A[high]: 
#             arr_max = A[low] 
#             arr_min = A[high] 
#         else: 
#             arr_max = A[high] 
#             arr_min = A[low] 
#         return (arr_max, arr_min) 
#     else: 
          
#         # If there are more than 2 elements 
#         mid = int((low + high) / 2) 
#         arr_max1, arr_min1 = getMinMax(low, mid, A) 
#         arr_max2, arr_min2 = getMinMax(mid + 1, high, A) 
  
#     return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         maxi, mini  = getMinMax(0, len(A) -1, A)
#         ans = maxi + mini
#         return ans

    # C++
# //Using the approach of divide and conquer.
# pair<int,int> findMinMax(vector<int> &A, int start, int end){
#     if(start == end)
#         return make_pair(A[start], A[start]);

#     int mid = (end-start)/2 + start;
#     //Find Min and Max pair for left sub-array
#     pair<int,int> mm1 = findMinMax(A,start,mid);
#     //Find Min and Max pair for right sub-array
#     pair<int,int> mm2 = findMinMax(A,mid+1,end);

#     //Compare the value to get the max and min for the entire array.
#     int minNum = mm1.first < mm2.first ? mm1.first : mm2.first;
#     int maxNum = mm1.second > mm2.second ? mm1.second : mm2.second;

#     //Return max and min values as a pair.
#     return make_pair(minNum,maxNum);
# }

# int Solution::solve(vector<int> &A) {
#     pair<int,int> minMax = findMinMax(A,0,A.size()-1);
#     return minMax.first + minMax.second;
# }

    # scala

# class Solution {
#     def solve(arr: Array[Int]): Int  = {
#             val l = arr.toList
#     val head = l.head
#     val (min, max) = l.tail.foldLeft((head, head))((pair, e) => {
#       if ( e < pair._1) (e, pair._2)
#       else if (e > pair._2) (pair._1, e)
#       else pair
#     })
    
#     min + max
#     }
# }

    # GO

# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer
#  */
# func solve(A []int)int{
#     max:=0
#     min:=0
#     for i,_:=range A{
#         if(A[i]>max){
#             max=A[i]}
#         }    
#     min=max
            
#     for i,_:=range A{
#         if(A[i]<min){
#         min=A[i]}
#     }    
#     return max+min    
# }
