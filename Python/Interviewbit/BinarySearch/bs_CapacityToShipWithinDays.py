# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:23:10 2024

@author: USER
"""

# Problem Description
# A conveyor belt has packages that must be shipped from one port to another within B days.

# The ith package on the conveyor belt has a weight of A[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within B days.

# Problem Constraints
# 1 <= B <= |A| <= 5 * 105
# 1 <= A[i] <= 105

# Input Format
# First argument is array of integers A denoting the weights.
# Second argument is the integer B denoting the number of days. 

# Output Format
# Return the least weight capacity of the ship.


# Example Input
# Input 1:
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = 5
# Input 2:
solve(A, B)
A = [3, 2, 2, 4, 1, 4]
B = 3


# Example Output
# Ouput 1:
# 15
# Ouput 2:

# 6


# Example Explanation
# Explanation 1:
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and 
# splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# Explanation 2:

# A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
def solve(A, B):
    n_A = len(A)
    sum_A = sum(A)
    cap = sum_A
    max_A = max(A)
    result = -1
    
    def isValid(A, B, capa):
        total = 0
        count = 1
        for i in range(n_A):
            total += A[i]
            if total > capa:
                count += 1
                total = A[i]
            if count > B:
                return False
        return True

    while (max_A <= cap):
        mid = (cap + max_A) // 2 
        if isValid(A, B, mid):
            result = mid
            cap = mid - 1
        else:
            max_A = mid + 1
    return result
    
A = [ 16, 2, 11, 4, 18, 17, 17, 8, 8, 6, 7, 9, 17, 20, 10, 5, 2, 11, 3 ]
B = 10
solve(A, B)

# # #     # Editoral:
# # #         # Python 

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, weights, days):
#         def is_enough(capacity):  #helper function, to check if given capacity is enough
#             count = 1
#             max_weight = capacity
#             for w in weights:
#                 if w > max_weight:
#                     max_weight = capacity
#                     count += 1
#                 max_weight -= w
#             return  count <= days

#         l, r = max(weights), sum(weights)
#         while l < r:
#             m = (l+r) // 2
#             if is_enough(m):
#                 r = m
#             else:
#                 l = m+1
#         return l

# # Scala
# class Solution {
#     def solve(A: Array[Int], B: Int): Int  = {

#         def divisionOfCurLot ( A : Array[Int], currLot : Int) : Int = {
#             var res= 0
#             var sum = 0
#             for ( weight <- A){
#                 if( weight > currLot)
#                     return -1 
#                 if ( (sum + weight )> currLot){
#                     sum = weight
#                     res += 1
#                 }
#                 else sum = sum + weight
#             }
#             res + 1
#         }

#         var s = A.sum
#         //sumArr.foreach(print)
#         //b search over the sumArr 
        
#         var left = 0
#         var n = A.size
#         var right = s + 1
#         while ( left < right){
#             var mid = left + ( right - left ) / 2
#             //print(" mid : " + mid )
#             var currLot = mid
#             var curDiv = divisionOfCurLot(A , currLot) 
#             //print( " curDiv: " + curDiv)
#             if ( curDiv != -1 && curDiv <= B)
#                 right = mid
#             else left = mid + 1
#            // print("\n")
#         }
#         return right
        
#         //return 0
#     }
# }

# C++
# bool check(vector<int>&weights,int x, int days) {
#         int cnt=0;
#         int day=0;
#         for(auto i: weights) {
#             if(cnt+i<=x) cnt+=i; 
#             else day++, cnt=i;
#         }
#         if(day<days) return true;
#         return false;
#     }
# int Solution::solve(vector<int> &weights, int days) {
#     int start=1;
#     int end=1e9;
#     for(auto i: weights) start=max(start,i);
#     while(1)
#     {
#         int mid=(start+end)/2;
#         if(check(weights,mid,days)) end=mid;
#         else start=mid;
#         if(end-start<=1) break;
#     }
#     if(check(weights,start,days)) return start;
#     else return end;
# }

# GO:
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# func solve(A []int , B int )  (int) {
#     maxWeight := A[0]
#     sum := 0

#     for _, v := range A {
#         maxWeight = max(maxWeight, v)
#         sum += v
#     }

#     feasable := func(A []int, weight int, kDays int) bool {
#         daysUsed := 1
#         taken := 0
#         for _, v := range A {
#             taken += v
#             if taken > weight {
#                 daysUsed++
#                 if daysUsed > kDays {
#                     return false
#                 }
#                 taken = v
#             }
#         }
#         return true
#     }

#     for maxWeight < sum {
#         mid := (maxWeight+sum)/2

#         if feasable(A, mid, B) {
#             sum = mid
#         } else {
#             maxWeight = mid + 1
#         }
#     }
#     return maxWeight
# }

# func max(a, b int) int {
#     if a >= b {
#         return a
#     }
#     return b
# }
