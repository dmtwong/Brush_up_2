# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:21:47 2024

@author: USER
"""
# Problem Description
# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

# Problem Constraints
# 1 <= |A| <= 105
# A consists only of lower-case characters.

# Input Format
# First argument is an string A.
# Output Format
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

# Example Input
# Input 1:
#  A = "abcde"
# Input 2:
# solve(A)
#  A = "abbaee"
# Example Output
# Output 1:
#  0
# Output 2:
#  1

# Example Explanation
# Explanation 1:

#  No possible rearrangement to make the string palindrome.
# Explanation 2:

#  Given string "abbaee" can b
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
def solve(A):
    dict_table = {}
    for i in A:
        if dict_table.get(i) == None:
            dict_table[i] = 1
        else:
            dict_table[i] += 1
    
    count_odd = 0
    
    for val in dict_table.values():
        # print(val)
        if val % 2 == 1:
            count_odd += 1
    if count_odd <= 1:
        return 1
    else:
        return 0

# my attenmpt on c++:
# 		unordered_map<string, int> char_hash;
# 		for (auto ch: A){
# 			auto iter = char_hash.find(std::string() + ch);
# 			if (iter == char_hash.end()){
# 				char_hash.insert(std::string() + ch, int(1));
# 			} else {
# 				iter->second += 1;
# 			}
# 		}
# 		count_odd = 0;
# 		for (auto& iter_2: char_hash) {
# 			if ((iter_2->second % 2) == 1){
# 				count_odd += 1;
# 			}
# 		}
# 		if (count_odd > 1){
# 			return 0;
# 		} else {
# 			return 1;
# 		}
#     # function to check whether characters 
# Editorial:
# int Solution::solve(string A) {
#   int hashMap[26] = {0};
#   for (char a: A)
#     hashMap[a - 'a']++;
#   int odd = 0;
#   for (int a: hashMap)
#     if (a % 2)
#       odd++;
#   if (odd > 1)
#     return 0;
#   return 1;
# }

# # of a string can form a palindrome  
# def canFormPalindrome(st) : 
  
#     # Create a count array and initialize   
#     # all values as 0 
#     count = [0] * (26) 
  
#     # For each character in input strings, 
#     # increment count in the corresponding 
#     # count array 
#     for i in range( 0, len(st)) : 
#         count[ord(st[i])-ord('a')] = count[ord(st[i])-ord('a')] + 1
  
#     # Count odd occurring characters 
#     odd = 0
      
#     for i in range(0, 26) : 
#         if (count[i] & 1) : 
#             odd = odd + 1
  
#         if (odd > 1) : 
#             return False
              
#     # Return true if odd count is 0 or 1,  
#     return True
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         if(canFormPalindrome(A)):
#             return 1
#         return 0

# import scala.collection.mutable.HashMap
# class Solution {
#     def solve(A: String): Int = {
#     var flag: Boolean = false
#     val map = HashMap[Char, Int]()
#     for (a <- A) {
#       map.update(a, map.getOrElse(a, 0) + 1)
#     }
#     for ((x, v) <- map) {
#       if (v % 2 == 1)
#         if(!flag && A.length % 2 == 1) flag = true
#         else return 0
#       }
#     1
#   }
# }

# func solve(A string )  (int) {
#     m := make(map[rune]int)
#     isOdd := len(A) % 2
#     oddChar := 0
#     for _, r := range A {
#         m[r]++
#     }
#     for _, v := range m {
#         if v % 2 == 1 {
#             oddChar++
#         }
#         if oddChar > isOdd {
#             return 0
#         }
#     }
#     return 1
# }
