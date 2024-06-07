# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:32:11 2024

@author: USER
"""

# Another question which belongs to the category of questions which are intentionally stated vaguely. 

# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

# Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

# Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output”

# For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations.

# Input Format

# The only argument given is integer A.
# Output Format

# Return a string denoting roman numeral version of A.
# Constraints

# 1 <= A <= 3999
# For Example

# Input 1:
    A = 5
# Output 1:
#     "V"

# Input 2:
    A = 14
intToRoman(A)
# Output 2:
#     "XIV"

# class Solution:
	# @param A : integer
	# @return a strings
def intToRoman(A):
    str_A = str(A)
    n_A = len(str_A)
    ix_A = n_A 
    result = ""
    def sub_roman(ix_A):
        if ix_A == 4:
            return {1: "M"} #5: "D" }
        elif ix_A == 3:
            return {1: "C", 5: "D", 10: "M"}
        elif ix_A == 2:
            return {1: "X", 5: "L", 10: "C"}
        elif ix_A == 1:
            return {1: "I", 5: "V", 10: "X"}   
        # match ix_A:
        #     case 4:
        #         return {1: "M"} #5: "D" }
        #     case 3: 
        #         return {1: "C", 5: "D", 10: "M"}
        #     case 2: 
        #         return {1: "X", 5: "L", 10: "C"}
        #     case 1: 
        #         return {1: "I", 5: "V", 10: "X"}   
    for i in str_A:
        cur_i = int(i)        
        dict_cur = sub_roman(ix_A)
        ix_A -= 1
        # print(cur_i)
        if ix_A == 4:            
            result += cur_i * dict_cur[1] 
        else: 
            if cur_i == 9:
                result += (dict_cur[1]+dict_cur[10])
            elif cur_i > 5: 
                extra_cur = cur_i - 5
                result += (dict_cur[5] + extra_cur*dict_cur[1])
            elif cur_i == 5: 
                result += dict_cur[5]
            elif cur_i == 4:
                # print('here')                
                result += (dict_cur[1]+dict_cur[5])
            else:
                # print('there')
                result += cur_i * dict_cur[1]
    return result

A = 3999
intToRoman(A)

# #     # Editoral:
# #         # Python 
# class Solution:
#     # @param A : integer
#     # @return a strings
#     def intToRoman(self, A):
#         roman_map = {
#             1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
#             40: "XL", 50: "L", 90: "XC", 100: "C",
#             400: "CD", 500: "D", 900: "CM", 1000: "M"
#         }
#         num = A
#         result = ''
#         values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         for value in values:
#             while num >= value:
#                 result += roman_map[value]
#                 num -= value
#         return result
# Scala:
#     class Solution {
#     def intToRoman(A: Int): String  = {
#         var n: Int = A
#         var i: Int = 0
#         val roman = new StringBuilder()
#         val nums = Array[Int] (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
#         while(n > 0) {
#             val times = n / nums(i)
#             roman ++= concatString(getRomanValue(nums(i)), times)
#             n = n % nums (i)
#             i += 1
#         }
#         roman.toString
#     }
    
#     //Find the Integral Value for roman symbol
#     def getRomanValue(n: Int): String = n match {
#         case 1 => "I"
#         case 4 => "IV"
#         case 5 => "V"
#         case 9 => "IX"
#         case 10 => "X"
#         case 40 => "XL"
#         case 50 => "L"
#         case 90 => "XC"
#         case 100 => "C"
#         case 400 => "CD"
#         case 500 => "D"
#         case 900 => "CM" 
#         case 1000 => "M"
#     }
#     def concatString(sym: String, n: Int): String  = {
#         if(n == 0) "" else sym + concatString(sym, n-1)
        
#     }
# C++:
#     string Solution::intToRoman(int A) {
#     string M[] = {"", "M", "MM", "MMM"};
#         // 100, 200, 300, .. 900
#         string C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
#         // 10, 20, ... 90
#         string X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
#         // 1, 2, ... 9
#         string I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
#         return M[A/1000] + C[(A%1000)/100] + X[(A%100)/10] + I[A%10];
# }
# GO:
#     /**
#  * @input A : Integer
#  * 
#  * @Output string.
#  */
# import (
#     "sort"
# )

# func intToRoman(A int )  (string) {
#     var result string
#     if A < 1 || A > 3999 {
#         return result
#     }
#     intToStrMap := map[int]string{
#         1000: "M",
#         900: "CM",
#         500: "D",
#         400: "CD",
#         100: "C",
#         90: "XC",
#         50: "L",
#         40: "XL",
#         10: "X",
#         9: "IX",
#         5: "V",
#         4: "IV",
#         1: "I",
#     }
#     sortedKeys := []int{}
#     for key, _ := range intToStrMap {
#         sortedKeys = append(sortedKeys, key)
#     }
#     sort.Slice(sortedKeys, func(i, j int) bool { return sortedKeys[i] > sortedKeys[j] })
#     for _, key := range sortedKeys {
#         value := intToStrMap[key]
#         quotient := A / key
#         if quotient != 0 {
#             for i := 0; i < quotient; i++ {
#                 result = result + value
#             }
#             A = A - (key * quotient)
#         }
#     }
#     return result
# }