# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:56:24 2024

@author: USER
"""

# Given an integer array A of length N. Where Ai is the cost of stepping on the ith stair.
# From ith stair, you can go to i+1th or i+2th numbered stair.
# Initially, you are at 1st stair find the minimum cost to reach Nth stair.

# Input Format
# The first and only argument is an integer array A.


# Output Format
# Return an integer.

# class Solution:
    # @param A : list of integers
    # @return an integer
    # def solve(self, A):

# def solve(A):
#     # result = A[0]
#     len_A = len(A)    
#     if len_A == 1: 
#         return A[0] # result
#     elif len_A == 2:
#         return A[1] + A[0]
#     result_step_1 = solve(A[:len_A-1]) # + A[len_A-1]
#     # print(result_step_1)
#     result_step_2 = solve(A[:len_A-2]) # + A[len_A-1]
#     # result_step_2 = 999
#     # print(result_step_2, A[len_A-1])    
#     print(A, result_step_1, result_step_2)
#     return min(result_step_1, result_step_2) + A[len_A-1]

# counter = 0
def solve(A):
    # global counter
    # counter += 1
    # print(counter)
    copy_A = A[:]
    copy_A[1] += copy_A[0]
    # print(A, copy_A)
    for i in range(2, len(copy_A)):
        copy_A[i] += min(copy_A[i-1], copy_A[i-2])
    return copy_A[-1]
A_1 = [1, 2, 1, 3]
A_2 = [1, 2, 3, 4]
A_3 = [2, 76, 46]
solve(A_1)
solve(A_2)
solve(A_3)


##############################
# Editoral:
    # Python
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         a, b = A[0], A[0] + A[1]
#         for i in range(2, len(A)):
#             a, b = b, A[i] + min(a, b)
#         return b
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, a):
#         res = -1
#         b = a[0]
#         c = b+a[1]
#         for i in range(2,len(a)):
#             res = min(b,c)+a[i]
#             b = c 
#             c = res
#         return c
    # C++
#     int Solution::solve(vector<int> &A) {
#     int n = A.size();
#     assert(1 <= n && n <= 1e5);
#     for(int &x: A) assert(1 <= x && x <= 1e4);
#     A[1] += A[0];
#     for(int i = 2; i < n; ++i){
#         A[i] += min(A[i-1], A[i-2]);
#     }
#     return A.back();
# }   
    # Scala
# class Solution {
#   private val memory = scala.collection.mutable.Map[Int, Int]()

#   def solve(A: Array[Int]): Int  = {
#     val len = A.length
#     val first: Int = A.head
#     val last: Int = A(len - 1)


#     if(len == 2 || len == 3) {
#       return first + last
#     }

#     val a: Array[Int] = A.slice(1, len - 1)
#     memory(0) = a(0)
#     memory(1) = a(1)

#     for(i <- 2 until a.length) {
#       memory(i) = a(i) + Math.min(memory(i-1), memory(i-2))
#     }

#     first + Math.min(memory(a.length - 2), memory(a.length - 1)) + last
#   }
# }
    