# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:32:22 2024

@author: USER
"""
# Problem Description
# Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.

# Problem Constraints
# 1 <= |A| <= 106
# -109 <= Ai <= 109

# Input Format
# First and only argument is an integer array A.

# Output Format
# Return 1 if any such integer p is found else return -1.

# Example Input
# Input 1:
  A = [3, 2, 1, 3]
  solve(A)
# Input 2:
  A = [1, 1, 3, 3]
  solve(A)
# Example Output
# Output 1:
#  1
# Output 2:
#  -1
# Example Explanation
# Explanation 1:

#  For integer 2, there are 2 greater elements in the array. So, return 1.
# Explanation 2:

#  There is no such integer exists.


# class Solution:
# 	# @param A : list of integers
# 	# @return an integer
# 	def solve(self, A):

def solve(A):
    ix = 0
    n_A = len(A)
    count_A = [0] * (n_A + 1)
    for ix in range(n_A):
        if A[ix] < 0:
            continue
        if A[ix] > n_A:
            count_A[n_A] += 1
            # print('here', ix)
        else:
            count_A[A[ix]] += 1
            # print('there', ix)
    # print('this', count_A, n_A)
    temp = count_A[n_A]    
    # print(temp)
    for i in range(n_A - 1, -1, -1):
        # print(temp, i, count_A[i])
        if (temp == i and count_A[i]) > 0:
            return 1
        elif temp > i:
            return -1  
        # print('this', temp, i, count_A[i])
        temp += count_A[i]
        # print('that', temp)
    return -1
        

    # Editoral:
        # Python

# class Solution:
# 	# @param A : list of integers
# 	# @return an integer
# 	def solve(self, A):
# 	    A.sort()
# 	    n = len(A)
# 	    for i in range(n-1):
# 	        if A[i] == A[i+1]:
# 	            continue
# 	        
# 	        if A[i] == n-i-1:
# 	            return 1
# 	    
# 	    if A[n-1] == 0:
# 	        return 1
# 	        
# 	    return -1

    # c++
# int Solution::solve(vector<int> &A) {
# 	sort(A.begin(), A.end()) ;
# 	int size = A.size();
# 	for(int i=0;i<size;i++){
# 		while(i+1<size && A[i]==A[i+1])
# 			i++;
# 		if(A[i]==size-1-i)
# 			return 1;
# 	}
# 	return -1;
# }

    # Scala
# class Solution {
#     def solve(A: Array[Int]): Int  = {
#         val n = A.length
#         val map:Map[Int, Int] = A.sorted.zipWithIndex.toMap
#         A.find(el => el == n - map.getOrElse(el, 0) -1) match {
#             case Some(_) => 1
#             case _ => -1
#         }
#     }
# }

    # GO
# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer
#  */
# import "sort"

# func solve(A []int )  (int) {
#     sort.Ints(A)

    
#     for i:=0;i<len(A);i++ {
#         if A[i] == 0 && i == len(A)-1 {
#             return 1
#         }
        
#         if A[i] == len(A)-i-1 && i != len(A)-1 && A[i] != A[i+1]{
#             return 1
#         }
#     }
#     return -1