# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:05:35 2024

@author: USER
"""

# Problem Description
# Determine whether an integer is a palindrome. Do this without extra space.
# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.

# Problem Constraints
# INT_MIN <= A <= INT_MAX

# Input Format
# The first argument is an integer A.

# Output Format
# Return 1 if A is a Palindrome Integer else return 0.

# Example Input
# Input 1:
A = 12121
isPalindrome(A)
# Input 2:
A = 123
isPalindrome(A)

# Example Output
# Output 1:
# 1
# Output 2:
# 0

# Example Explanation
# Explanation 1:
#  12121 when reversed will be 12121, and 12121 = 12121, hence a palindrome number.

# Explanation 2:
#  123 when reversed will be 321, and 123 != 321, hence not a palindrome number

# class Solution:
# 	# @param A : integer
# 	# @return an integer
# 	def isPalindrome(self, A):
def isPalindrome(A):
    str_A = str(A)
    i = 0
    j = len(str_A) - 1
    compResult = True    
    while i <= j and compResult == True:
        # print(i, j)
        compResult = (str_A[i] == str_A[j])
        i += 1
        j -= 1
    return int(compResult)


# # Editorial:
#     def isPalindrome(self, A):
#         return int(str(A)==str(A)[::-1])
    
# int Solution::isPalindrome(int A) {
#     assert(A >= INT_MIN && A <= INT_MAX);
#     string a = to_string(A);
#     string b = a;
#     reverse(b.begin(), b.end());
#     if(a == b) return 1;
#     else return 0;
# }

# bool Solution::isPalindrome(int A) {
#     if(A<0)
#         return false;
#     long int temp = 0, temp2 = A;
#     while(A!=0)
#     {
#         temp = temp*10 + A%10;
#         A/=10;
#     }

#     if(temp==temp2)
#         return true;
#     else
#         return false;
# }

# class Solution {
#     def isPalindrome(A: Int): Int  = {
#         if (A.toString == A.toString.reverse) 1 else 0
#     }
# }

# func isPalindrome(A int )  (int) {
#     if A < 0 {
#         return 0
#     }
    
#     if A < 10 {
#         return 1
#     }

#     revNum := 0
#     currNum := A

#     for currNum != 0 {
#         rem := currNum % 10
#         revNum = revNum * 10 + rem
#         currNum = currNum / 10
#     }

#     if revNum == A {
#         return 1
#     }
#     return 0
# }
