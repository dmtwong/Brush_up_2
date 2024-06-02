# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:20:58 2024

@author: USER
"""
# Problem Description
# Implement pow(x, n) % d.
# In other words, given x, n and d,
# Find (xn % d)
# Note that remainders on division cannot be negative. In other words, make sure the answer you return is non-negative integer.

# Problem Constraints
# -109 <= x <= 109
# 0 <= n <= 109
# 1 <= d <= 109

# Example Input
# Input 1:
x = 2
n = 3
d = 3
pow(x,n,d)
# Input 2:
x = 5
n = 2
d = 6

# Example Output
# Output 1:
# 2
# Output 2:
# 1


# Example Explanation
# Explanation 1:
# 23 % 3 = 8 % 3 = 2.
# Explanation 2:
# 52 % 6 = 25 % 6 = 1.
# class Solution:
#     # @param x : integer
#     # @param n : integer
#     # @param d : integer
#     # @return an integer
#     def pow(self, x, n, d):
def pow(x, n, d):
    result = 1
    base = x % d
    while n > 0:        
        if n % 2 == 1:
            result = (result * base) % d
        # print(n)
        n = n >> 1
        # print(n)
        sq_base = base ** 2
        base = sq_base % d
    result = result % d
    if result < 0:  
        result += d
    return result


    
    # Editoral:
        # Python 2.7
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : integer
#     # @return an integer
#     def pow(self, A, B, C):
#         result = 1
#         base = A % C
#         while B > 0:
#             if B % 2 == 1:
#                 result = (result*base) % C
#             B = B >> 1
#             base = (base*base)%C
#         return result%C

    # C++
# int Solution::pow(int x, int n, int p) {
#     assert(x >= -1e9 && x <= 1e9);
#     assert(n >= 0 && n <= 1e9);
#     assert(p >= 1 && p <= 1e9);
#     if (n == 0) return 1 % p;

# 			long long ans = 1, base = x;
# 			while (n > 0) {
# 				// We need (base ** n) % p. 
# 				// Now there are 2 cases. 
# 				// 1) n is even. Then we can make base = base^2 and n = n / 2.
# 				// 2) n is odd. So we need base * base^(n-1) 
# 				if (n % 2 == 1) {
# 					ans = (ans * base) % p;
# 					n--;
# 				} else {
# 					base = (base * base) % p;
# 					n /= 2;
# 				}
# 			}
# 			if (ans < 0) ans = (ans + p) % p;
# 			return ans;
# }