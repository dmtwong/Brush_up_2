# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:21:47 2024

@author: USER
"""

# class Solution:
#     # @param A : list of integers
#     # @return a strings
#     def solve(self, A):

# Problem Description

# Given an array A containing N integers, find the variance of the array. Return your answer up to 2 decimal points.

def solve(A):
    import numpy as np
    result = np.var(A)
    return round(result, 2)


# Scala:
# class Solution {
#     def solve(A: Array[Int]): String  = {
        
#         def findMeanInt(x: Array[Int]): Double = x.sum.toDouble / x.length
        
#         def findMeanDouble(x: Array[Double]): Double = x.sum / x.length

        
#         def subtractAndSquare(x: Array[Int], mean: Double): Array[Double] = {
#             x.map { int =>
#                 (int - mean) * (int - mean)
#             }
#         }
        
#     val temp = (findMeanDouble(subtractAndSquare(A, findMeanInt(A))))
    
#     ((((temp * 100).round).toInt).toDouble / 100).toString
        
#     }
# }

# C++
# string Solution::solve(vector<int> &A) {

#     double st = 0;

#     double n = A.size();

#     for(int i=0; i<n; i++)

#         st += A[i];

#     double mean = st/n;

#     st=0;

#     for(auto x:A)

#         st += pow(x-mean,2);

#     st /= n;

    

#     // For rounding off

#     st *= 100;

#     st = round(st);

#     string s = to_string(st/100);

#     size_t p = s.find('.');

#     return s.substr(0,p+3);

# }

# GO:
#     import "strconv"
# /**
#  * @input A : Integer array
#  *
#  * @Output string.
#  */
# func solve(A []int) string {
#     s := 0.0
#     mid := middle(A)
#     _ = mid
#     for _, n := range A {
#         r := (float64(n) - mid)
#         s += r * r
#     }
#     s = s / (float64(len(A)))
#     str := strconv.FormatFloat(s, 'f', 2, 64)
#     return str
# }

# func middle(A []int) float64 {
#     var s float64
#     for _, n := range A {
#         s += float64(n)
#     }
#     return s / float64(len(A))
# }
