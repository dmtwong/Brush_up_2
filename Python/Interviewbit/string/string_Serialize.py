# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:09:46 2024

@author: USER
"""

# Problem Description
# You are given an array A of strings and we have to serialize it and return the serialized string.
# Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.
# For example, for a string 'interviewbit', its serialized version would be 'inteviewbit12~'.
# Problem Constraints
# 1 <= |A| <= 1000
# 1 <= |Ai| <= 1000
# Ai only contains lowercase english alphabets.
# Input Format
# The first argument A is the string array A.
# Output Format
# Return a single integer denoting the serialized string.
# Example Input
# Input 1:
A = ['scaler', 'academy']
# Input 2:
# A = ['interviewbit']
# Example Output
# Output 1:
# scaler6~academy7~
# Output 2:
# interviewbit12~
# Example Explanation
# Explanation 1:
# Length of 'scaler' is 6 and academy is 7. So, the resulting string is scaler6~academy7~.
# Explanation 2:
# Explained in the description above.
# class Solution:
#     # @param A : list of strings
#     # @return a strings
#     def serialize(self, A):

def serialize(A):
    result = ''
    for i in A:
        n_i = str(len(i))
        cur_temp = i+n_i+"~"
        result += cur_temp
    return result
serialize(A)

# Editorial
#     Python:
# class Solution:
#     # @param A : list of strings
#     # @return a strings
#     def serialize(self, A):
#         ans = ""
#         for x in (A):
#             ans += x
#             ans += str(len(x))
#             ans += '~'
        
#         return ans

# string Solution::serialize(vector<string> &A) {
#     assert(A.size() >= 1 && A.size() <= 1000);
#     string ans = "";
#     for(auto &x: A){
#         assert(x.size() >= 1 && x.size() <= 1000);
#         for(auto &y : x){
#             assert(y >= 'a' && y <= 'z');
#         }
#         ans += x;
#         ans += to_string(x.size());
#         ans += '~';
#     }
#     return ans;
# }

# GOL
# /**
#  * @input A : array of strings
#  * 
#  * @Output string.
#  */

# import (
#     "strings"
#     "strconv"
#     )
# func serialize(A []string )  (string) {
#     count := 0
#     for i, a := range A {
#         A[i] = a + strconv.Itoa(len(a)) + "~"
#         count += len(A[i])
#     }
    
#     B := strings.Join(A, "")
#     return B
# }
