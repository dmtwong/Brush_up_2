# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:32:28 2024

@author: USER
"""

# Problem Description
# You are given a string A which is a serialized string. You have to restore the original array of strings.
# The string in the output array should only have lowercase english alphabets.
# Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.
# For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.

# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The first argument is the string A.

# Output Format
# Return an array of strings which are deserialized.

# Example Input
# Input 1:
A = 'scaler6~academy7~'
# Input 2:

A = 'interviewbit12~'
deserialize(A)
# Example Output
# Output 1:
# ['scaler', 'academy']
# Output 2:
# ['interviewbit']

# Example Explanation
# Explanation 1:
# Length of 'scaler' is 6 and academy is 7. So, the resulting string is scaler6~academy7~.
# We hve to reverse the process.
# Explanation 2:

# Explained in the description above.
# class Solution:
    # @param A : string
    # @return a list of strings
    # def deserialize(self, A):
        
def deserialize(A):    
   list_A = A.split(sep = "~")
   result = [''.join(let for let in x if let.isalpha()) for x in list_A]
   result.pop()
   return result


# Editorial:
#     import re

# class Solution:
#     # @param A : string
#     # @return a list of strings
#     def deserialize(self, A):
#         x = re.split("[\d]*~", A)
#         x.pop(len(x) - 1)
#         return x
# vector<string> Solution::deserialize(string A) {
#     vector<string> ans;
#     int i = -1;
#     int j = 0;
#     while(j < A.size()){
#         while(A[j] <= 122 && A[j] >= 97){
#             j++;
#         }
#         ans.push_back(A.substr(i + 1, j - i - 1));
#         while(j < A.size() && A[j] != '~'){
#             j++;
#         }
#         i = j++;
#     }   
#     return ans;
# }

# func deserialize(A string )  ([]string) {
#     words := make([]string,0)
#     word := ""
#     first := true
#     for i:=0; i<len(A); i++ {
#         if (A[i] < 97 || A[i]> 122){
#             if first == true {
#                 words = append(words, word)
#                 first = false
#             }
#             word = ""
#             continue;
#         }
#         first = true
#         word += string(A[i])
#     }
#     return words
# }
