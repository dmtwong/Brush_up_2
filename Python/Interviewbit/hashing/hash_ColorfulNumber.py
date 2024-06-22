# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:49:19 2024

@author: USER
"""

# Problem Description
# For Given Number A, find if it's a COLORFUL number or not.
# COLORFUL number:
# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 3245 (10) 2**3 +2 
# 324 > 3 2 4 32 24 324: 6 = 3 + 2 +1 
# 12345 -> 5 + 4 + 3 + 2 + 1 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
# Return 1 if A is a COLORFUL number, else return 0
# Problem Constraints
# 0 <= A <= 109

# Input Format
# The first argument is an integer A.
# Output Format
# Return 1 if A is a COLORFUL number, else return 0


# Example Input
# A = 23


# Example Output
# 1


# Example Explanation
# A = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since the product of every digit of a sub-sequence is different.
# a = set()
# a.
# Output: 1

# class Solution:
# 	# @param A : integer
# 	# @return an integer
# 	def colorful(self, A):
def colorful(A):
    str_A = str(A)
    n_A = len(str_A)
    n_Num = 0
    result = set()
    for i in range(n_A):
        n_Num += 1
    bucket_agg = []
    n_str = 1
    for i in range(n_A):
        cur_bucket = []
        bucket_agg.append(cur_bucket)
        for j in range(n_A- n_str + 1):
            cur_str = str_A[j:(j+n_str)]
            cur_prod = 1
            for k in cur_str:
                cur_prod *= int(k)
            # print(i, j, cur_prod)
            if cur_prod not in result:
                result.add(cur_prod)
            else:
                return 0
            cur_bucket.append(cur_str)
        n_str += 1
    return 1
colorful(23)   
colorful(3245)   

# from functools import reduce
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def colorful(self, A):
#         products = set()
#         str_num = str(A)
#         for i in range(len(str_num)):
#             for j in range(i + 1, len(str_num) + 1):
#                 product = reduce(lambda x, y: x * y, map(int, list(str_num[i:j])))
#                 if product in products:
#                     return 0
#                 products.add(product)
#         return 1

# int Solution::colorful(int A) {
#    if (A < 10) return 1;
# 	set<int> s;
# 	vector<int> v;
# 	while (A) {
# 		int lastdigit = A % 10;
# 	    A /= 10;
# 		for (auto &i : v) i *= lastdigit;
# 		v.push_back(lastdigit);
# 		for (auto i : v) {
# 			if (s.count(i)) return 0;
# 			else s.insert(i);
# 		}
# 	}
# 	return 1;
# }

# class Solution {
#     def colorful(A: Int): Int  = {
#     val digits = math.log10(A).toInt + 1
#     val set = new collection.mutable.HashSet[Int]

#     for (windowSize <- 1 to digits) {
#       var num = A
#       for (i <- 1 to digits - windowSize + 1) {
#         val n = (num % (math.pow(10, windowSize))).toInt
#         val res = n.toString.toList.map(_.asDigit).foldLeft(1)(_ * _)
#         if (set.contains(res)) return 0
#         set += res
#         num /= 10
#       }
#     }

#     1
#     }
# }

# import (
#     "strconv"
# )
    
# func colorful(A int )  (int) {
#         strA := strconv.Itoa(A)
#         subNums := []string{}
#         for i := 1; i <= len(strA); i++ {
#                 for j := 0; i+j <= len(strA); j++ {
#                         subNums = append(subNums, strA[j:i+j])
#                 }
#         }
#         sumMap := map[int]bool{}

#         for i := 0; i < len(subNums); i++ {
#                 prod := 1
#                 for j := len(subNums[i]) - 1; j >= 0; j-- {
#                         digit := int(subNums[i][j] - '0')
#                         prod *= digit
#                 }
#                 if _, ok := sumMap[prod]; ok {
#                         return 0
#                 }
#                 sumMap[prod] = true
#         }
#         return 1
# }