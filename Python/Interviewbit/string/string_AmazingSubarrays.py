# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:24:46 2024

@author: USER
"""

# Problem Description
# You are given a string A, and you have to find all the amazing substrings of A.
# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
# Note: Take the mod of the answer with 10003.

# Problem Constraints
# 1 <= |S| <= 106
# S can have special characters

# Input Format
# Only argument given is string S.

# Output Format
# Return a single integer X mod 10003, where X is the number of Amazing Substrings in the given string.

# Example Input
A = 'ABEC'

# Example Output
# 6

# Example Explanation
# Amazing substrings of the given string are :
# 1. A
# 2. AB
# 3. ABE
# 4. ABEC
# 5. E
# 6. EC
# here the number of substrings is 6 and 6 % 10003 = 6.
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):

# temp = string.ascii_uppercase
# [let for let in temp if let in 'AEIOU']
# [let for let in range(len(temp)) if temp[let] in 'AEIOU']
# n_A = 4 
# sum([n_A - let for let in range(len(A)) if A[let] in 'AEIOU'])

def solve(A):
    import string
    n_A = len(A)
    sub_vowel = [n_A - let for let in range(len(A)) if A[let] in 'AEIOUaeiou']
    return(sum(sub_vowel)%10003)
solve(A)

# # Editorial
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         size = len(A)
#         count = 0
#         for index in range(size):
#             if A[index].isalpha() and A[index].lower() in ["a", "e", "i", "o", "u"]:
#                 count += (size-index)
#         return count%10003
    
# int Solution::solve(string s) {    
#     map<char, bool> m;
#     m['a'] = m['e'] = m['i'] = m['o'] = m['u'] = 1;
#     m['A'] = m['E'] = m['I'] = m['O'] = m['U'] = 1;
    
#     int n = s.length();
#     long long ans = 0;
#     for(int i = 0; i < n; i += 1) {
#         if(m[s[i]])
#             ans += (n - i);
#     }
#     return ans % 10003;
# }

# class Solution {
#     def solve(A: String): Int  = {
#         if (A.length == 0) return 0        
#         val set = Set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
#         def isVowel(c: Char) = set.contains(c)

#         val result = (0 until A.length).foldLeft(0) { case (acc, idx) =>
#             if (isVowel(A(idx))) acc + (A.length - idx) else acc
#         }

#         result % 10003
#     }
# }
