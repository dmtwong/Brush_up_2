# -*- coding: utf-8 -*-
"""]
Created on Mon Jul 15 10:35:02 2024

@author: USER
"""
# Given a matrix of integers A of size N x M in which each row is sorted.
# Find and return the overall median of matrix A.
# NOTE: No extra memory is allowed.
# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
# Problem Constraints
# 1 <= N, M <= 10^5
# 1 <= N*M <= 10^6
# 1 <= A[i] <= 10^9
# N*M is odd

# Input Format
# The first and only argument given is the integer matrix A.
# Output Format
# Return the overall median of matrix A.

# Example Input
# Input 1: 
A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ] 
# Input 2: 
A = [   [5, 17, 100]    ]
# Example Output
# Output 1: 
#  5 
# Output 2: 
#  17

# Example Explanation
# Explanation 1: 
# A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
# Median is 5. So, we return 5. 
# Explanation 2:

# Median is 17.

def findMedian(A):
    sorted_A = []
    for i in range(len(A)):
        for j in range(len(A[0])):
             sorted_A.append(A[i][j])
    sorted_A.sort() 
    # print(sorted_A)
    mid = len(sorted_A) // 2 
    if len(A) % 2 == 0: 
        result = (sorted_A[mid-1] + sorted_A[mid]) / 2 
    else: 
        result = sorted_A[mid] 
    return result

findMedian(A)


# # Editorial:
#     int Solution::findMedian(vector<vector<int> > &A) {
#     int l = 0, r = INT_MAX;
#     int mid, req = (int)A.size() * (int)A[0].size();
#     assert(A.size()*A[0].size()<=1000000);
#     assert(req % 2);
#     while(r - l > 1){
#         mid = l + (r - l) / 2;
#         int cnt = 0;
#         for(auto &i: A){ 
#             //using upper bound in a sorted array to count number of elements smaller than mid
#             int p = upper_bound(i.begin(), i.end(), mid) - i.begin();
#             cnt += p;
#         }
#         if(cnt >= (req/2 +1)) r = mid;
#         else l = mid;
#     }   
#     return r;
# }

# Scala:
# class Solution {
#     def findMedian(A: Array[Array[Int]]): Int  = {
#       import java.util

#       val r = A.length
#       val c = A(0).length
    
#       var max = Int.MinValue
#       var min = Int.MaxValue
#       for (i <- 0 until r) {
#         min = math.min(min, A(i)(0))
#         max = math.max(max, A(i)(c - 1))
#       }
    
#       val desired = (r * c + 1) / 2
#       while (min < max) {
#         val mid = min + (max - min) /2
#         var place = 0
#         var get = 0
    
#         for (i <- 0 until r) {
#           get = util.Arrays.binarySearch(A(i), mid)
#           if(get < 0) get = Math.abs(get) - 1
#           else {
#             while (get < A(i).length && A(i)(get) == mid) {
#               get += 1
#             }
#           }
          
#           place += get
#         }
        
#         if(place < desired) min = mid + 1
#         else max = mid
#       }
      
#       min
#     }
# }

# GO:
# func findMedian(A [][]int) int {
#     median := (1 + (len(A) * len(A[0]))) / 2
#     min := A[0][0]
#     max := A[0][len(A[0])-1]

#     for i := 0; i < len(A); i++ {
#         if A[i][0] < min {
#             min = A[i][0]
#         }
#         if A[i][len(A[0])-1] > max {
#             max = A[i][len(A[0])-1]
#         }
#     }

#     for min < max {
#         mid := (max + min) / 2
#         count := counting(A, mid)
#         if count < median {
#             min = mid + 1
#         } else {
#             max = mid
#         }
#     }

#     return min
# }

# func counting(A [][]int, target int) int {
#     count := 0
#     for row := 0; row < len(A); row++ {
#         count += countRow(A, row, target)
#     }
#     return count
# }

# func countRow(A [][]int, row, target int) int {
#     mid := 0
#     low := 0
#     high := len(A[0]) - 1
#     for low < high {
#         mid = low + (high-low)/2
#         if target == A[row][mid] {
#             for A[row][mid+1] == target && (mid+1) < (len(A[0])-1) {
#                 mid++
#             }
#             mid++
#             break
#         } else if target < A[row][mid] {
#             high = mid
#         } else {
#             low = mid + 1
#         }
#     }

#     for mid >= 0 && A[row][mid] > target {
#         mid--
#     }
#     if mid+1 < len(A[row]) && A[row][mid+1] <= target {
#         mid = len(A[row]) - 1
#     }

#     return mid + 1
# }
    
