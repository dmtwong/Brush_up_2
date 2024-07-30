# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:12:04 2024

@author: USER
"""

# Problem Description
# Given a string A. The only operation allowed is to insert characters at the beginning of the string.
# Find how many minimum characters are needed to be inserted to make the string a palindrome string.
# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The only argument given is string A.

# Output Format
# Return the minimum characters that are needed to be inserted to make the string a palindrome string.

# Example Input
# Input 1:
A = "ABC"
solve(A)
# Input 2:
A = "AACECAAAA"

# Example Output
# Output 1:
# 2
# Output 2:
# 2

# Example Explanation
# Explanation 1:
# Insert 'B' at beginning, string becomes: "BABC".
# Insert 'C' at beginning, string becomes: "CBABC".
# Explanation 2:
# Insert 'A' at beginning, string becomes: "AAACECAAAA".
# Insert 'A' at beginning, string becomes: "AAAACECAAAA".


# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
        
def solve(A):
    n_A = len(A)
    rev_A = A[::-1]    
    mirror_A = A + "!" + rev_A    
    
    def search(s_A):        
        n_s_A = len(s_A)
        temp = [0] * n_s_A
        # temp[0] = 0 

        len_A = 0
        i = 1
        while i < n_s_A:         
            if s_A[i] == s_A[len_A]:
                # print(i, s_A, len_A)
                # print(temp)
                len_A += 1
                temp[i] = len_A
                i += 1             
            elif len_A != 0:               
                # print('here', len_A, i)
                # print(temp)
                len_A = temp[len_A - 1]
            else: 
                # print('there', i)
                # print(temp)
                temp[i] = 0
                i += 1     
        return temp
    
    result = search(mirror_A)    
    return n_A - result[-1]

# Editroial
# class Solution:
#     # @param A : string
#     # @return an integer
#     def create_lps(self,A):
#         M=len(A)
#         lps=[None]*M
#         l=0
#         lps[0]=l
#         i=1
        
#         while i<M:
#             if A[i]==A[l]:
#                 l+=1
#                 lps[i]=l
#                 i+=1
#             else:
#                 if l!=0:
#                     l=lps[l-1]
#                 else:
#                     lps[i]=0
#                     i+=1
#         return lps
        
        
#     def solve(self, A):
#         lps=self.create_lps(A+"$"+A[::-1])
#         return len(A)-lps[-1]

# vector<int> computeLPSArray(string str) {
#     int M = str.length();
#     vector<int> lps(M);
#     int len = 0;
#     lps[0] = 0;
#     int i = 1;
#     while (i < M) {
#         if (str[i] == str[len]) {
#             len++;
#             lps[i] = len;
#             i++;
#         }
#         else {
#             if (len != 0) {
#                 len = lps[len-1];

#             }
#             else {
#                 lps[i] = 0;
#                 i++;
#             }
#         }
#     }
#     return lps;
# }

# int Solution::solve(string str) {
#     assert(str.size() >= 1 && str.size() <= 1e6); 
#     string revStr = str;
#     reverse(revStr.begin(), revStr.end());
#     string concat = str + "$" + revStr;
#     vector<int> lps = computeLPSArray(concat);
#     return (str.length() - lps.back());
# }

# class Solution {
#     def solve(A: String): Int  = {
#         def isPalindrome(s:String) = s sameElements s.reverse
        
#         val ss = A.reverse
#         for {
#             i <- ss.indices
#             if isPalindrome(ss.substring(i))
#         } return i
#         0
#     }
# }


# func solve(A string )  (int) {
#     if isPalindrome(A) {
#         return 0
#     }
    
#     i:= len(A) -1
#     potentialPalindrome := A[i:] + A 
#     for !isPalindrome(potentialPalindrome) {
#         i -= 1
#         potentialPalindrome = Reverse(A[i:]) + A
#     }
    
#     return len(A) - i
# }

# func Reverse(s string) string {
#     runes := []rune(s)
#     for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
#         runes[i], runes[j] = runes[j], runes[i]
#     }
#     return string(runes)
# }


# func isPalindrome(input string) bool {
# 	for i := 0; i < len(input)/2; i++ {
# 		if input[i] != input[len(input)-i-1] {
# 			return false
# 		}
# 	}
# 	return true
# }