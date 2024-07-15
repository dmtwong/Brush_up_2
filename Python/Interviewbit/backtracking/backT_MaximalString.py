# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:36:07 2024

@author: USER
"""

# Self note: review this one

# Problem Description
# Given a A A and integer B, what is maximal lexicographical A that can be made from A if you do atmost B swaps.

# Problem Constraints
# 1 <= |A| <= 9
# A contains only digits from 0 to 9.
# 1 <= B <= 5

# Input Format
# First argument is A A.
# Second argument is integer B.

# Output Format
# Return a A, the naswer to the problem.

# Example Input
# Input 1:
A = "254"
B = 1
solve(A, B)
# Input 2:
A = "254"
B = 2

# Example Output
# Output 1:
#  524
# Output 2:
#  542

# Example Explanation
# Explanation 1:
#  Swap 2 and 5.
# Explanation 2:
    
# Swap 2 and 5 then swap 4 and 2.

# class Solution:
#     # @param A : A
#     # @param B : integer
#     # @return a As
#     def solve(self, A, B):
def solve(A, B):
    C = [A]
    def solve_2(A, B, C):
        def swap(A, i, j):
            return (A[:i] + A[j] + 
                    A[i + 1:j] + 
                    A[i] + A[j + 1:])
            
        if B == 0:
            return
    
        n = len(A)
    
        for i in range(n - 1):
            for j in range(i + 1, n):
                if A[i] < A[j]:
                    A = swap(A, i, j)
                    if A > C[0]:
                        C[0] = A
                    solve_2(A, B - 1, C)
                    A = swap(A, i, j)
    solve_2(A, B, C)
    return C[0]
    
                    
    # # from collections import defaultdict
    # # dd_1 = defaultdict(lambda: 0)
    # list_A = [int(i) for i in A]
    # from collections import OrderedDict
    # d_1 = OrderedDict()
    # n_A = len(A)
    # for i in range(9, -1, -1):
    #     d_1[i] = 0
    # for i in A:
    #     # if d_1.get(i) == None:
    #     #     d_1[i] = 1
    #     # else:
    #     #     d_1[i] += 1
    #     int_i = int(i)
    #     d_1[int_i] += 1
    
    
    # keys_d_1 = list(d_1.keys())
    # for i in keys_d_1:
    #     if d_1[i] == 0:
    #         d_1.pop(i)
    # # return d_1       

    # i = 0
    # swap_Left = B
    # keys_left = list(d_1.keys())
    # cur_high = keys_left[0] 
    # j = 1
    # while i < n_A and swap_Left >= 0:
    #     # print(i, swap_Left)
    #     int_i = int(list_A[i])
    #     # print(int_i, cur_high, 'this')
    #     if int_i == cur_high:
    #         i += 1
    #         continue
    #     else:
    #         print(i, swap_Left, list_A)
    #         temp = list_A[i: n_A][:]
    #         print(temp)
    #         temp.reverse()
    #         print(temp)
    #         ix_high = (len(temp) - list_A.index(cur_high) - i + 1 - j)
    #         print(ix_high)
    #         # print(ix_high, 'that')
    #         # ix_high = 0
    #         # for j in range(i, n_A):
                
    #         list_A[i], list_A[i+ ix_high] = list_A[i+ ix_high], list_A[i]
    #         swap_Left -= 1
    #         j += 1
    #         # print(d_1, "before")
    #         d_1[keys_left[0]] -= 1            
    #         # print(d_1, "after")
    #         # print(keys_left)
    #         # print(keys_d_1)
    #         # print(keys_d_1[keys_left[0]])
    #         if d_1[keys_left[0]] == 0:
    #             keys_left.pop(0)
    #             d_1.pop(cur_high)
    #             # print(d_1)
    #             cur_high = int(keys_left[0])
    #         # print(cur_high)
    #         i += 1
    # list_A = [str(i) for i in list_A]
    # return int(''.join(list_A))

A = "129814999"
B = 4    
solve(A, B) # 999984211

# Editorial:
# class Solution:
#     # @param A : string
#     # @param B : integer
#     # @return a strings
#     def solve(self, A, B):
#         if len(A) == 1 or B == 0:
#             return A
#         combinations = []
#         for (i, s) in enumerate(A):
#             currString = s + A[1:i] + A[0] + A[i+1:] if not i == 0 else A
#             combinations.append(currString)
#         ans = '0'
#         for s in combinations:
#             newComb = self.solve(s[1:], B-1) if s != A else self.solve(s[1:], B)
#             ans =  max(ans, s[0] + newComb)
#         return ans

# void swap(char &a,char &b)
# {
#     char c=a; a=b; b=c;
# }

# string ans;
# int n;

# void check(int i,string &str,int k)
# {
#     if(ans<str)
#     ans=str;
    
#     if(!k || i==n)
#     return;
    
#     check(i+1,str,k);

#     for(int j=i+1;j<n;j++)
#     {
#         if(str[j]>str[i])
#         {
#             swap(str[j],str[i]); 
#             check(i+1,str,k-1);
#             swap(str[j],str[i]); 
#         }
#     }
# }
# string Solution::solve(string str, int k) 
# {
#      ans=str;
#     n=str.length();
    
#      check(0,str,k);
#      return ans;
# }

# class Solution {
#     def swap(s: String, i: Int, j: Int): String = {
#     val cs = s.toCharArray
#         val swp = cs(i)
#         cs(i) = cs(j)
#         cs(j) = swp
#         new String(cs)
#     }
  
#     def solve(A: String, B: Int): String = {
#         var maxString = A
#         def loop2(swaps: Int, soFar: String): Unit = {
#           var mutableStr = soFar
#           if (swaps > 0)
#             for {i <- 0 until soFar.length
#                  j <- i + 1 until soFar.length
#                  } {
#               if (mutableStr.charAt(j) > mutableStr.charAt(i)) {
#                 mutableStr = swap(mutableStr, i, j)
#                 loop2(swaps - 1, mutableStr)
#                 mutableStr = swap(mutableStr, i, j)
#               }
#             } else
#             if (mutableStr > maxString) maxString = mutableStr
    
#         }
    
#         loop2(B, A)
#         maxString
#     }
# }
                     
#                      import "strings" 
# func solve(A string , B int )  (string) {
#     maxSoFar := A
#     a := strings.Split(A,"")
#     recur(a,0,B,&maxSoFar)
#     return maxSoFar
# }

# func swap(a []string, i, j int) []string {
#     temp := a[i]
#     a[i] = a[j]
#     a[j] = temp
#     return a
# }

# func compStringArr(a []string, b string) bool {
#     temp := ""
#     for _,v := range a{
#         temp +=v
#     }
#     return temp > b
# }

# func recur(a []string, curn int, count int, maxSoFar *string) {
#     if curn == len(a) || count == 0 {
#         return
#     }
#     //findMaxChar
#     maxChar := a[curn]
#     for i:= curn+1 ; i< len(a);i ++ {
#         if a[i] > maxChar {
#             maxChar = a[i]
#         }
#     }
#     //if MaxChar is same as curn, move on to next index
#     if maxChar == a[curn] {
#         recur(a, curn+1, count, maxSoFar)
#     } else {
#         //check if MaxChar at more than one place, recurse further with every possible swap
#         for i := curn+1 ; i < len(a) ; i++ {
#             if a[i] == maxChar {
#                 //if maxChar swap
#                 a = swap(a, curn, i)
#                 //compare to maxSoFar and save
#                 if  compStringArr(a, *maxSoFar) {
#                     temp := ""
#                     for _,v := range a{
#                         temp +=v
#                     }
#                     *maxSoFar = temp
#                 }
#                 //recur by decrementing remaingng swaps(count)
#                 recur(a, curn+1, count-1, maxSoFar)
#                 //swap back in place, to try other possible swap
#                 a = swap(a, i, curn)
#             }
#         }
#     }
# }