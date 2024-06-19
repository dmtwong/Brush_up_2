# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:44:41 2024

@author: USER
"""

# Find if the given number is a power of 2 or not. More specifically, find if the given number can be expressed as 2^k where k >= 1.
# Note: The number length can be more than 64, which means the number can be greater than 2 ^ 64 (out of long long range)

# Problem Constraints
# 1 <= |A| <= 104

# Input Format
# The first argument is a string A.

# Output Format
# Return 1 if the number is a power of 2 else return 0

# Example Input
# 128

# Example Output
# 1

# Example Explanation
# 128 can be expressed as 2 ^ 7.

# class Solution:
# 	# @param A : string
# 	# @return an integer
# 	def power(self, A):
def power(A):
    A = int(A)
    if A == 1:
        return 0
    while A > 0:
        if A != 1 and A % 2 == 1:
            return 0
        else: 
            A = A >> 1
            # print(A)
    return 1
        
power(128)
power(127)
power(1)

# # Fastest rather than editorial
# int Solution::power(string A) {
#     int N = A.length();
#     //Method 1
#     int num = A[0]-'0';
#     for(int i = 1; i<N; i++) num = (num*10)+(A[i]-'0');
#     if(num == 1) return 0;
#     //for eg: 8 - 1000 and 7 - 0111. So 1000&0111 = 0. 
#     if((num & (num-1)) == 0) return 1;
#     return 0;
# }
# class Solution {
#     def power(A: String): Int  = {
#       var s = BigInt(A)
#       if (s < 2) 0
#       else {
#         while (s > 1) {
#           val xx = s & 1
#           if (s > 1 && xx != 0) return 0
#           s = s >> 1
#         }
#         1
#       }
#     }
# }

# class Solution:
#     # @param A : string
#     # @return an integer
#     def power(self, A):
#         A = int(A)
#         if A == 1:
#             return 0
#         if A & (A-1) == 0:
#             return 1
#         return 0
    
# import (
#     "fmt"
#     "math/big"
# )
# /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func power(A string )  (int) {
#     // Power of 2 implies that only 1 bit in the int is set
#     // IE 2,4,8,16,32.. etc
#     //  00010, 001000, 010000, 100000
#     // There are fancy algorithms for detecting number of bits set that are:
#     // 1. probably not worth memorizing
#     // 2. technically overkill for a problem like this
    
#     // A more simple algorithm would be to bit shift right 64 times.
#     // If the 1st bit is set and the value is 1, then it's a power of 2.
   
#     val := new(big.Int)
#     _, err := fmt.Sscan(A, val)
    
#     if val.Bit(0) > 0 || err != nil {
#         return 0
#     }

#     bitcount := 0
#     for i := 1; i < val.BitLen(); i++ {
#         if val.Bit(i) > 0 {
#             bitcount++
#             if bitcount > 1 {
#                 return 0
#             }
#         }
#     }

#     return bitcount
# }