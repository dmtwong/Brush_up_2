# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:22:01 2024

@author: USER
"""

# Problem Description
 
#  You are given an integer array A.

# You have to find the number of occurences of each number.
# Return an array containing only the occurences with the smallest value's occurence first.
# For example, A = [4, 3, 3], you have to return an array [2, 1], where 2 is the number of occurences for element 3, 
# and 1 is the number of occurences for element 4. But, 2 comes first because 3 is smaller than 4.

# Problem Constraints
# 1 <= |A| <= 105
# 1 <= Ai <= 109

# Input Format
# The first argument is the integer array A.

# Output Format
# Return an integer array denoting the occurences of each number.

# Example Input
# Input 1:
A = [1, 2, 3]
findOccurences(A)
# Input 2:
A = [4, 3, 3]

# Example Output
# Output 1:
# [1, 1, 1]
# Output 2:
# [2, 1]

# Example Explanation
# Explanation 1:
# All the elements occur once, so the resultant array should be [1, 1, 1].
# Explanation 2:

# Explained in the description above.
# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def findOccurences(self, A):
    
def findOccurences(A):
    import bisect 
    n_A = len(A)
    sort_A = []    
    for i in range(n_A):
        bisect.insort(sort_A, A[i])
    result = []
    count_curr  = 1
    key_curr = sort_A[0]
    for i in range(1, n_A):
        if sort_A[i] == key_curr:
            count_curr += 1
        else:
            result.append(count_curr)
            key_curr = sort_A[i]
            count_curr = 1
    result.append(count_curr)
    return result 


# # #     # Editoral:
# # #         # Python 
# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def findOccurences(self, A):
#         d = {}
#         for i in A:
#             try:
#                 d[i]+=1
#             except:
#                 d[i]=1
#         res = []
#         for i in sorted(d):
#             res.append(d[i])
#         return res
#     # Scala
# import scala.collection.mutable
# class Solution {
#     def findOccurences(A: Array[Int]): Array[Int]  = {
#         val m = mutable.Map[Int,Int]()
#         A.foreach { v =>
#             m.put(v, m.getOrElse(v, 0)+1)
#         }
#         val sortedKeys = m.keySet.toArray.sorted
#         val ret = Array.fill(sortedKeys.length)(0)
#         var idx = 0
#         sortedKeys.foreach { k =>
#             ret(idx) = m(k)
#             idx = idx+1
#         }
#         ret

#     }
# }

# C++:
# vector<int> Solution::findOccurences(vector<int> &A) {
#     map<int, int> mp;
#     for(auto &x : A){
#         mp[x]++;
#     }
#     vector<int> ans;
#     for(auto &x : mp){
#         ans.push_back(x.second);
#     }
#     return ans;
# }
# GO:
# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer array.
#  */
 
# import "sort"

# func findOccurences(A []int )  ([]int) {
#     frequencyMap := make(map[int]int)
#     for i:= 0 ; i< len(A) ;i ++ {
#         frequencyMap[A[i]] = frequencyMap[A[i]] + 1 
#     }
#     keysInOrder := []int{}
#     for k,_ := range(frequencyMap) {
#         keysInOrder = append(keysInOrder, k)
#     } 
#     sort.Ints(keysInOrder)
#     ans := []int{}
#     for i := 0 ; i< len(keysInOrder) ; i ++ {
#         ans = append(ans, frequencyMap[keysInOrder[i]])
#     }
#     return ans
# }
