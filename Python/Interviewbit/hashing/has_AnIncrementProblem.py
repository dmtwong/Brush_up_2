# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:11:29 2024

@author: USER
"""

# Problem Description
# Given a stream of numbers A. On arrival of each number, you need to increase its first occurrence by 1 and include this in the stream.
# Return the final stream of numbers.
# Note: You will traverse the stream from left to right and update the first occurrence of the number by 1, if found.

# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10000

# Input Format
# First and only argument is the array A.
# Output Format
# Return an array, the final stream of numbers.

# Example Input
# Input 1: 
A = [1, 1] 
# Input 2:
A = [1, 2]
#  Input 3:
A = [1, 1, 2, 2]
solve(A)
# Example Output
# Output 1:
# [2, 1]
#  Output 2:
# [1, 2]
#  Output 3:
# [3, 1, 3, 2]
# Example Explanation
# Explanation 1:
# On arrival of the second element, the other element is increased by 1.
#  Explanation 2:
# No increases are to be done.
# Explanation 3:
# Stream after arrival of numbers (1-based indexing):
#   First number  (1): [1]          , Simply push 1 to the stream
#   Second number (1): [2, 1]       , Increment first occurence of 1, present at 1st Index and push 1 to the stream
#   Third number  (2): [3, 1, 2]    , Increment first occurence of 2, present at 1st Index and push 2 to the stream
#   Fourth number (2): [3, 1, 3, 2] , Increment first occurence of 2, present at 3rd Index and push 2 to the stream

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
def solve(A):
    unique = set()
    result = []
    n_A = len(A)
    for i in range(n_A):
        cur_i = A[i]
        if cur_i in unique:
            # unique.add(cur_i)
            # result.append(cur_i)
        # else:
            ix_i = result.index(cur_i)
            result[ix_i] += 1
            unique.add(result[ix_i])
        unique.add(cur_i)
        result.append(cur_i)
    return result
A = [ 1, 2, 3, 2, 3, 1, 4, 2, 1, 3 ] # Expect: 4 5 3 2 3 2 4 2 1 3 
solve(A)

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         indices = {}
        
#         for (i, num) in enumerate(A):
#             if num not in indices:
#                 indices[num] = [i]
#                 continue
                
#             prev = indices[num][0]
#             A[prev] += 1
#             if A[prev] in indices:
#                 indices[A[prev]].append(prev)
#                 indices[A[prev]] = sorted(indices[A[prev]])
#             else:
#                 indices[A[prev]] = [prev]
                
#             indices[num][0] = i
#             indices[num] = sorted(indices[num])
        
#         return A


# vector<int> Solution::solve(vector<int> &A) {
#     vector<int> res;
#     for(int i=0;i<A.size();i++) {
#         auto it=find(res.begin(),res.end(),A[i]);
#         if(it!=res.end()) {
#             (*it)++;
#             res.push_back(A[i]);
#         }
#         else {
#             res.push_back(A[i]);
#         }
#     }
#     return res;
# }

# class Solution {
#     def solve(A: Array[Int]): Array[Int]  = {

#     def loop(i: Int, cache: Map[Int, Int]): Array[Int] = {
#       if (i == A.length) A
#       else {
#         val nCache =
#           if (cache.contains(A(i))) {
#             val oldPos = cache(A(i))
#             val newVal = A(oldPos) + 1

#             // update the array and add the new element to the cache
#             A(oldPos) = newVal

#             // if the new value, ie the old one increment of one unit
#             // is already present in the cache, update the index to the min
#             // otherwise add it as a new item to the cache
#             if (cache.contains(newVal))
#               cache + (newVal -> Math.min(oldPos, cache(newVal)))
#             else
#               cache + (newVal -> oldPos)
#           }
#           else cache
#         loop(i + 1, nCache + (A(i) -> i))
#       }
#     }

#     loop(0, Map.empty[Int, Int])
#   }


# }

# func solve(A []int )  ([]int) {
#     m := make(map[int]int)
    
#     for i, v := range A {
#         if _, ok := m[v]; ok {
#             A[m[v]]++
#             m[A[m[v]]] = m[v]
#             m[v] = i
#         } else {
#             m[v] = i
#         }
#     }
#     return A
# }

