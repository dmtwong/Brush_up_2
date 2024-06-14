# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:43:42 2024

@author: USER
"""
# Problem Description
# You are given two numbers represented as integer arrays A and B, where each digit is an element.
#  You have to return an array which representing the sum of the two given numbers.
# The last element denotes the least significant bit, and the first element denotes the most significant bit.
# Note : Array A and Array B can be of different size. ( i.e. length of Array A may not be equal to length of Array B ).

# Problem Constraints
# 1 <= |A|, |B| <= 105
# 0 <= Ai, Bi <= 9

# Input Format
# The first argument is an integer array A. The second argument is an integer array B.

# Output Format
# Return an array denoting the sum of the two numbers.

# Example Input
# Input 1:
A = [1, 2, 3]
B = [2, 5, 5]
# Input 2:
A = [9, 9, 1]
B = [1, 2, 1]

# Example Output
# Output 1:
# [3, 7, 8]
# Output 2:
# [1, 1, 1, 2]

# Example Explanation
# Explanation 1:
# Simply, add all the digits in their place.
# Explanation 2:
# 991 + 121 = 1112
# Note that the resultant array size might be larger.

def addArrays(A, B):            
    # A = [9, 9, 1]
    # B = [1, 2, 1]
    str_A = [str(x) for x in A]
    str_B = [str(x) for x in B]
    num_A = int(''.join(str_A))
    num_B = int(''.join(str_B))
    
    result = str(num_A + num_B)
    res = []
    for i in result:
        res.append(i)
        
    return res


# # #     # Editoral:
# # #         # Python 
# class Solution:
#     # @param A : list of integers
#     # @param B : list of integers
#     # @return a list of integers
#     def addArrays(self, A, B):
#         A.reverse()
#         B.reverse()
#         C = []
#         carry = 0
#         i = 0
#         n = min(len(A), len(B))
#         while i < n:
#             x = carry + A[i] + B[i]
#             C.append(x%10)
#             carry = x//10
#             i += 1        
#         while i < len(A):
#             x = carry + A[i]
#             C.append(x%10)
#             carry = x//10
#             i += 1        
#         while i < len(B):
#             x = carry + B[i]
#             C.append(x%10)
#             carry = x//10
#             i += 1        
#         while carry > 0:
#             C.append(carry%10)
#             carry = carry//10        
#         C.reverse()        
#         return C

# C++ 
# vector<int> sum(vector<int> &A, vector<int> &B, int n, int m){
#     vector<int> ans; 
#     int i = n - 1, j = m - 1;
#     int carry = 0, s = 0;
#     while (j >= 0) {
#         s = A[i] + B[j] + carry;
#         ans.push_back(s % 10);
#         carry = s / 10;
#         i--;
#         j--;
#     }
#     while (i >= 0) {
#         s = A[i] + carry;
#         ans.push_back(s % 10);
#         carry = s / 10;
#         i--;
#     }
#     if (carry>0){
#         ans.push_back(carry);
#     }
#     reverse(ans.begin(), ans.end());
#     return ans;
# }
# vector<int> Solution::addArrays(vector<int> &A, vector<int> &B) {
#     int n = A.size();
#     int m = B.size();
#     if (n >= m)
#         return sum(A, B, n, m);
#     else
#         return sum(B, A, m, n);
# }

# Scala:
#     class Solution {
#     def addArrays(A: Array[Int], B: Array[Int]): Array[Int]  = {
       
#        var high1 = A.size -1
#        var high2 = B.size -1
#        var carry = false 

#        import scala.collection.mutable._
#        var st = Stack[Int]()

#        while(high1 >=0 && high2 >= 0) {
  
#           var res = 0
          
#           if(carry){
#               res = A(high1) + B(high2) + 1
#               carry = false
#           }
#           else {
#             res = A(high1) + B(high2)
#           }

#           if(res < 10){
#               st.push(res)
#           }
#           else{
#               carry = true
#               st.push(res % 10)
#           }

#           high1 -= 1
#           high2 -= 1
#        }

#        if(high1 <0){
#            for(i <- high2 to 0 by -1){
#                var res = 0
#                 if(carry){
#                     res = B(i) + 1
#                     carry = false
#                 }
#                 else {
#                     res = B(i)
#                 }

#                 if(res < 10){
#                     st.push(res)
#                 }
#                 else{
#                     carry = true
#                     st.push(res %10)
#                 }

#            }
#        }

#        if(high2 <0){
#            for(i <- high1 to 0 by -1){
#                var res = 0
#                 if(carry){
#                     res = A(i) + 1
#                     carry = false
#                 }
#                 else {
#                     res = A(i)
#                 }

#                 if(res < 10){
#                     st.push(res)
#                 }
#                 else{
#                     carry = true
#                     st.push(res %10)
#                 }

#            }
#        }

#        if(carry){
#            st.push(1)
#            carry = false
#        }

#        var arr = new ArrayBuffer[Int]()

#        while(!st.isEmpty){
#            arr += st.pop
#        }

#        return arr.toArray


#     }
# }

# GO:
#     /**
#  * @input A : Integer array
#  * @input B : Integer array
#  * 
#  * @Output Integer array.
#  */
# //  import "fmt"
# func addArrays(A []int , B []int )  ([]int) {
#     res := make([]int,0)
#     i := len(A)-1
#     j := len(B)-1
#     carry := 0

#     for  i >= 0 || j >= 0 { 
#         sum := 0
#         if i >=0 && j >= 0{
#             sum = A[i]+B[j] + carry
#         }
#         if i < 0 {
#             sum = B[j] + carry
#         }
#         if j < 0 {
#             sum = A[i] + carry
#         }
        
#         if (sum < 10){
#             carry = 0
#             res = append(res, sum)
#         } else {
#             carry = 1
#             res = append(res, sum%10)
#         }
#         i--
#         j--
#     }

#     if carry > 0 {
#         res = append(res, 1)
#     }

#     for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
#         res[i], res[j] = res[j], res[i]
#     }

#     return res
# }
