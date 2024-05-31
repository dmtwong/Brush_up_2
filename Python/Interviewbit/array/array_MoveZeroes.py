# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:11:05 2024

@author: USER
"""

# Problem Description
 
# Given an integer array A, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Problem Constraints
# 1 <= |A| <= 105

# Input Format
# First argument is array of integers A.

# Output Format
# Return an array of integers which satisfies above property.

# Example Input
# Input 1:
A1 = [0, 1, 0, 3, 12]
# Input 2:
A2 = [0]

# Example Output
# Ouput 1:
# [1, 3, 12, 0, 0]
# Ouput 2:

# [0]

# Example Explanation
# Explanation 1:
# Shift all zeroes to the end.
# Explanation 2:

# There is only one zero so no need of shifting.

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):

A3 = [1, 6, 1, 0, 9, 6, 2, 5, 6, 2, 10, 2, 0, 6]
def solve(A):    
    n_A = len(A)
    ix = 0
    reach_end = n_A
    while reach_end != 0:
        # print(reach_end)
        if A[ix] == 0:
            A.append(0)
            del A[ix]
            reach_end -= 1
        else:
            ix += 1
            reach_end -= 1
    return A

    # for i in range(n_A):
    #     print(i,A[i], A)
    #     if A[i] == 0:
    #         A.append(0)
    #         del A[i]      
    # return A
    
    # n_A = len(A)
    # # print(id(A))
    # A.sort()
    # count_0 = A.count(0)
    # zero_tba = count_0
    # while (count_0 !=0 ):
    #     A.pop(A.index(0))
    #     count_0 -= 1
    # while (zero_tba != 0):
    #     A.append(0)
    #     zero_tba -= 1 
    # # print(id(A))
    # return A
    
A1 = [0, 1, 0, 3, 12]
A2 = [0]
A3 = [1, 6, 1, 0, 9, 6, 2, 5, 6, 2, 10, 2, 0, 6]
A4 = [0, 0, 9, 4, 0, 10, 3, 8, 6, 2, 6]

solve(A1)
solve(A2)
solve(A3)
solve(A4)


##############################
# Editoral:
    # Python
#     class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         count = []
#         li = []
#         for i in A:
#             if (i == 0):
#                 count.append(i)
#             else:
#                 li.append(i)
#         return li + count
    
#     # C++
# vector<int> Solution::solve(vector<int> &nums) {
#     int j = 0;
#     // move all the nonzero elements advance
#     for (int i = 0; i < nums.size(); i++) {
#         if (nums[i] != 0) {
#             nums[j++] = nums[i];
#         }
#     }
#     for (;j < nums.size(); j++) {
#         nums[j] = 0;
#     }
#     return nums;
# }

#     # Scala
    
#     class Solution {
#     def solve(A: Array[Int]): Array[Int]  = {

#         var b = A
#         var nonZeroCount = 0 

#         for (i <- 0 to b.size - 1){

#             if(b(i) != 0){
#                 var temp = b(i)
#                 b(i) = b(nonZeroCount)
#                 b(nonZeroCount) = temp
#                 nonZeroCount += 1
#             }
#         }

#         b 
#     }
# }
    
#     # GO 
# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer array.
#  */
# func solve(A []int )  ([]int) {
#     B:=make([]int,len(A))
#     j:=0
#     for i:=0;i<len(A);i++{
#         if A[i]!=0{
#             B[j]=A[i]
#             j++
#         }
#     }
#     return B
# }