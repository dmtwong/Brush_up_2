# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:41:29 2024

@author: USER
"""

# Asked In:
# Problem Description
# Given an integer A.
# Write binary representation of the integer without leading zeros.
# Flip all bits then return the integer value of the binary number formed.
# Flipping means 0 -> 1 and 1 -> 0.
# Problem Constraints
# 1 <= A <= 109
# Input Format
# Given an integer A.
# Output Format
# Return an integer.

# Example Input
# Input 1:
A = 7
solve(A)
# Input 2:
A = 5
# Example Output
# Output 1:
# 0
# Output 2:
# 2

# Example Explanation
# Explanation 1:
# 7 -> 111 -> 000 ->0
# Explanation 2:
# 5 -> 101 -> 010 ->2
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def solve(self, A):
    
def solve(A):
    x = 1
    while x <= A:
        x <<= 1
    x -= 1
    return x ^ A

    # binary_A = []
    # while A > 0:
    #     cur = A % 2 
    #     binary_A.append(cur)
    #     A = A >> 1
    #     # print(A)
        
    # # while True: 
    # #     if binary_A[0] == 1:
    # #         break
    # #     else:
    # #         binary_A.pop(0)
                    
    # n_A = len(binary_A)
    # pow_Bin = n_A - 1
    # result = 0
    # print(binary_A)
    # for i in range(n_A):
    #     cur_i = abs(binary_A[i] - 1)
    #     print(cur_i)        
    #     result += (cur_i * (2 ** pow_Bin))
    #     pow_Bin -= 1
    #     print(result, pow_Bin)
    # return result

A = 100000
solve(A) # ExpecteD:31071

# Editorial:
#     class Solution:
#     # @param A : integer
#     # @return an integer
#     def solve(self, A):
#         x=''
#         y=''
#         while(A!=0):
#             x+=str(A%2)
#             A//=2
#         x=x[::-1]    
#         for i in range(len(x)):
#             if x[i]=='1':
#                 y+='0'
#             else:
#                 y+='1'
#         return  int(y,2)
    
# int Solution::solve(int A) {
#     assert(1<=A && A<=1e9);
#     int x = 1;
#     while(x <= A){
#         x <<= 1;
#     }
#     x--;
#     return (x ^ A);
# }
# import "strconv"

# func solve(A int )  (int) {
#     bin := strconv.FormatInt(int64(A), 2)
#     var binReverse string
#     for _, s := range bin {
#         if string(s) == "0" {
#             binReverse += "1"
#         } else {
#             binReverse += "0"
#         }
#     }
#     result, _ := strconv.ParseInt(binReverse, 2, 64)
#     return int(result)
# }

