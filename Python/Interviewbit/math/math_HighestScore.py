# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:46:07 2024

@author: USER
"""
# Self note: the answer expect average not mean

# Problem Description
 
# You are given a 2D string array A of dimensions N x 2,
# where each row consists of two strings: first is the name of the student, second is their marks.
# You have to find the maximum average mark. If it is a floating point, round it down to the nearest integer less than or equal to the number.

# Problem Constraints
# 1 <= N <= 105
# Input Format
# The first argument is a 2D string array A.

# Output Format
# Return a single integer which is the highest average mark.

# Example Input
# Input 1:
A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"]]
highestScore(A)
# Input 2:
A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"], ["Alice", "10"]]

A = [  ['fqyh', 79],
  ['fqyh', 12],
  ['fqyh', 46],
  ['fqyh', 45],
  ['fqyh', 20],
  ['fqyh', 10],
  ['fqyh', 92],
  ['fqyh', 93],
  ['fqyh', 72],
  ['fqyh', 53],
  ['fqyh', 39],
  ['fqyh', 99],
  ['fqyh', 52],
  ['fqyh', 59]
]
# Example Output
# Output 1:
# 90
# Output 2:
# 85

# Example Explanation
# Explanation 1:
# Alice has the highest average with 90 marks.
# Explanation 2:

# Bob has the highest average with 85 marks.

# class Solution:
#     # @param A : list of list of strings
#     # @return an integer
#     def highestScore(self, A):
def highestScore(A):
    # import bisect 
    # import math
    from collections import defaultdict
    # n_A = len(A)
    dict_def = defaultdict(list)
    for i in A:
        dict_def[i[0]].append(i[1])
    result = 0
    for i in dict_def.values():
        n_i = len(i)
        avg_i = sum(list(map(int, i))) // n_i
        # print(avg_i)
        result = max(result, avg_i)
    return result

# test_1 = [10, 12, 20, 39, 45, 46, 52, 53, 59, 72, 79, 92, 93, 99]
# test_1[6]
# test_1[7]
# test_1[8]

# #     # Editoral:
# #         # Python 
# from collections import defaultdict
# class Solution:
#     # @param A : list of list of strings
#     # @return an integer
#     def highestScore(A):
#         dic=defaultdict(list)
#         for val in A:
#             dic[val[0]].append(int(val[1]))
#         print(dic)
#         print(dic.keys())
#         print(dic.values())
#         ans=0
#         for val in dic.values():
#             n=len(val)
#             tot=sum(val)
#             avg=tot//n
#             ans=max(ans,avg)
#         return ans

# C++:
# int Solution::highestScore(vector < vector < string > > & A) {
#     map < string, pair < int, int >> mp;
#     for (int i = 0; i < A.size(); i++) {
#         if (mp.find(A[i][0]) == mp.end()) {
#             mp[A[i][0]] = make_pair(0, 0);
#         }
#         mp[A[i][0]] = make_pair(mp[A[i][0]].first + stoi(A[i][1]), mp[A[i][0]].second + 1);
#     }
#     int ans = 0;
#     for (auto & x: mp) {
#         ans = max(ans, x.second.first / x.second.second);
#     }
#     return ans;
# }

# Scala:
# /**
#  * @input A : 2D string array
#  * 
#  * @Output Integer
#  */
# import "strconv"
# //import "fmt"

# func highestScore(A [][]string )  (int) {
#     avgMarks := make(map[string]int)
#     timesSeen := make(map[string]int)

#     for i := 0; i < len(A); i++ {
#         curName := A[i][0]
#         _, found := avgMarks[curName]
#         if !found {
#             avgMarks[curName], _ = strconv.Atoi(A[i][1])
#             timesSeen[curName] = 1
#             continue
#         }
        
#         curMark, _ := strconv.Atoi(A[i][1])
#         avgMarks[curName] += curMark
#         timesSeen[curName] ++
#     }

#     //fmt.Println(avgMarks)
#     //fmt.Println(timesSeen)

#     for key, _ := range avgMarks {
#         avgMarks[key] = avgMarks[key] / timesSeen[key]
#     }

#     highest := -1
#     for _, value := range avgMarks {
#         if value > highest {highest = value}
#     }

#     return highest
# }
