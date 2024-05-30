# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:38:54 2024

@author: USER
"""

# Problem Description
# You are given an integer N and the task is to reverse the digits of the given integer. 
# Return 0 if the result overflows and does not fit in a 32 bit signed integer
# Look at the example for clarification.

# Problem Constraints
# N belongs to the Integer limits.

# Input Format
# Input an Integer.

# Output Format
# Return a single integer denoting the reverse of the given integer.

# Example Input
# Input 1:
#  x = 123
# Input 2:
#  x = -123
# Example Output
# Output 1:
#  321
# Ouput 2:
#  -321
# Example Explanation
#  If the given integer is negative like -123 the output is also negative -321.

# class Solution:
# 	# @param A : integer
# 	# @return an integer
# 	def reverse(self, A):
def reverse(A):
    from collections import deque
    def int_str(result_str, isNeg):
        result_int = int(result_str)
        if isNeg == True:
            result_int = -result_int
        return result_int
    
    isNeg = False   
    if A < 0:
        isNeg = True
        A = abs(A)
    str_A = str(A)
    n_A = len(str_A)   
    deque_A = deque(str_A)
    result = ''
    # print(deque_A)
    for i in range(n_A):
        result += deque_A.pop() 
    # print(result)
    if n_A > 10:
        return 0
    elif n_A == 10:
        if int(result[0]) >= 3:
            return 0
        elif int(result[0]) == 2:
            # print('here')
            if isNeg == False:
                if int(result[1:]) > 147483647:                    
                    return 0
                else:
                    return int_str(result, isNeg)
            else:
                if int(result[1:]) > 147483648:
                    return 0        
                else:
                    return int_str(result, isNeg)
        else:
            return int_str(result, isNeg)
    else:
        return int_str(result, isNeg)

t1 = 123
t2 = 1000000045
t3 = 214748364
t4 = 2147483647
t4a = 2147483649
t4b = 3147483647
t5 = 1463847512
t6 = -1153072433
t7 = -1110968012
reverse(t1)
reverse(t2)
reverse(t3)
reverse(t4)
reverse(t5)
reverse(t4a)
reverse(t4b)
reverse(t6)
reverse(t7)